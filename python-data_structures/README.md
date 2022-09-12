# **Python - Data Structures, Lists, Tuples**

## **General**

- What are lists and how to use them <br>
	String list / Index: <br>
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
	sea_monster[1][1] will be 'bi'

- What are the differences and similarities between strings and lists
- What are the most common methods of lists and how to use them
- How to use lists as stacks and queues
- What are list comprehensions and how to use them
- What are tuples and how to use them
- When to use tuples versus lists
-What is a sequence
- What is tuple packing
- What is sequence unpacking
- What is the del statement and how to use it
