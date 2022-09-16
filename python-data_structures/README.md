# **Python :snake: - Data Structures, Lists, Tuples**

## **General**

- **What are lists and how to use them:**
	Python most versatile *compound data types* is **the list**, which can be written as a list of comma-separated values (items) between `square brackets`. Lists might contain items of different types, but usually the items all have the same type.
	- **List can be indexed an sliced:** <br>
		```sea_monster = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']``` <br>

	We can access the list at "index" , start a 0 with 'shark' but it could be a *negative* index <br>
	like sea_monster[-3] = 'squid' (starts at -1)

	- **Slicing list:** we can create a slice with this techie [x:y]
	warning:  x is an inclusive index, y an exclusive index. you can also use negative index !
	- **Stride** when you use this form [x:y:z] the 'z' , the stride, refers to how many items you want to move 
	forward. you can also use only the stride paramater [::2]
	- **Modifying Lists with Operators:**
	the ```+``` operator is used to ```concatenate``` two or more lists together, or adding an item: <br>
	```sea_monster + ['yeti']```
	- **Removing from a list:**
	Use the ```del``` statement with the index position, for example: ```del sea_monster[-3]```
	- **Nested Lists:**
	sea_monster could be ```[['shi', 'sho'],['ba', 'bi']] ``` then you would need to specify multiples indices
	sea_monster[1][1] will be "bi"

- **What are the differences between strings and lists:**
	We cannot easily make a list into a string, but we can make a string into a list simply using `list()` function.
	`Strings` can only consists of `characters`, while `lists`can contain any data type.
	When we add two `strings`, we use the `+` concatenation operator, but with a list, we use the `.append` method.
	Finally **Unlike strings,** lists are a *mutable type* ==> possible to change their content. strings are of *immutable type.* 

- **What are the most common methods of lists and how to use them:**

- **How to use lists as stacks and queues:**
	### Stacky way:
	The list methods previously shown make it very easy to use list as a `stack`, where the last element added is the first element retrieved.(LIFO). To add an item on top of `stack`, use `append()`, to retrieve an element from the top, use `pop()`. No explicit index needed.
	### Queue way:
	In queue, first element added is the first element retrieved (FIFO). *However* lists are <u>not efficient for that purpose </u>, because all elements have to be shifted by one when you want to insert or pop from the beginning of a list ==> slow, be aware of that.
	Anyway, it is possible, to implement it use `collections.deque`, it was designed to perform fast appends and pops from both ends.
	```
	>>> from collections import deque
	>>> queue = deque(["Eric", "John", "Michael"])
	>>> queue.append("Terry")           # Terry arrives
	>>> queue.append("Graham")          # Graham arrives
	>>> queue.popleft()                 # The first to arrive now leaves
		'Eric'
	>>> queue.popleft()                 # The second to arrive now leaves
		'John'
	>>> queue                           # Remaining queue in order of arrival
		deque(['Michael', 'Terry', 'Graham'])
- **What are list comprehensions and how to use them:**
	`List comprehension` offers a shorter syntax when you want to create a new list based on the value of an existing list. Let's take a basic example, given a list of car brand names, you want a new list, based on only the car-brands which contains a 'm':
	```
	>>> cars = ['Mercedes', 'Bmw', 'Maserati', 'Porsche', 'Bentley', 'Honda', 'Subaru']
	>>> newcars = [x for x in cars if "m" or "M" in x]
	>>> print(newcars)
	>>> ['Mercedes', 'Bmw', 'Maserati']
	```
	pretty neat uh? without list comprehension, you would need to write a `for`statement with conditional test inside.
- **What are tuples and how to use them:**
	Tuples are used to store multiple items in a single variable, tuples are one of 4 built-in data types in Python. they are used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. You write tuple with round brackets!
	==> A tuple is a collection which is `ordered` and **unchangeable.**

- *When to use tuples versus lists*
	- Key difference between tuples and lists: on the one hand the tuples are immutable objects , on the other hand the lists are mutable. This means that tuples cannot be changed while the lists can be modified.
	- Tuples are more memory efficient than the lists.
	When it comes to the time efficiency, again tuples have a slight advantage over the lists especially when lookup to a value is considered.
	- If you have data which is not meant to be changed in the first place, you should choose tuple data type over lists.
- *What is a sequence*
	A sequence is a positionally ordered collection of items. And you can refer to any item in the sequence by using its index number e.g., s[0] and s[1].
	In Python, the sequence index starts at 0, not 1. So the first element is s[0] and the second element is s[1]. If the sequence s has n items, the last item is s[n-1].
	Python has the following built-in sequence types: **lists, bytearrays, strings, tuples, range, and bytes.** Python classifies sequence types as *mutable* and *immutable.*

	mutables : lists, bytearrays <br>
	immutables : strings, tuples, range, bytes <br>

	homogeneous : all elements of sequence are of the same type (strings)<br>
	heterogeneous : where you can store different types of element (lists) <br>
	==> <u>In general</u>, homogeneous are more efficient than heterogeneous in terms of storage and operations.
- **What is tuple packing:**
	When you create a tuple, you normally assing values to it, this is what we call *packing a tuple*:
	cars = ("Benz", "Toyota", "Dodge")

- What is sequence unpacking
- What is the del statement and how to use it
