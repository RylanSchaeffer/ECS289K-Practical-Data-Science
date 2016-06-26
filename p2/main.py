__author__ = 'rylan'

import constructGraph
import matplotlib.pyplot as plt
import operator
import networkx

file = 'inpFile_IMDB_Top500_2015.html'

# construct graph of top 500 IMDB movies and their corresponding top 12 recommended movies
graph = constructGraph.constructGraph(file)

# create and save interactive visual representation of graph, without labels
networkx.draw(graph, with_labels=False)
plt.savefig('graphwithoutlabels.png')

# create interactive visual representation of graph, with labels
networkx.draw(graph, with_labels=True)

# calculate number of connected components
print 'There are %d connected components\n' % networkx.number_connected_components(graph)

# generate each connected component subgraph
subgraphs = list(networkx.connected_component_subgraphs(graph))

# for each connected component subgraphs, calculate which node has the highest fraction of nodes connected to it
centralNodes = [sorted(networkx.degree_centrality(subgraph).items(), key=operator.itemgetter(1), reverse=True)
                for subgraph in subgraphs]

# print the most-connect node for each subgraph with its corresponding degree of connectivity
for i in range(0, len(centralNodes)):
    print 'In connected component %d of %d nodes, the most-connected movie (%s) is connected to %0.2f percent of the nodes in ' \
          'the subgraph.\n' % (i+1, len(centralNodes[i]), centralNodes[i][0][0], 100*centralNodes[i][0][1])

