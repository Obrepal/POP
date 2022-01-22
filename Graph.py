import networkx as nx
import pandas as pd
import matplotlib.pyplot as plt


edges = pd.DataFrame({'source' : [2, 4, 5, 3, 0, 2, 5, 4, 7, 3, 6, 4],
                      'target' : [1, 7, 3, 5, 5, 0, 6, 2, 8, 8, 7, 7],
                      'weight' : [5, 3, 20, 2, 5, 3, 2, 6, 7, 3, 3, 2]})

nodes = pd.DataFrame({'node' : [0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
                      'name' : ['Foo', 'Bar', 'Baz','Foo', 'Bar', 'Baz','Foo', 'Bar', 'Baz','ee'],
                      'visited' : [0, 0, 0, 0, 0, 0, 0, 0, 0,0],
                      'spice' : [0,11,25,70,8,9,5,8,9,10]
                      })


G = nx.Graph()

G = nx.from_pandas_edgelist(edges, 'source', 'target', 'weight')

nx.set_node_attributes(G, pd.Series(nodes.visited, index=nodes.node).to_dict(), 'visited')
nx.set_node_attributes(G, pd.Series(nodes.name, index=nodes.node).to_dict(), 'name')
nx.set_node_attributes(G, pd.Series(nodes.spice, index=nodes.node).to_dict(), 'spice')


labels = nx.get_edge_attributes(G,"weight")
#pos = nx.spring_layout(G,k=1, iterations=4)
pos=nx.fruchterman_reingold_layout(G)
node_labels = nx.get_node_attributes(G,'spice')
#nx.draw_networkx_labels(G, pos,labels = node_labels)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
nx.draw(G,pos, with_labels=True,font_color='black',node_color='red',node_size=500)
plt.show()
