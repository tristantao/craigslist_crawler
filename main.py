import sys
import time, csv, optparse
from bs4 import BeautifulSoup, SoupStrainer
import requests
from datetime import date

def get_raw_html(raw_link):
    print "[STATUS] Scraping {0}".format(raw_link)
    r = requests.get(raw_link)
    if(r.status_code != requests.codes.ok):
        print "WARN: Request did not come back with OK status code for: %s \nExiting" % raw_link
        exit(1)
    raw_html = r.text
    return raw_html


def get_listing_url(search_link):
    #looks on a result result page, and returns a set() containing individuals ads.
    #will return empty set if no more ads are found.
    location_tag = search_link.split("search")[0]
    ad_links = set()
    raw_html = get_raw_html(search_link)
    bt_struct = BeautifulSoup(raw_html, "html.parser")
    for listing_link in bt_struct.find_all('a', {'class': 'i'}):
        ad_links.add(location_tag + listing_link['href'])
    return ad_links




def generate_search_url(region, term, min_price, max_price):
    static_base = "http://%s.craigslist.org/search/sss?query=%s&minAsk=%s&maxAsk=%s&sort=rel"
    return static_base % (region, term, min_price, max_price)


if __name__ == '__main__':
    search_term = sys.argv[1]
    REGIONS = ['losangeles', 'sfbay']
    SEARCH_TERM = 'motorcycle'
    MIN_PRICE = 0
    MAX_PRICE = 0

    print search_term
    while True:
        listing_batch = get_listing_ur
        pass
