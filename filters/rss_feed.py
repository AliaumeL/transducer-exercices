#!/usr/bin/env python3
#
# Aliaume LOPEZ - 2024 GPL-3.0
#
# Generate an RSS feed from a list of markdown files. 
#
# Files are read from the metadata value `items`, and their content is replaced
# with raw html content read from the corresponding xml file.
#

import panflute as pf

def finalize(doc):
    pass

def prepare(doc):
    # list items from the metadata
    items = doc.get_metadata('items')
    files = []
    for i in items:
        try:
            with open(i, 'r') as file:
                files.append(file.read())
        except FileNotFoundError:
            continue
    doc.metadata['items'] =  [pf.RawBlock(f, format='html') for f in files]

if __name__ == '__main__':
    pf.run_filter(lambda x,d: x, prepare=prepare, finalize=finalize)
