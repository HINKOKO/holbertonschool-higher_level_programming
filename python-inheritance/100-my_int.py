#!/usr/bin/python3
"""Module 100 - My Rebel Integer"""


class MyInt(int):
    """Rebel class that inverts == and !="""

    def __eq__(self, other):
		"""equality becomes inequality"""
        return super().__ne__(other)

    def __ne__(self, other):
		"""inequality becomes equality"""
        return super().__eq__(other)
