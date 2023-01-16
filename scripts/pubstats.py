from scholarly import scholarly

# Google Scholar
scholar_id = "QoX9bu8AAAAJ"

author = scholarly.search_author_id(scholar_id)
scholarly.fill(author, sections=["indices"])

with open("_includes/metrics/gs_h.md", "w") as fp:
    fp.write(str(author["hindex"]))

with open("_includes/metrics/gs_citedby.md", "w") as fp:
    fp.write(str(author["citedby"]))
