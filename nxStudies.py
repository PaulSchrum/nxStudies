# -*- coding: utf-8 -*-

import networkx as nx
import matplotlib.pyplot as plt
import random

class PowerNode(object):
    def __init__(self, an_int):
        self.id = an_int
        self.power = 0.0

    def __repr__(self):
        return "{0} pow={1:0.2f}  ".format(self.id, self.power)

class PowerEdge(object):
    def __init__(self, an_int, start_node, end_node):
        self.id = an_int
        self.capacity = 0.5
        self.flow = 0.0
        self.start_node = start_node
        self.end_node = end_node

    def __repr__(self):
        return "id>{0}=flow:{1}  {2} to {3}".format(self.id, self.flow,
                self.start_node.id, self.end_node.id)

node_count = 7
edge_count = 9

node_seed = set(range(node_count))
edge_seed = range(edge_count)

g = nx.DiGraph()

random.seed(72)
g.add_nodes_from([PowerNode(i) for i in node_seed])
ttl_power = 0.0
for a_node in g.nodes:
    a_node.power = random.uniform(-1.0, 1.0)
    ttl_power += a_node.power

nodes_list = list(g.nodes)
first_node = nodes_list[0]
ttl_power = sum((n.power for n in g.nodes))
first_node.power -= ttl_power
ttl_power = sum((n.power for n in g.nodes))

print(ttl_power)
print()

for i in edge_seed:
    n1 = 0
    n2 = 0
    while n1 == n2:
        n1 = random.choice(nodes_list)
        n2 = random.choice(nodes_list)

    g.add_edge(n1, n2, instance=PowerEdge(i, n1, n2))
    edge_list = list(g.edges)

all_edges = list(g.edges.data(data=True))

dbg = True

for e in all_edges:
    powE = e[2]['instance']
    powE.flow = 0.22

all_edges = list(g.edges.data(data=True))
all_power_edges = [e[2]['instance'] for e in all_edges]

nx.draw(g)
plt.show()

for _, first_node in g.nodes(data=True):
    dbg = True
    in_adj, out_adj = g.in_edges(first_node), g.out_edges(first_node)
    dbg = True

'''
What am I trying to do here? I am trying to come up with a random network 
which has sources and sinks where I can compute flows. So that is next (in
my spare time).
'''
