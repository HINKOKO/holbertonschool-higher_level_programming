#!/usr/bin/python3
""" Matrix multiplication crazy stuff !!!"""


def matrix_mul(m_a, m_b):
    """m_a and m_b must be list of lists
    of integers or floats
    Requirements checked in order"""
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")

    for row_a in m_a:
        if type(row_a) is not list:
            raise TypeError("m_a must be a list of lists")
        for i in row_a:
            if not isinstance(i, (float, int)):
                raise TypeError("m_a should contain only integers or floats")
            if len(row_a) != len(m_a[0]):
                raise TypeError("each row of m_a must be of the same size")
    for row_b in m_b:
        if type(row_b) is not list:
            raise TypeError("m_b must be a list of lists")
        for j in row_b:
            if not isinstance(j, (float, int)):
                raise TypeError("m_b should contain only integers or floats")
            if len(row_b) != len(m_b[0]):
                raise TypeError("each row of m_b must be of same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be mutiplied")

    if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
        raise ValueError("{} can't be empty".format(
            "m_a" if m_a == [] else "m_b"))

    new_matrix = []
    for i in range(len(m_a)):
        new_rows = []
        for j in range(len(m_b[0])):
            res = 0
            for k in range(len(m_a[0])):
                res += m_a[i][k] * m_b[k][j]
            new_rows.append(res)
        new_matrix.append(new_rows)
    return new_matrix
