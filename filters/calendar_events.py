#!/usr/bin/env python3
#
# Parses the metadata of the file to produce
# calendar events 
#
# uses the metadata inside the
# markdown file to build an event
#
# event : 
#   type: todo | event
# start : date
# end   : date
# due   : date
# duration : date
# description : string
# summary : string
# url : string
# geo : string
# location : string
# organizer : string
# contact : string
# last-modified : string

import icalendar  as ics
import panflute   as pf
import datetime   as dt
import dateparser as dp

def prepare(doc):
    #event = doc.get_metadata("event")
    #if not event:
    #    return

    event = ics.Event()

    start = doc.get_metadata("start")
    end   = doc.get_metadata("end")
    dur   = doc.get_metadata("duration")
    
    # invalid event
    if ((start is None) or (end is None)) and (dur is None):
        return 

    if start:
        event.add("start", dp.parse(start, settings={'TO_TIMEZONE': 'UTC'}))
    if end:
        event.add("end", dp.parse(end))
    if dur:
        event.add("duration", dp.parse(dur))

    skeys = ["summary", "description", "location", "url"]
    for skey in skeys:
        v = doc.get_metadata(skey)
        if v and isinstance(v,str):
            event.add(skey, v)
        elif v:
            event.add(skey, pf.stringify(v))

    doc.metadata["event"] = pf.Str(event.to_ical().decode("utf8"))

if __name__ == "__main__":
    pf.run_filter(lambda x,d: x, prepare=prepare)
