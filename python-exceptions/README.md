# **Python - Exceptions**

## **Learning Objectives:**
- **Introduction:**
	Software applications don’t run perfectly all the time, you should have noticed that. :smile: Despite intensive debugging and multiple testing levels, applications still fail. Bad data, broken network connectivity, corrupted databases, memory pressures, and unexpected user inputs can all disturb an application to run normally. When such events occurs, disturbing the normal flow, this is known as **an exception.** And it's your application's job—and your job as a coder—to catch and handle these exceptions gracefully so that your app keeps working.

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
	==> string printed as the exception type is the name of `the built-in exception` that occured.
	[Built-in exceptions](https://docs.python.org/3/library/exceptions.html#bltin-exceptions) lists them and give their meaning.

- **What are exceptions and how to use them:**
	After what has been said, we can declare that an `exception` is an event, which occurs during the execution of a program that disrupts the normal flow of the program's instructions. In general, when a Python script encounters a situation that it cannot deal with, it raises an exception. **An exception is a Python object that represents an error.**
	
- **How to correctly handle an exception:**
	Files from `0-safe_print_list.py` to `4-list_division.py` are good examples of how to handle with exceptions.
	Here is the generic syntax for handling an exception:
	```
	try:
		Do your stuff here...
		........
	except Exception_1:
		If Exception_1 occurs, then execute this block
	except Exception_2:
		If Exception_2 occurs, then execute this block
	```
	**Notes**
	- First, the *try block* is executed
	- If no exception occurs, the *except block* is <u>skipped</u> and execution of *try* is finished
	- A single *try* may have multiples *except statements*, very useful when the *try block* may generates different kind of exceptions
	- After your *except block*, you may add an *else block*, the code inside will execute if the code in *try* didn't raise an exception.
	- The *else block* is the right place for code that does not need *the try block's protection*.
	**==> Good to know:** Exception handling don't just handle exceptions if they happen in the *try block*, but also if they occur **inside functions that are called (even indirectly) in the *try block*.**

- **When do we need to use exceptions:**
	Basically, when you write ***some suspicious code*** that may raise an exception, you can defend your program by placing the *suspicious code* in a `try: block.` Like shown above, after the `try: block`, include an `except: statement`, followed by a block of code which handles the problem as elegantly as possible.
- **What’s the purpose of catching exceptions:**
	If you have no exception handling, and something goes wrong with the program (you divide by 0, you input alpha into a numeric variable, stuff like that...), the program "crashes".
	But friends, with exception handling, the user gets a nice little 'Please don't do that, because...hit Enter to go where you were'
	An elegant crash, not a dirty one.

- **How to raise a builtin exception:**
	*(Exercices 5-raise_exception and 6-raise_exception_msg)*
	The raise statement allows a programmer to force, or throw a specified exception if a condition occurs.
	Have a look at this example, coming from the official python docs:
	```
	>>> raise NameError('HiThere')
	Traceback (most recent call last):
  		File "<stdin>", line 1, in <module>
	NameError: HiThere
	```
	Think of this example, say you want a user to enter a date.The date has to be either today or in the future.
	If the user enters a past date, tadaaaa ! in your program you have planned to **raise an exception**:
	```
	dateinput = input("Enter date in yyyy-mm-dd format: ")
	date_provided = datetime.strptime(dateinput, '%Y-%m-%d')
	print ("Date provided is: " + date_provided.strftime('%Y-%m-%d'))

	if (date_provided.date() < current_date.date()):
    	raise Exception("Date provided can't be in the past")
	```

- **When do we need to implement a clean-up action after an exception:**
	The *try statement* supports another optional block which is designed to define *clean-up actions* that **must be executed under all circumstances.**
	This *clean-up block* is declared in a **finally:**	clause. If the **finally** is present, it will be executed wether or not the `try` statement produces an exception.

	In real world applications, the finally clause is **useful** for releasing external resources (such as files or network connections), *regardless of whether the use of the resource was successful.*

