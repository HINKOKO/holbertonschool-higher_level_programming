# **Python - More Data Structures: Set, Dictionary** 

## General Learning Objectives: <br>

- ### What are sets and how to use them: <br>
	A set is an unordered collection with no duplicate elements. Basic uses include membership testing and eliminating duplicate entries. Set objects also support mathematical operations like union, intersection, difference, and symmetric difference. <br>
	Curly braces or the ```set()``` function can be used to create sets. *Note!* to create an empty set you have to use ```set()```, not ```{}```; the latter creates an empty [```dictionary```](#dictionaries)
	
- ### What are the most common methods of set and how to use them <br>
	With set method, you can achieve pretty cool stuff !
	```
	basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
	print(basket)                      # show that duplicates have been removed
	{'orange', 'banana', 'pear', 'apple'}
	 'orange' in basket                 # fast membership testing
	True
	 'crabgrass' in basket
		False

	 Demonstrate set operations on unique letters from two words
	...
 	a = set('abracadabra')
 	b = set('alacazam')
 	a                                  # unique letters in a
	{'a', 'r', 'b', 'c', 'd'}
	a - b                              # letters in a but not in b
	{'r', 'd', 'b'}
	 a | b                              # letters in a or b or both
	{'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
	 a & b                              # letters in both a and b
	{'a', 'c'}
	 a ^ b                              # letters in a or b but not both
	{'r', 'd', 'b', 'm', 'z', 'l'}
	```
	Sets also supports `set comprehension` like lists.
	```
	>>> a = {x for x in 'shogoli' if x not in 'ogi'}
	>>> a
	{'s', 'h', 'l'}
	```
	
- ### When to use sets versus lists
	When you are intending to determine if an 'object' is present, `sets` are better than list (perfect exemple membership storage). But `sets` are not indexed like `lists`.
- ### How to iterate into a set
- ### What are dictionaries and how to use them
- ### When to use dictionaries versus lists or sets
- ### What is a key in a dictionary
- ### How to iterate over a dictionary
- ### What is a lambda function
- ### What are the map, reduce and filter functions
