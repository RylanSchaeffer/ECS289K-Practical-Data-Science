__author__ = 'rylan'

import requests
from lxml import html

def scrape(sourceOne, sourceTwo):

    sources = [sourceOne, sourceTwo]

    # extract pages
    # try:
    pages = [requests.get(source) for source in sources]
    # except requests.exceptions.HTTPError:
    #     print "Error: Invalid HTTP response"
    # except requests.exceptions.TooManyRedirects:
    #     print "Error: Too many redirects"
    # except requests.exceptions.ConnectionError:
    #     print "Error: Network problem"

    # save Google News for manual confirmation
    f = open('googlenews.html', 'w')
    f.write(pages[0].content)
    f.close()

    # save Yahoo News for manual confirmation
    f = open('yahoonews.html', 'w')
    f.write(pages[1].content)
    f.close()

    # parse page contents into html trees
    trees = [html.fromstring(page.content) for page in pages]

    # extract article titles from Google
    GoogleContent = []
    for title in trees[0].xpath('//h2//a/span/text()'):
        try:
            GoogleContent.append(str(title))
        except UnicodeEncodeError:
            pass

    # extract article titles from Yahoo
    YahooContent = []
    for title in trees[1].xpath('//h3//a/text()'):
        try:
            YahooContent.append(str(title))
        except UnicodeEncodeError:
            pass

    return YahooContent, GoogleContent