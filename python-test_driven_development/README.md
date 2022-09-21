# **Python :snake: - Test-driven development**

## **Learning Objectives**

- **What’s an interactive test**
	It's a test ran within the interactive mode of Python, so far I have used the method `unittest`
	Let's say you have a file `circles.py` which is supposed to computes the area of a circle according to a given radius in input, then you have to create a `test_circles.py`, kind of test modules, in which you must include:
	```
	import unittest
	from circles import circles_area 
	#from your module name import the function name
	from matrixh import pi
	#you need to import pi too to run the tests
	```

	Then you just have to enter in interactive mode by typing
	```
	python3 -m unittest test_circles
	```
	the `-m` tells Python to run test_circles module as a `script`.

- **Why tests are important:**
	To quote **Shakespeare:** "Trust, but verify, with unit testing"
	**Tests** are <u>***very important***</u> because we can not just type code and walk away and assume **everything will be allright.**<br>
	By writing *unit tests* we can test and check the software we are working on, to assure that all cases will be covered, with appropriate errors when necessary.
- **How to write Docstrings to create tests:**
- How to write documentation for each module and function
- What are the basic option flags to create tests
- How to find edge cases
