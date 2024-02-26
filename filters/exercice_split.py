##
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

def enumerate_subheadings(elem, start, stop):
    body = list(enumerate_until_breakpoint(elem.next, stop))
    groups = [list(group) 
              for key, group in groupby(body, key=lambda x: (isinstance(x, pf.Header) and x.level == start))]
    out = { "id": elem.identifier, "body": pf.MetaBlocks(*groups[0]), "title": pf.stringify(elem), "content": pf.MetaList(groups[0]), "hints": [] }
    # raise ValueError(groups)
    for (k,v) in zip(groups[1::2], groups[2::2]):
        k = k[0]
        if "hint" in k.classes:
            out["hints"].append({ "title": pf.stringify(k), "id": k.identifier, "body": v })
        elif "solution" in k.classes:
            out["solution"] = v
    return out


current_header = None
current_exercise = None

def is_section_div(elem):
    return isinstance(elem, pf.Div) and "section" in elem.classes and len(elem.content) > 0 and isinstance(elem.content[0], pf.Header)

# This function is called for each element in the document
# if the element is a level two heading, then it means that it is
# an exercice, in which case, we collect all the elements until the next
# level two heading, and consider them as the body of the exercice
# that we add to the metadata dictionnary
def split_exercises(elem, doc):
    global current_exercise, current_header
    if is_section_div(elem) and "def" in elem.classes:
        title = [pf.RawInline("\\begin{definition}[{", format="latex"), *elem.content[0].content, pf.RawInline("}] \\label{"+ elem.identifier +"}", format="latex")]
        end   = pf.RawBlock("\\end{definition}", format="latex")
        return [pf.Plain(*title), *elem.content[1:], end]
    elif is_section_div(elem) and "exercise" in elem.classes:
        # we set the current exercice to the current element
        current_exercise = elem
        # create a latex block with the content of the exercice
        title = [pf.RawInline("\\begin{exercise}[{", format="latex"), *elem.content[0].content, pf.RawInline("}] \\label{"+ elem.identifier +"}", format="latex")]
        end   = pf.RawBlock("\\end{exercise}", format="latex")
        return [pf.Plain(*title), *elem.content[1:], end]
        # return elem
    elif current_exercise and is_section_div(elem) and "hint" in elem.classes:
        eid = current_exercise.identifier
        if "hints" not in doc.metadata:
            doc.metadata["hints"] = []
        doc.metadata["hints"].append(pf.MetaMap(eid=eid, 
                                                id=elem.identifier,
                                                title=pf.stringify(elem.content[0]),
                                                content=pf.MetaBlocks(*elem.content[1:])))
        return [pf.RawBlock("$\\triangleright$ \\cref{" + elem.identifier +  "}", format="latex")]
    elif current_exercise and is_section_div(elem) and "solution" in elem.classes:
        eid = current_exercise.identifier
        if "solutions" not in doc.metadata:
            doc.metadata["solutions"] = []
        doc.metadata["solutions"].append(pf.MetaMap(eid=eid,
                                                    id=elem.identifier,
                                                    title=pf.stringify(elem.content[0]),
                                                    content=pf.MetaBlocks(*elem.content[1:])))
        return []


def main(doc=None):
    return pf.run_filter(split_exercises, doc=doc)

if __name__ == '__main__':
    main()
