#!/usr/bin/env python3
#
# Splits exercices (heading of level 2) into the body of the exercice
# hints (heading of level 3)
# and its solution (last heading of level 3)
#
# The solutions are added in the metadata dictionnary of solutions
# the hints are added in the metadata dictionnary of hints
#
# This can then be used by templates.

import panflute as pf

from itertools import groupby

def is_section_div(elem):
    return isinstance(elem, pf.Div) and "section" in elem.classes and len(elem.content) > 0 and isinstance(elem.content[0], pf.Header)

def enumerate_headings(elem):
    """ Goes up in the tree to find all parent headings """
    current = elem
    while current is not None:
        current = current.parent
        if isinstance(current, pf.Header):
            yield current
        elif is_section_div(current):
            yield current

def split_exercises(elem, doc):
    if is_section_div(elem) and "def" in elem.classes:
        title = [pf.RawInline("\\begin{definition}[{", format="latex"), *elem.content[0].content, pf.RawInline("}] \\label{"+ elem.identifier +"}", format="latex")]
        end   = pf.RawBlock("\\end{definition}", format="latex")
        return [pf.Plain(*title), *elem.content[1:], end]
    elif is_section_div(elem) and "exercise" in elem.classes:
        title = [pf.RawInline("\\begin{exercise}[{", format="latex"), *elem.content[0].content, pf.RawInline("}] \\label{"+ elem.identifier +"}", format="latex")]
        end   = pf.RawBlock("\\end{exercise}", format="latex")
        return [pf.Plain(*title), *elem.content[1:], end]
    elif is_section_div(elem) and "hint" in elem.classes:
        parents = list(enumerate_headings(elem))
        eid = parents[0].identifier
        if "hints" not in doc.metadata:
            doc.metadata["hints"] = []
        doc.metadata["hints"].append(pf.MetaMap(eid=eid, 
                                                id=elem.identifier,
                                                title=pf.stringify(elem.content[0]),
                                                content=pf.MetaBlocks(*elem.content[1:])))
        return pf.Plain(pf.RawInline("$\\triangleright$ \\cref{" + elem.identifier +  "}", format="latex"))
    elif is_section_div(elem) and "solution" in elem.classes:
        parents = list(enumerate_headings(elem))
        raise ValueError(parents)
        eid = parents[1].identifier
        if "solutions" not in doc.metadata:
            doc.metadata["solutions"] = []
        doc.metadata["solutions"].append(pf.MetaMap(eid=eid,
                                                    id=elem.identifier,
                                                    title=pf.stringify(elem.content[0]),
                                                    content=pf.MetaBlocks(*elem.content[1:])))
        return pf.Plain(pf.RawInline("$\\triangleright$ \\cref{" + elem.identifier +  "}", format="latex"))


def main(doc=None):
    return pf.run_filter(split_exercises, doc=doc)

if __name__ == '__main__':
    main()
