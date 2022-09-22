# **Python - More classes**

## **Learning Objectives**

- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- **What are the special \_\_str\_\_ and \_\_repr\_\_ methods,how to use them, and in what are they different:**
	They are important **Python object functions**<br>
	<u>Python \_\_str\_\_ :</u> This method returns the `string representation` of the object. This method must return the String object. If we don't implement \_\_str\_\_() function for a class, the built-in method \_\repr\_\_ will be used instead
	<u>Python \_\_repr\_\_ : </u> This method returns the `object representation in string format`.
	If possible, the string returned should be a valid Python expression that can be used to reconstruct the object again. <br>
	<u>**So what's the difference ??**</u> If both the functions returns strings, which is supposed to be the object representation, what the hell differs ? Well, the **\_\_str\_\_** function is supposed to return a human-readable format, which is good for logging or diplaying some information about the object.
	Whereas the **\_\_repr\_\_** is supposed to return an *official string representation of the object*, <u> which can be used to construct the object again </u>
	Have a look at this real life example:
	```
	>>> import datetime
	>>> now = datetime.datetime.now()
	>>> now.__str__()
	'2022-09-22 05:24:32.327452'
	>>> now.__repr__()
	'datetime.datetime(2022, 9, 22, 5, 24, 32, 327452)'
	```
	It's clear now that \_\_str\_\_() method is more **human friendly, human readable**, whereas \_\_repr\_\_() method is more **computer, or machine friendly**, richer in information for reconstruction the object.



- 
- What is a class attribute
- What is the difference between a object attribute and a class attribute
- What is a class method
- What is a static method
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is and what does contain __dict__ of a class and of an instance of a class
- How does Python find the attributes of an object or class
- How to use the getattr function
