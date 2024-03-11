#!/usr/bin/env python3

import icalendar  as ics
import panflute   as pf
import datetime   as dt
import dateparser as dp

# TODO.

DATE_FIELDS = ["due", "start", "end", "duration"]
CTN_FIELDS  = ["url", "organizer", "location"]

def rewrite_ics(elem, doc):
    if isinstance(elem, pf.Div) and "ics-todo" in elem.classes and doc.format == "latex":
        return [pf.RawBlock("\\begin{quote}",format="latex"),
                *elem.content[1:],
                pf.RawBlock("\\end{quote}",format="latex")]
    elif isinstance(elem, pf.Div) and "ics-todo" in elem.classes:
        title = elem.content[0] # title of the event
        data  = elem.content[1] # data fields
        hz    = elem.content[2] # horizontal rule
        desc  = elem.content[3:] # full description = rest of the text

        values = {}
        raise ValueError(data)

        event = ics.Event()
        event.add("summary", pf.stringify(title))
        event.add("description", pf.stringify(desc))


if __name__ == "__main__":
    pf.run_filter(rewrite_ics)
