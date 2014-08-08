import sys
import os
import time, csv, optparse
from bs4 import BeautifulSoup, SoupStrainer
import requests
from datetime import date
import pdb
import random
import traceback

def get_raw_html(raw_link):
    #returns the raw html of a page, errors and exits if request doesn't go through
    #Will return emptry string IF an issue comes up
    print "[STATUS] Scraping {0}".format(raw_link)

    try:
        r = requests.get(raw_link)
        if (r.status_code != requests.codes.ok):
            print "WARN: Request did not come back with OK status code for: %s \nExiting" % raw_link
            exit(1)
        raw_html = r.text
    except Exception e:
        print "ERR: Request threw an error: %s \nReturning" % raw_link
        print traceback.format_exc()
        return ""
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

def generate_search_url(region, page, term, min_price, max_price):
    #static_base = "http://%s.craigslist.org/search/sss?s=%s&query=%s&minAsk=%s&maxAsk=%s&sort=rel"
    static_base = "http://%s.craigslist.org/search/sss?s=%s&maxAsk=%s&minAsk=%s&query=%s&sort=rel"
    return static_base % (region, page, min_price, max_price, term)


def crawl_and_output(ad_links, output_prefix, folder):
    #ad_links is a set() of links to individual ads.
    #output_prefix is the prefix of the file that gets outputted.
    for ad in ad_links:
        output_id = ad.split("org/")[1].replace('.html' ,'').replace('/', '_')
        output_path = os.path.join(os.getcwd(), folder, (output_prefix+output_id))

        f = open(output_path, 'w')
        raw_html = get_raw_html(ad)
        bt_struct = BeautifulSoup(raw_html, "html.parser")
        body = bt_struct.find('section', {'id': 'postingbody'})
        #pdb.set_trace()
        f.write(str(body))
        f.close()
        time.sleep(random.randint(50, 250) / 1000.0)


if __name__ == '__main__':
    REGIONS = ['losangeles', 'sfbay']
    SEARCH_TERM = 'motorcycle'
    MIN_PRICE = 0
    MAX_PRICE = 0
    OUTPUT_PREFIX = 'moto'
    CURRENT_PAGE = 0

    while True:
        search_url = generate_search_url(REGIONS[1], CURRENT_PAGE, SEARCH_TERM, MIN_PRICE, MAX_PRICE)
        ad_links = get_listing_url(search_url)
        crawl_and_output(ad_links, OUTPUT_PREFIX, 'data/sfbay/')

        if len(ad_links) == 0:
            CURRENT_PAGE = 0
            break
        else:
            CURRENT_PAGE += 100
        time.sleep(random.randint(10,30) / 10.0)

