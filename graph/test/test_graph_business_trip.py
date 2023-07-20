import pytest
from graph.graph_business_trip import get_weight , business_trip 
from graph.graph import Graph

graph=Graph()

Metroville,Pandora,Arendelle,New_Monstropolis,Naboo,Narnia=[graph.add_vertex('Metroville'), 
                                                            graph.add_vertex('Pandora'),
                                                            graph.add_vertex('Arendelle'),
                                                            graph.add_vertex('New Monstropolis'),
                                                            graph.add_vertex('Naboo'),
                                                            graph.add_vertex('Narnia')]

 

    
graph.add_edge(Pandora,Arendelle,150)
graph.add_edge(Pandora,Metroville,82)
graph.add_edge(Arendelle,Metroville,99)
graph.add_edge(Arendelle,New_Monstropolis,42)
graph.add_edge(Metroville,New_Monstropolis,105)
graph.add_edge(Metroville,Narnia,37)
graph.add_edge(Metroville,Naboo,26)
graph.add_edge(New_Monstropolis,Naboo,73)
graph.add_edge(Naboo,Narnia,250)




def test_get_weight():
    assert get_weight(Metroville,Arendelle,graph=graph)==99
    assert get_weight(Narnia,Arendelle,graph=graph)==None


def test_business_trip():
    assert business_trip([Metroville, Pandora],graph=graph)=='82$' 
    assert business_trip([Arendelle, New_Monstropolis, Naboo],graph=graph)== '115$'
    assert business_trip([Naboo, Pandora],graph=graph)== 'null'







