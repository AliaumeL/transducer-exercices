#!/usr/bin/env python3

import panflute as pf

def slugify(text):
    """ Poor man's slugify """
    return text.lower().replace(" ", "-")

def prepare(doc):
    doc.metadata["knowledge-reverse"] = {}
    doc.metadata["knowledge-undefined"] = {}
    if "knowledges" not in doc.metadata:
        doc.metadata["knowledges"] = []
        return
    for number, knowledge in enumerate(doc.metadata["knowledges"]):
        if "synonyms" not in knowledge:
            continue
        synonyms = [ pf.stringify(x) for x in knowledge["synonyms"]  ]
        if len(synonyms) == 0:
            continue
        if "name" in knowledge:
            name = knowledge["name"]
        else: 
            name = f"{synonyms[0]} {number}"
        name = slugify(name)
        for syn in synonyms:
            doc.metadata["knowledge-reverse"][syn] = name

def finalize(doc):
    if "knowledge-undefined" in doc.metadata:
        d = doc.metadata["knowledge-undefined"].content.dict
        l = list( { "name": k, "count": d[k] }
                  for k,v in d.items() )
        doc.metadata["knowledge-undefined"] = l

def resolve_knowledge(elem, doc):
    """ We stringify the element, search for a corresponding
        table in the 
    """
    elem = pf.stringify(elem)
    if "knowledge-reverse" in doc.metadata and elem in doc.metadata["knowledge-reverse"]:
        return pf.stringify(doc.metadata["knowledge-reverse"][elem])
    else:
        if elem not in doc.metadata["knowledge-undefined"]:
            doc.metadata["knowledge-undefined"][elem] = 1
        else:
            doc.metadata["knowledge-undefined"][elem] += 1
        return "undefined"

def run_knowledge(elem, doc):
    if isinstance(elem, pf.Quoted) and elem.quote_type == "DoubleQuote":
        kl_resolve = resolve_knowledge(pf.Plain(*elem.content), doc)
        if doc.format == "latex":
            return [pf.RawInline("\\intro{", format="latex"),
                    *elem.content,
                    pf.RawInline("}", format="latex")]
        else:
            return pf.Span(*elem.content,
                            identifier=kl_resolve,
                            classes=["kl-intro"])
    elif isinstance(elem, pf.Quoted) and elem.quote_type == "SingleQuote":
        kl_resolve = resolve_knowledge(pf.Plain(*elem.content), doc)
        if doc.format == "latex":
            return [pf.RawInline("\\kl{", format="latex"),
                    *elem.content,
                    pf.RawInline("}", format="latex")]
        else:
            return  pf.Link(*elem.content,
                            url=f"#{kl_resolve}",
                            title=f"knowledge-definition",
                            identifier="todo-add-backlinks",
                            classes=["kl-ref"])

def main(doc=None):
    return pf.run_filter(run_knowledge, doc=doc, prepare=prepare, finalize=finalize)

if __name__ == '__main__':
    main()
