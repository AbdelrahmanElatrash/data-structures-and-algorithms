import pytest
from graph.graph import Node , Edge , Graph


graph=Graph()
    
a=graph.add_vertex('A')
b=graph.add_vertex('B')
c=graph.add_vertex('C')
d=graph.add_vertex('D')
e=graph.add_vertex('E')
f=graph.add_vertex('F')
g=graph.add_vertex('G')
h=graph.add_vertex('H')
    
    
graph.add_edge(a,d)
graph.add_edge(a,b)

graph.add_edge(b,d)
graph.add_edge(b,c)
    
graph.add_edge(c,g)
    
graph.add_edge(d,f)
graph.add_edge(d,h)
graph.add_edge(d,e)
    
graph.add_edge(f,h)


def test_depth_first():
    assert graph.depth_first(a)==['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']