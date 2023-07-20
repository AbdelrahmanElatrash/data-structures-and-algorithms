class Node:
    
    def __init__(self,value):
        self.value=value
        
    def __str__(self) :
        return self.value
        
class Edge:
    
    def __init__(self,vertex,weight=0) -> None:
        self.vertex=vertex
        self.weight=weight
        

class Graph:
    
    def __init__(self) -> None:
        self.adj_list={}
        
    
    def add_vertex(self,value):
        """
        Add a vertex to the graph
        Arguments: value <any>
        Returns: The added vertex
        """
        vertix=Node(value)
        if vertix in self.adj_list :
            return vertix
        
        self.adj_list[vertix]=[]   #      vertix is a key  his value is list containe edges
        
        return vertix
    
    
    def add_edge(self,vertex1,vertex2,weight=0):
        """
        Adds a new edge between two vertices in the graph
        Arguments: 2 vertices to be connected by the edge
        """
        if vertex1 not in self.adj_list or vertex2 not in self.adj_list :
            return "one or both vertices not in graph object"
        
        edge1=Edge(vertex2,weight)
        edge2=Edge(vertex1,weight)
        
        self.adj_list[vertex1].append(edge1)
        self.adj_list[vertex2].append(edge2)
        
        
    def get_vertices(self):
        """
        Arguments: none
        Returns all of the vertices in the graph as a collection (set, list, or similar)
        """
        vertices=[]
        if len(self.adj_list) ==0 :
            return vertices
        
        for vertex in self.adj_list:
            vertices.append(vertex.__str__())
        
        return vertices
    
    
    def get_neighbors(self ,vertex):
        """
        Arguments: vertex 
        Returns a collection of edges connected to the given vertex
                Include the weight of the connection in the returned collection
        """
        edges=[]
        
        if vertex not in self.adj_list :
            return edges
        
        for edge in self.adj_list[vertex] :  # so its a list 
            edges.append((edge.vertex.value, edge.weight))
            
        return edges
    
    
    def size(self):
        """
        Arguments: none
        Returns the total number of vertices in the graph
        """

        return len(self.adj_list)
    
    
    def breadth_first(self,node):
        """
        Arguments: Node
        Return: A collection of nodes in the order they were visited.
        """
        visited=[]
        queue=[]
        
        visited.append(node.value)
        queue.append(node)
        
        while queue :
            vertex=queue.pop(0)
            
            for edge in self.adj_list[vertex]:
                
                if edge.vertex.value not in visited:
                    visited.append(edge.vertex.value)
                    queue.append(edge.vertex)
                    
            
        return visited       
            
        
    
    
    
# if __name__=="__main__":
    
#     graph=Graph()
    
#     a=graph.add_vertex(0)
#     b=graph.add_vertex(1)
#     c=graph.add_vertex(2)
#     d=graph.add_vertex(3)
    
    
#     graph.add_edge(a,b)
#     graph.add_edge(a,c)
#     graph.add_edge(b,c)
#     graph.add_edge(c,d)
#     graph.add_edge(d,b)
#     graph.add_edge(d,c)
    
    
#     # print(graph)
#     print(graph.breadth_first(a))
    
#     # c=graph.get_neighbors(a)
#     # print(graph.size())
#     # for i in c:
#     #     print(i)
       
    