__author__ = 'rylan'

import re
import string

def compare(titlesOne, titlesTwo):

    # pairings is a nested dictionary, with the following structure:
    # pairings[Title of Article from Source One][Title of Article from Source Two] =
    #       sum of length of words common to both of the two articles' titles
    pairings = {}

    for titleOne in titlesOne:

        pairings[titleOne] = {}

        # remove punctuation and split article title into words
        one = titleOne.translate(None, string.punctuation).split()

        for titleTwo in titlesTwo:

            # initialize sum of length of words in common to 0
            pairings[titleOne][titleTwo] = 0

            two = titleTwo.translate(None, string.punctuation).split()

            # for each word in the first article's title, search for the word in the second article's title
            for word in set(one):

                # exclude I, a, an, not etc.
                if len(word) <= 3:
                    continue

                word = word.lower()

                # if the last character is 's', then the word may be a pluralization of another word; in that case,
                # append a '?' to the RX pattern because the other article may use the singular form of the word
                word = word+'?' if word[-1] == 's' else word

                if re.search(word, titleTwo.lower()):

                    pairings[titleOne][titleTwo] += len(word)

                    if word[-1] == '?':
                        pairings[titleOne][titleTwo] -= 2

             # for each word in the second article's title, search for the word in the first article's title
            for word in set(two):

                # exclude I, a, an, not etc.
                if len(word) <= 3:
                    continue

                word = word.lower()

                # if the last character is 's', then the word may be a pluralization of another word; in that case,
                # append a '?' to the RX pattern because the other article may use the singular form of the word
                word = word+'?' if word[-1] == 's' else word

                if re.search(word, titleOne.lower()):

                    pairings[titleOne][titleTwo] += len(word)

                    # penalize potential for non-pluralized words
                    if word[-1] == '?':
                        pairings[titleOne][titleTwo] -= 2


    return pairings