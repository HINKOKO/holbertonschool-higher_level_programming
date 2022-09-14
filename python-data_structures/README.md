# **Python - Data Structures, Lists, Tuples**

## **General**

- *What are lists and how to use them* <br>
	Python most versatile *compound data types* is **the list**, which can be written as a list of comma-separated values (items) between square brackets. Lists might contain items of different types, but usually the items all have the same type.
	### **Like strings** <br>
	- **List can be indexed an sliced:** <br>
		```sea_monster = ['shark', 'cuttlefish', 'squid', 'mantis shrimp', 'anemone']``` <br>

	We can access the list at "index" , start a 0 with 'shark' but it could be a *negative* index <br>
	like sea_monster[-3] = 'squid' (starts at -1)

	**Slicing list:** we can create a slice with this techie [x:y]
	warning:  x is an inclusive index, y an exclusive index. you can also use negative index !
	**Stride** when you use this form [x:y:z] the 'z' , the stride, refers to how many items you want to move 
	forward. you can also use only the stride paramater [::2]
	**Modifying Lists with Operators:**
	the ```+``` operator is used to ```concatenate``` two or more lists together, or adding an item: <br>
	```sea_monster + ['yeti']```
	**Removing from a list:**
	Use the ```del``` statement with the index position, for example: ```del sea_monster[-3]```
	**Nested Lists:**
	sea_monster could be ```[['shi', 'sho'],['ba', 'bi']] ``` then you would need to specify multiples indices
	sea_monster[1][1] will be "bi"
	### **Unlike strings:** <br>
		lists are a *mutable type* possible to change their content. strings are *immutable*

- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- *What are tuples and how to use them:*
	Tuples are used to store multiple items in a single variable, tuples are one of 4 built-in data types in Python. they are used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. You write tuple with round brackets!
	==> A tuple is a collection which is ordered and **unchangeable.**

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
- What is tuple packing
- What is sequence unpacking
- What is the del statement and how to use it
