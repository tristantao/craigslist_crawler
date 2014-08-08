craigslist_crawler
==================

a simple script to crawl some craigslist ads

run via

    python main.python

Issues:

    * Sometimes BS crashes with infinite recursion (probably a BS issue)
    * Sometimes connectino gets reset, we just ignore and conitnue.


We also stop crawling past result 2500, since craiglist stops you looking past it anyways (without having to go through some extra hoop).
