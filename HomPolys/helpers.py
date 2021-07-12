"""
Author: Madelyn Andersen
Helper functions for formatting and computation in core
"""
import numpy as np

import sys

if 'ipykernel' in sys.modules:
    from IPython.display import Latex

def in_notebook():
    return 'ipykernel' in sys.modules

def tex(string):
    """Adds equation-signs around tex string"""
    if 'ipykernel' in sys.modules:
        return Latex("$" + string + "$")
    else:
        return string

def map_edges(num_var, edges, mapping):
    """ Apply a mapping from V(G) -> [q] to the edges E(G).

    Return the resulting powers for the monomial.
    """
    powers = np.zeros((1, num_var ** 2)).tolist()[0]
    for edge in edges:
        mapped_to = sorted([mapping[edge[0]], mapping[edge[1]]])
        powers[mapped_to[0] * num_var + mapped_to[1]] += 1
    return powers

