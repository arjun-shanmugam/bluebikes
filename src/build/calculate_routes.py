import matplotlib.pyplot as plt
import osmnx as ox
somerville_graph = ox.graph_from_place('Somerville, MA', network_type='drive')
somerville_graph = ox.projection.project_graph(somerville_graph, to_latlong=True
plt.show()