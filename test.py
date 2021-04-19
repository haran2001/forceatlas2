import networkx as nx
import matplotlib.pyplot as plt
from fa2 import ForceAtlas2
import numpy as np

# Create ForceAtlas2 object with desired parameters
forceatlas2 = ForceAtlas2(
                          # Behavior alternatives
                          outboundAttractionDistribution=True,  # Dissuade hubs
                          linLogMode=False,  # NOT IMPLEMENTED
                          adjustSizes=False,  # Prevent overlap (NOT IMPLEMENTED)
                          edgeWeightInfluence=1.0,

                          # Performance
                          jitterTolerance=1.0,  # Tolerance
                          barnesHutOptimize=True,
                          barnesHutTheta=1.2,
                          multiThreaded=False,  # NOT IMPLEMENTED

                          # Tuning
                          scalingRatio=2.0,
                          strongGravityMode=False,
                          gravity=1.0,

                          # Log
                          verbose=True)

# G = nx.grid_2d_graph(25, 25)
# print(nx.info(G))
# positions = forceatlas2.forceatlas2_networkx_layout(G, pos=None, iterations=5000)
# nx.draw_networkx(G, positions, node_size=20, with_labels=False, alpha=0.5)
# plt.axis('off')
# plt.show()

G = nx.random_geometric_graph(400, 0.2)
print(nx.info(G))
positions = forceatlas2.forceatlas2_networkx_layout(G, pos=None, iterations=2000)
# nx.draw_networkx_nodes(G, positions, node_size=20, with_labels=False, node_color="blue", alpha=0.4)
nx.draw_networkx_nodes(G, positions, node_size=20, node_color="blue", alpha=0.4)
nx.draw_networkx_edges(G, positions, edge_color="green", alpha=0.05)
plt.axis('off')
plt.show()