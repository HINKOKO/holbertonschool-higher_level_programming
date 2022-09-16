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
	A dictionary is another example of data structure in Python. Like a list, it is one of the most commonly used data structure in programming. A dictionary is used to `map` or `associate` things you want to store to keys you nedd to get them, so it consists of a collection of `key-value pairs`, each key-value pair maps the key to its associated value.
	**Dictionary map keys to values and store them in an array or collection**
	You can declare a dictionary like this
	```
	>>> stuff = {'Colorado': 'nice', 'name': 'baki', 'height' : 333}
	```
	A dictionary lets you use anything, not just numbers, yep, a dict `maps one thing to another` no matter what it is. But pay attention, dictionary elements are **not accessed by numerical index.**
	Still, if you don't get them by index, how do you get them ?
	**A value is retrieved** in a dictionary by specifying its corresponding key in squarre brackets:
	```
	>>> stuff(['Colorado'])
	'nice'
	```
	**Adding an entry**
	```
	>>> stuff['chicken'] = 'delicious'
	```
	**Updating an entry** just assign a new value to an existing key:
	```
	>>> stuff['name'] = 'Bane'
	```
	**To delete an entry** simply use the `del` statement, specifying the key to delete:
	```
	del stuff['Colorado']
	```
	### Note on numbers as keys:
	If you try to access a dictionary entry with an undefined key or a number, Python interpreter raises a `KeyError`
	```
	>>> stuff['youhou']
	Traceback (most recent call last):
  	File "<pyTonyshell#2>", line 1, in <module>
		stuff['youhou']
	KeyError: 'youhou'
	```
	```
	>>> stuff[1]
	Traceback (most recent call last):
  	File "<pyTonyshell#2>", line 1, in <module>
		stuff['1']
	KeyError: 1
	```
	That's the same error, [1] looks like a numerical index but `it is not`
	In fact, any `immutable type` (almost correct - see section on [keys](#what-is-a-key-in-a-dictionary)) can be used as a key, accordingly, there is no reason you can't use integers as keys
	```
	>>> stuff = {0: 'zero', 1: 'the best'}
	```
	so if you access stuff[1] it might appear as an index or indice, **but it is not!**
	Python interprets them as **keys** , they have nothing to do with the order of items in dictionary.

- ### When to use dictionaries versus lists or sets
	*Dictionaries and lists share the following characteristics:*

	Both are: - mutable. <br>
			  - dynamic. They can grow and shrink as needed.<br>
			  - can be nested. A list can contain another list. A dictionary can contain another dictionary. A dictionary can also contain a list, and vice versa.
			  
	*Dictionaries differ from lists primarily in how elements are accessed:*

	List elements are accessed by their position in the list, via indexing.
	Dictionary elements are accessed via keys.
	Difference with list: list is for an ordered list of items. A Dictionary (dict) is for `matching` some items, called `keys` to other items, called `values`.
- ### What is a key in a dictionary
	Keys must be of `hashable type`, which means it can be passed to a hash function, so their hash value won't change during their key's lifetime.
- ### How to iterate over a dictionary

- ### What is a lambda function
	A `lambda function` is a way of creating a little *function inline*, without all the syntax of a *def*.<br>
	Here's a little lambda with a single parameter:
	```
	>>> lambda n: n ** 2
	```
	The code of lambda is typically a single expression without `variables` or `if statements`, and does not `"return"`. **Lambda** is perfect where you have a short computation to write inline. Many programs have some *sub-parts* which can be solved compactly with **Lambda**, for longer code, **def** is better.
	The real power of lambda is seen with the use of **map()**, section right below buddies.

- ### What are the map, reduce and filter functions
 - #### **map():**
   **map()** function executes a specified *function* for each *item* in a iterable. The item is sent to the function as a parameter.
   Syntax:
   ```
   >>> map(function, iterables)
   ```
   *function:* Required, the function to execute on each item.
   *iterables:* Required, a sequence, a collection of item or an iterator object. You can send as many iterables as a you like, but make sure the function has one parameter for each iterables.
   Sample example with **lambda** (here our function-parameter is a little lambda function):
   ```
   >>> nums = [1, 2, 4, 10]
   >>> map(lambda n: 2 * n, nums)
   >>> #print fails! on Python 3 and above, map() returns an iterator, so you have to specify `list`
   >>> <map object at 0x10ce156f5>
   >>> list(map(lambda n: 2 *n, nums))
   >>> [2, 4, 8, 20]
   ``` 
