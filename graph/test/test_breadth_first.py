import pytest
from graph.graph import Node , Edge , Graph



graph=Graph()
    
a=graph.add_vertex(0)
b=graph.add_vertex(1)
c=graph.add_vertex(2)
d=graph.add_vertex(3)
    
    
graph.add_edge(a,b)
graph.add_edge(a,c)
graph.add_edge(b,c)
graph.add_edge(c,d)
graph.add_edge(d,b)
graph.add_edge(d,c)


def test_breadth_first():
    assert graph.breadth_first(a)==[0, 1, 2, 3]