"""
Author: Madelyn Andersen
Functions for graph input and computation to help core
"""
import itertools

def create_graph_edges(string):
    """Accepts string inputs of the following types:
    Kn, Pn, Cn, Sn, On, KNbM, KLOOPn, Bn
    
    
    SIMPLE graphs
    Kn: complete graph with vertices 0 to n-1
    Pn: path graph with vertices 0 to n-1, edges between i and i+1
    Cn: cycle graph with vertices 0 to n-1, path graph with edge from n-1 to 0
    Sn: star graph with vertices 0 to n-1, edges between 0 and i
    On: graph with no edges on vertices 0 to n-1
    
    KNbM: complete bipartite graph with vertices 0 to n-1
    KLOOPn: complee graph with vertices 0 to n-1 and loops on every node
    Bm: m-bond B^m is vertices 0 and 1 connected by m edges
    """
    graph_type = string.translate({ord(k): None for k in '0123456789'}).upper()
    
    if graph_type == "KB":
        num_vertices_1 = int(string[1:string.upper().find("B")])
        num_vertices_2 = int(string[string.upper().find("B") + 1:])
        edge_list = list(
            itertools.product(
                range(num_vertices_1),
                range(num_vertices_1, num_vertices_1 + num_vertices_2)))
        return edge_list
    
    num_vertices = int(string[len(graph_type):])
    
    if graph_type == "K":
        if num_vertices == 0: edge_list = []
        else:
            edge_list = list(itertools.combinations(range(num_vertices), 2))
    
    elif graph_type == "P":
        edge_list = list(zip(range(num_vertices)[:-1], range(num_vertices)[1:]))
    
    elif graph_type == "C":
        if num_vertices == 1: edge_list = [(0, 0)]
        elif num_vertices == 2: edge_list = [(0, 1), (0, 1)]
        else:
            range_ = list(range(num_vertices))
            edge_list = list(zip(range_[:-1] + [range_[0]], range_[1:] + [range_[-1]]))
        
    elif graph_type == "S":
        edge_list = list(zip([0] * (num_vertices - 1), range(1, num_vertices)))
        
    elif graph_type == "O": edge_list = []
        
        
    """
    MULTI graphs
    
    Kloopn: complete graph with vertices 0 to n-1 and loops on every node
    Bm: m-bond B^m is vertices 0 and 1 connected by m edges
    
    """
    if graph_type == "KLOOP":
        if num_vertices == 0: edge_list = []
        else:
            # cartesian product remove the duplicates
            edge_list = sorted(set([
                tuple(sorted(e)) for e in list(itertools.product(range(num_vertices), range(num_vertices)))]))
    elif graph_type == "B":
        edge_list = [(0, 1)] * num_vertices
        
    
    return num_vertices, edge_list


def make_multi_simple(edge_list):
    """
    Takes the edge list of a graph and returns the simple graph obtained by removing loops and multiple edges
    """
    new_edges = sorted(set([tuple(sorted(e)) for e in edge_list])) # slow remove duplicates
    new_edges = list(filter(lambda e: e[0] != e[1], new_edges)) # remove loops
    return new_edges