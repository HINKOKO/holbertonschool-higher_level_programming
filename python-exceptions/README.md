# **Python - Exceptions**

## **Learning Objectives:**

- **What’s the difference between errors and exceptions:**
	Before going any further, we have to understand the subtle difference between an `error` and an `exception`.
	**Errors cannot be handled**, while Python's `exceptions`can be **handled at the runtime.**
	Everybody has already seen a `syntax error`, it's the most common kind of complaint of our computer:
	```
	>>> if x > 0
		print(x)
	>>> File "<stdin>", line 1
    	if x > 0
           		^
		SyntaxError: invalid syntax
	```
	A colon is missing after the statement `if` so the parser displays a little arrow where the error was detected.
	We've all been through this.
	Now, about `exceptions`, even if your syntax is perfect, you may have an error, detected in the `execution`of code, **errors detected during `execution` are called `exceptions`**, but rejoice ! they are not *fatal*, and we're going to learn how to handle them in our Python programs.
	However, this is what an error message due to exception looks like:
	```
	>>> 10 / 0
	Traceback (most recent call last):
  		File "<stdin>", line 1, in <module>
	ZeroDivisionError: division by zero
	```
	The last line shows what happened, `exceptions` comes in different types, e.g. you may have 
	**ZeroDivisionError, NameError and TypeError.**
- What are exceptions and how to use them
- When do we need to use exceptions
- How to correctly handle an exception
- What’s the purpose of catching exceptions
- How to raise a builtin exception
- When do we need to implement a clean-up action after an exception

