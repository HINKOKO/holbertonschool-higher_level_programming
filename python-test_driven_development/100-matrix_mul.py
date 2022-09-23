#!/usr/bin/python3
""" Matrix multiplication crazy stuff !!!"""


def matrix_mul(m_a, m_b):
	"""m_a and m_b must be list of lists
	of integers or floats
	Requirements checked in order"""
	if type(m_a) or type(m_b) is not list:
		raise TypeError("{} must be a list".format("m_a")
						if not isinstance(m_a, list) else "m_b")

	for rows in m_a:
		for i in rows:
			if not isinstance(i, (float, int)):
				raise TypeError("m_a must be a list of lists")
			if len(rows) != len(m_a[0]):
				raise TypeError("each row of m_a must be of the same size")
	for rows in m_b:
		for j in rows:
			if not isinstance(j, (float, int)):
				raise TypeError("m_b must be a list of lists")
			if len(rows) != len(m_b[0]):
				raise TypeError("each row of m_b must be of same size")
			if len(rows) != len(m_a):
				raise ValueError("m_a and m_b can't be mutiplied")

	if m_a == [] or m_a == [[]] or m_b == [] or m_b == [[]]:
		raise ValueError("{} can't be empty".format(
			"m_a" if m_a == [] else "m_b"))

