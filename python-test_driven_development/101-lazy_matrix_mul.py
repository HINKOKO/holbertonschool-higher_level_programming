#!/usr/bin/python3
""" Matrix Multiplication - The LAzy Way !"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Using lazy Numpy"""
    new_matrix = np.matmul(m_a, m_b)
    return new_matrix
