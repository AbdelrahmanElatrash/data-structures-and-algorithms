try:
    from graph import Graph 
except :
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


def loop(v):
    for e in v:
        e.vertex , e.weight
        
for k in graph.adj_list:
    
    print(k.value, graph.get_neighbors(k) ) 
    
 
def get_weight(v1,v2,graph=graph):
    """
    check if there is a path between 2 vetrices
    args: v1,v2 <vertices>
    return the bath weight between v1 and v2 <int>
    """
    if v1 in graph.adj_list and v2 in graph.adj_list:
        for edge in graph.get_neighbors(v1) :
            if v2.value == edge[0] :
                return edge[1]
    else :
        return None
    
def business_trip(trip,graph=graph):
    """
    Arguments: trip, list of city names
    Return: str the cost of the trip (if it’s possible) or null (if not)
    """
    
    total_cost=0
    for i in range(0,len(trip)-1):
        v1=trip[i]
        v2=trip[i+1]
        try:
            total_cost +=get_weight(v1,v2,graph=graph)
        except :
            return 'null'
        
    return str(total_cost)+'$'

# print(business_trip([Naboo, Pandora])) 
# print(get_weight(Metroville,Arendelle))   
    