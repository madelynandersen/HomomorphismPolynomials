"""
Author: Madelyn Andersen
Helper functions for formatting and computation in core
"""
import numpy as np

def tex(string):
    """Adds equation-signs around tex string"""
    return "$" + string + "$"

def map_edges(num_var, edges, mapping):
    """ Apply a mapping from V(G) -> [q] to the edges E(G).

    Return the resulting powers for the monomial.
    """
    powers = np.zeros((1, num_var ** 2)).tolist()[0]
    for edge in edges:
        mapped_to = sorted([mapping[edge[0]], mapping[edge[1]]])
        powers[mapped_to[0] * num_var + mapped_to[1]] += 1
    return powers

