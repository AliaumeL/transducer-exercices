# Things to do

## Community

- [x] allow to edit pages by linking to the github repository
- [x] allow to comment on pages by opening issues on the github repository
- [x] create an "rss" feed for the website using
  <https://github.com/chambln/pandoc-rss> or a variant thereof
  

## Calendar Research

> I want to have a calendar (or several calendars)
  on the static website.

It is not a good idea to *automatically* generate events.
-> it makes *large* and complicated yaml headers

Calendar events are complicated. It can be VTODO, VEVENT, response, locations,
chairman etc. These are complicated enough to be in a separate file.

The idea: a markdown file is describing an event feed. This is probably the
best thing because events are not self contained. This means desinging a
specific pandoc writer.

## Indexing

Create a searchable index using stork. The main problem right now is to split
on sections.

## Tooling

- [ ] precompute mathjax to speed up page rendering
- [ ] create test suites for the pages (unused references, broken links, etc.)
- [ ] allow to do *cross page references* seamlessly 
- [ ] enable knowledge sharing between pages
- [ ] allow to use knowledges in mathematical definitions
- [ ] allow to share mathematical definitions between markdown files
- [ ] create a "book" output, merging exercise sessions and homeworks
