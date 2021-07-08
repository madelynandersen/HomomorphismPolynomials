"""
Author: Madelyn Andersen

Core file for polynomials.
"""

import helpers
import graphs

import sys
import itertools
from tqdm import tqdm
import multiprocess as mp
from functools import partial
import copy

import numpy as np
#from numpy.polynomial import Polynomial as Poly

POOL = mp.Pool(mp.cpu_count())

class Monomial:
    """ Represent a monomial as a class.

    Used by Polynomial class to build up larger terms.
    """

    def __init__(self, num_var=1, powers=None):
        self.num_var = num_var
        if powers:
            self._powers = powers
        
    def set_powers(self, powers):
        self._powers = powers
    
    def get_powers(self):
        return self._powers
    
    def _tex(self):
        """ Returns a tex-friendly formatting of the monomial."""
        result = ""
        for i in range(self.num_var):
            if self._powers[i] != 0:
                result += "x_{i}^{j}".format(i=i, j="{%d}" % self._powers[i])
        return result

    def __str__(self):
        return helpers.tex(self._tex())

class Polynomial:
    """ Represent a polynomial as a class."""

    def __init__(self, num_var, coef=None, powers=None):
        self.num_var = num_var
        self._monomials = []
        self._coef = []
        self._powers = []
        if coef:
            self._coef = coef
        if powers:
            self._powers = powers
            self.set_monomials()

    # Get and set attributes
    def _clear(self):
        self._coef = []
        self._powers = []
        self._monomials = []

    def _clear_monomials(self):
        self._monomials = []
        
    def set_powers(self, powers):
        self._powers = powers
        self.set_monomials()
    
    def get_powers(self):
        return self._powers

    def get_power(self, ind):
        return self._powers[ind]
    
    def set_coef(self, coef):
        self._coef = coef
    
    def get_coefs(self):
        return self._coef
    
    def get_coef(self, ind):
        return self._coef[ind]

    def set_monomials(self):
        self._clear_monomials()
        for i in tqdm(range(len(self._coef))):
            self._monomials += Monomial(self.num_var, self._powers[i])

    # Add monomials to polynomial

    def add_monomials(self, coef, powers):
        """ Add a list of monomials to polynomial"""
        for i in range(len(powers)):
            self.add_monomial(coef[i], Monomial(self.num_var, powers[i]))

        return self

        
    def add_monomial(self, coef, mono):
        """ Add a single monomial to polynomial"""
        if mono.get_powers() in self._powers:
            # If already in polynomial, add coeficients together.
            # Remove monomial if new coeficient is equal to 0.
            ind = self._powers.index(mono.get_powers())
            if self._coef[ind] + coef == 0:
                self._coef.pop(ind)
                self._powers.pop(ind)
                self._monomials.pop(ind)
            else:
                self._coef[self._powers.index(mono.get_powers())] += coef
        
        else:
            # If not already in polynomial, simply add to end of attr lists.
            self._coef += [coef]
            self._powers += [mono.get_powers()]
            self._monomials += [mono]
        
        # Return self for repeated function use.
        return self

    def add_monomial_from_edge_list(self, num_vertices, edges, coef=1):
        # for each mapping from num_vertices to [num_var], 
        # create a monomial from the edges
        mappings = itertools.product(range(self.num_var), repeat=num_vertices)
        to_pool = partial(helpers.map_edges, self.num_var, edges)
        powers_result = tqdm(
            POOL.imap(to_pool, mappings),
            total = self.num_var ** num_vertices,
            position=0)
        
        # Add a monomial for each resulting monomial from all of the mappings
        for p in tqdm(
            powers_result,
            total = self.num_var ** num_vertices,
            position=0):
            self.add_monomial(coef, Monomial(len(p), p))
        
        return self

    
    def add_monomial_from_graph_string(self, string, coef=1):
        self.add_monomial_from_edge_list(
            *graphs.create_graph_edges(string),
            coef=coef
        )

    # Polynomial manipulation techniques using methods

    def __copy__(self):
        return Polynomial(self.num_var, self._coef, self._powers)

    def __add__(self, other):
        return self.copy().add_monomials(other.get_coef(), other.get_powers())
    
    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

    def __sub__(self, other):
        return self.copy().add_monomials(
            np.array(other.get_coef()) * -1,
            other.get_powers())

    
    # Format output
    def _tex(self):
        result = ""
        for i in range(len(self._coef)):
            if self._coef[i] != 1:
                result += "({a})".format(a=self._coef[i])
            result += self._monomials[i]._tex()
            if i < len(self._coef) - 1:
                result += ' + '
        return result

    def __str__(self):
        return helpers.tex(self._tex())


if __name__ == "__main__":
    # Tests:
    p = Polynomial(2)
    p.add_monomial(4, Monomial(2, [2, 3]))
    print(p)
    p.add_monomial(-1, Monomial(2, [1, 3]))
    print(p)

    POOL.close()


    # Run the code with input at terminal level
