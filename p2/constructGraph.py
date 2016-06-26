__author__ = 'rylan'

from lxml import html
import networkx
import requests

def constructGraph(file):

    graph = networkx.Graph()

    # open html file of top 500 IMDB movies
    top500 = open(file, 'r')

    # convert html file into html tree for xpath searching
    tree = html.parse(top500)

    # extract movie elements from html document
    movies = tree.xpath('//body//a')

    for movie in movies:

        # extract movie title
        movieTitle = movie.text_content()

        # add movie title to graph
        if movieTitle not in graph.nodes():
            graph.add_node(movieTitle)

        # extract movie url
        movieURL = movie.values()[0]

        # convert movie html page into html tree for xpath searching
        moviePageTree = html.fromstring(requests.get(movieURL).content)

        # extract top 12 recommended movies for the given movie
        recommendedMovieNodes = moviePageTree.xpath('//div[@id = \'titleRecs\']//div[@class = \'rec_item\']//a/img')
        recommendedMovieTitles = [node.attrib['title'] for node in recommendedMovieNodes]

        for recommendedMovieTitle in recommendedMovieTitles:

            # add recommended movie to graph
            if recommendedMovieTitle not in graph.nodes():
                graph.add_node(recommendedMovieTitle)

            # connect recommended movie to original movie
            graph.add_edge(movieTitle, recommendedMovieTitle)

    return graph
