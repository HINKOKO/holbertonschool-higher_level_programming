# **Python :snake: Almost a circle**

## **Learning Objectives**

- **What is Unit testing and how to implement it in a large project:**
	A unit test is a test that checks a single component of code, usually modularized as a function, and ensures that it performs as expected. <br>
	Unit tests are an important part of regression testing to ensure that the code **still functions as expected after making changes** to the code and helps ensure **code stability.** After making changes to our code, we can run the unit tests we have created previously to ensure that the existing functionality in other parts of the codebase *has not been impacted by our changes.*

	Another key benefit of unit tests is that they help easily isolate errors. Imagine running the entire project and receiving a string of errors. How would we go about debugging our code?
- How to serialize and deserialize a Class
- How to write and read a JSON file
- **What is *args and how to use it:**
	It's easy to write a function for adding two numbers. But what if you need to add three, four, five or an *I don't know how many numbers* I will have to add.
	Here comes the ***args**. When we have a variable numbers of arguments, we shouldn't modify our functions everytime. Instead, you can use `*args` (and `**kwargs`) as arguments when you are not sure, when you don't know about the number of arguments that will be passed to your function. (It's like the `argc` and `**argv` we saw in C :brain:)

	So ! ***args** allows us to pass a **variable number of non-keyword arguments to a Python function.** We have to use the `*` **asterisx** before parameter name to declare as a "variable number"
	Be aware that `args` is not a **magic word**, Only the `*`**asterisk** is magic, you could write ***gorilla** and it would work also, this is a **convention** to use args and kwargs.

	How to use with an example: (just don't ommit the asterisk in the function and let's go !)
	```
	def add(*args):
		sum = 0
		for num in args:
			sum += num
		return sum

	print(add(1, 2, 3, 4, 5))

	# Output
	15
	```
- What is **kwargs and how to use it
- How to handle named arguments in a function
