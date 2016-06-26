__author__ = 'rylan'

def printToHTML(pairings):

    # open file
    f = open('ECS289KAssignment1.html', 'w')

    # set up basic html structure
    f.write('<!DOCTYPE html>\n<html>\n'
            '<head>\n<title>ECS289K Assignment 1</title>\n'
            '<style>\ntable, th, td {\n\tborder: 1px solid black;\n\tborder-collapse: collapse;\n}\n'
            'th, td {\n\tpadding: 15px;\n}\n</style>\n</head>\n'
            '<h1>ECS289K Assignment 1 - Paired News Articles</h1>\n<table style="width:100%">\n'
            '<tr>\n<th>Google News</th>\n<th>Yahoo News</th>\n</tr>\n')

    # for each possible pair of articles
    for key1 in pairings.keys():
        for key2 in pairings[key1].keys():

            # if the matching value is greater than 12, the topics are declared to be concerning the same topic
            # note: 12 is a rough estimate
            if pairings[key1][key2] > 13:
                f.write('<tr>\n' + '<td>' + key1 + '</td>\n<td>' + key2 + '</td>\n</tr>\n')

    # finish html document and close file
    f.write('</table>\n</body>\n</html>\n')
    f.close()