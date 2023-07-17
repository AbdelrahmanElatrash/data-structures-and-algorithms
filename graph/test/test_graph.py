import pytest
from graph.graph import Node , Edge , Graph


graph_obj=Graph()
a=graph_obj.add_vertex('v1')
b=graph_obj.add_vertex('v2')

def test_add_vertex():
    c=graph_obj.add_vertex('key1')
    assert c.value == 'key1'
    
    
    
def test_add_edge():
    
    assert graph_obj.add_edge('key1','key2')== 'one or both vertices not in graph object' 
    
    assert graph_obj.add_edge(a,b)==None
    
    
def test_get_vertices():
    assert graph_obj.get_vertices()==['v1', 'v2', 'key1']
    
    
def test_get_neighbors():
    assert graph_obj.get_neighbors(a)== [('v2', 0)]
    
    
def test_size():
    assert graph_obj.size()==3
    


