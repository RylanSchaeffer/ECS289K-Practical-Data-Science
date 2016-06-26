__author__ = 'rylan'

from scrape import scrape
from compare import compare
from printToHTML import printToHTML

# sourceOne = 'https://news.google.com/'
# sourceTwo = 'https://news.yahoo.com/'
sourceOne = raw_input('Please enter first newsource: ')
sourceTwo = raw_input('Please enter second newsource: ')

articleTitles = scrape(sourceOne, sourceTwo)
pairings = compare(articleTitles[0], articleTitles[1])
printToHTML(pairings)
