#!/usr/bin/env python3

import icalendar  as ics
import panflute   as pf
import datetime   as dt
import dateparser as dp

# TODO.


DATE_FIELDS = ["due", "start", "end", "duration"]
CTN_FIELDS  = ["url", "organizer", "location"]

def parse_ics_item(elem,doc):
    if not (isinstance(elem, pf.Plain) and len(elem.content) > 1):
        return

    first = elem.content[0]
    if not isinstance(first, pf.Strong):
        return
    if not len(first.content) > 0:
        return
    if not isinstance(first.content[0], pf.Str):
        return

    strkey = first.content[0].text
    if not (len(strkey) > 0 and strkey[-1] == ":"):
        return

    key   = strkey[:-1].lower()
    value = pf.Plain(*elem.content[1:])

    return (key, value)


    

def rewrite_ics(elem, doc):
    if isinstance(elem, pf.Div) and "ics-todo" in elem.classes and doc.format == "latex":
        return [pf.RawBlock("\\begin{quote}",format="latex"),
                *elem.content[1:],
                pf.RawBlock("\\end{quote}",format="latex")]
    elif isinstance(elem, pf.Div) and "ics-todo" in elem.classes:
        title = elem.content[0]  # title of the event
        data  = elem.content[1]  # data fields
        hz    = elem.content[2]  # horizontal rule
        desc  = elem.content[3:] # full description = rest of the text

        values = {}
        for item in data.content:
            if isinstance(item, pf.ListItem):
                p = parse_ics_item(item.content[0], doc)
                if p:
                    values[p[0]] = p[1]

        event = ics.Event()
        event.add("summary", pf.stringify(title))
        event.add("description", pf.stringify(desc))
        for f in CTN_FIELDS:
            v = values.get(f, None)
            if v:
                event.add(f, pf.convert_text(pf.stringify(v), output_format="plain"))
        for f in DATE_FIELDS:
            v = values.get(f, None)
            if v:
                d = dp.parse(pf.stringify(v))
                event.add(f, d)

        if "events" not in doc.metadata:
            doc.metadata["events"] = []

        doc.metadata["events"].append(pf.MetaBlocks(pf.RawBlock(event.to_ical().decode("utf-8"), format="html")))


if __name__ == "__main__":
    pf.run_filter(rewrite_ics)
