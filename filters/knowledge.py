#!/usr/bin/env python3

import panflute as pf

def run_knowledge(elem, doc):
    if isinstance(elem, pf.Quoted) and elem.quote_type == "DoubleQuote":
        return [pf.RawInline("\\intro{", format="latex"),
                pf.RawInline("<span class=\"intro\">", format="html"),
                *elem.content,
                pf.RawInline("</span>", format="html"),
                pf.RawInline("}", format="latex")]
    elif isinstance(elem, pf.Quoted) and elem.quote_type == "SingleQuote":
        return [pf.RawInline("\\kl{", format="latex"),
                pf.RawInline("<span class=\"kl\">", format="html"),
                *elem.content,
                pf.RawInline("</span>", format="html"),
                pf.RawInline("}", format="latex")]
    elif isinstance(elem, pf.Code) and "kl" in elem.classes:
        return [pf.RawInline("\\kl{", format="latex"),
                pf.RawInline("<span class=\"kl\">", format="html"),
                *elem.content,
                pf.RawInline("</span>", format="html"),
                pf.RawInline("}", format="latex")]

def main(doc=None):
    return pf.run_filter(run_knowledge, doc=doc)

if __name__ == '__main__':
    main()
