"""
Gale-Shapley Algorithm Package

This package contains implementations of the Gale-Shapley algorithm
for stable matching problems, particularly focused on the hospital-resident
matching problem.
"""

from .gale_shapley import gale_shapley, read_input_file

__all__ = ['gale_shapley', 'read_input_file'] 