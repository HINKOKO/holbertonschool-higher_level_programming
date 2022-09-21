# **Python :snake: - Test-driven development**

## **Learning Objectives**

- **What’s an interactive test**
	**Method 1**: It's a test ran within the interactive mode of Python, so far I have used the method `unittest`
	Let's say you have a file `circles.py` which is supposed to computes the area of a circle according to a given radius in input, then you have to create a `test_circles.py`, kind of test modules, in which you must include:
	```
	import unittest
	from circles import circles_area 
	#from your module name import the function name
	from matrix import pi
	#you need to import pi too to run the tests
	```

	Then you just have to enter in interactive mode by typing
	```
	python3 -m unittest test_circles
	```
	the `-m` tells Python to run test_circles module as a `script`.

	**Method 2:** Is about using `doctest` python facility. The `doctest` searches for pieces of text that <u> look like interactive Python sessions </u>, we could see this as "executable documentation" or "literate testing" or "test inside text".
	Here again, pass `-m` for executing as a `script` and `-v` for a detailed log of what's been going on under the hood.
	Note that we could have nested our "text test" inside our *.py* files, then `doctest` would have down his job, at the condition you include this at this end of your module:
	```
	if __name__== "__main__"
		import doctest
		doctest.testmod()
	```
	but here, for a good understanding and clarity, we separate our **text tests** in **text files** inside folder **/tests.**



- **Why tests are important:**
	To quote **Shakespeare:** "Trust, but verify, with unit testing"
	**Tests** are <u>***very important***</u> because we can not just type code and walk away and assume **everything will be allright.**<br>
	By writing *unit tests* we can test and check the software we are working on, to assure that all cases will be covered, with appropriate errors when necessary.
- **How to write Docstrings to create tests:**
	Proper way is demonstrated inside the folder /tests on this repository
- **How to write documentation for each module and function:**
	Same answer as above
- **What are the basic option flags to create tests:**

- **How to find edge cases:**
