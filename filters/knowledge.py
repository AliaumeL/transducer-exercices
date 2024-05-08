#!/usr/bin/env python3

import panflute as pf

# state is 
# a dictionnary with the following fields:
# - knowledge-forward: a dictionnary that maps knowledge 'labels'
#   to the knowledge object itself (with synonyms and potential other
#   fields defined)
# - knowledge-reverse: a dictionnary that maps synonyms 
#   to knowledge 'labels' names
# - knowledge-undefined: a dictionnary that maps 
#   undefined names to the number of times they were used


# TODO: 
# - in the preprocessing phase, find out which knowledges
#   are defined.
# - use this information to distinguish between dead links
#   and undefined knowledges

def default_state():
    return { "knowledge-forward": {},
             "knowledge-reverse": {},
             "knowledge-undefined": {} }

def resolve_knowledge(elem, doc, state):
    elem = pf.stringify(elem)
    kdef = state["knowledge-forward"]
    krev = state["knowledge-reverse"]
    kudf = state["knowledge-undefined"]
    if elem in krev:
        return krev[elem]
    elif elem in kudf:
        kudf[elem] += 1
    else:
        kudf[elem] = 1
    return None

def slugify(text):
    """ Poor man's slugify """
    return text.lower().replace(" ", "-")

def prepare(doc,state):
    if "knowledges" not in doc.metadata:
        doc.metadata["knowledges"] = []
        return doc
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
        state["knowledge-forward"][name] = knowledge
        for syn in synonyms:
            state["knowledge-reverse"][syn] = name

def finalize(doc,state):
    l = list( { "name": k, "count": v }
              for k,v in state["knowledge-undefined"].items() )
    doc.metadata["knowledge-undefined"] = l
    return doc

def run_knowledge(elem, doc, state):
    if isinstance(elem, pf.Quoted) and elem.quote_type == "DoubleQuote":
        if doc.format == "latex":
            return [pf.RawInline("\\intro{", format="latex"),
                    *elem.content,
                    pf.RawInline("}", format="latex")]
        else:
            kl_resolve = resolve_knowledge(pf.Plain(*elem.content),
                                           doc, 
                                           state)
            if kl_resolve is None:
                return pf.Span(*elem.content,
                            classes=["kl-undefined", "kl-intro"])

            return pf.Span(*elem.content,
                            identifier=kl_resolve,
                            classes=["kl-intro"])
    elif ((isinstance(elem, pf.Quoted) and elem.quote_type == "SingleQuote")
          or
          (isinstance(elem, pf.Span) and "kref" in elem.classes)):
        if doc.format == "latex":
            return [pf.RawInline("\\kl{", format="latex"),
                    *elem.content,
                    pf.RawInline("}", format="latex")]
        else:
            kl_resolve = resolve_knowledge(pf.Plain(*elem.content),
                                           doc, 
                                           state)
            if kl_resolve is None:
                return pf.Span(*elem.content,
                            classes=["kl-undefined", "kl-ref"])
            # Try to find a good alternative text for the link
            kl_def = state["knowledge-forward"].get(kl_resolve, {})
            desc = kl_def["name"] if "name" in kl_def else kl_resolve
            return  pf.Link(*elem.content,
                            url=f"#{kl_resolve}",
                            title=f"Definition of {desc}",
                            # identifier="todo-add-backlinks",
                            classes=["kl-ref"])

def main(doc=None):
    state = default_state()
    # Closures to the rescue of state passing 
    pf.run_filter(run_knowledge, 
                  prepare=lambda doc: prepare(doc,state),
                  finalize=lambda doc: finalize(doc,state),
                  doc=doc,
                  state=state)

if __name__ == '__main__':
    main()
