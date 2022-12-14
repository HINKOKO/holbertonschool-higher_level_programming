# **Python :snake: - Classes and Objects**

## **Learning Objectives**

- **What is OOP:**
	Python is called an `Object-Oriented programming language`, this means there is a construct in Python called a `class` that **lets you structure your software in a particular way**. Using `classes`, you can add consistency to your programs so that they can be used in a cleaner way. **At least that's the theory.**
	  ***why do we need OOP***
	  - Makes developing large software projects easier and more intuitive
	  - Allows us to think of complex software in terms of real-world objects and <br>
	  their relationship to one another
	  - A very common **programming paradigm (i.e. style of designing a software, specific way we design the software)
	
- **“first-class everything” :**
	I have to tell you something guys: in Python, `everrything is a class`, yes indeed, Sir Guido Van Rossum has designed Python according to the principle written as title: **"first class everything".**
	In other words, he wanted *everything* to be treated the same way, everything is a class implies that functions and methods are values just like lists, integers, characters...Each of these are instances of their corresponding classes.
	Guido wrote:"One of my goals for Python was to make it so that all objects were "first class", by this, I meant that I wanted all objects that could be named in the language (e.g. integers, strings, functions, classes, modules, methods, and so on) to have an equal status. That is, they can be assigned to variables, placed in lists, stored in dictionaries, passed as arguments, an so forth" (Blog, The History of Python, February 27, 2009).

- **What is a class:**
	A class is a way to take a grouping of functions and data and place them inside a `container` so you can access them with the `dot "." ` operator.

- **What is an object and an instance:**
	An **Object** is an entity, or a "thing" in your program, often a noun.(such as a person, an email)
	**Objects** are like little bundles of data that will be used in the life of our program.
	For example, a person will have *properties* (or "data"), like *Name, Age, Adress*, our object also have *behaviors* , the actions the object can take, like *Walk, Talk, Breathe.*

- **What is the difference between a class and an object or instance:**
	**`Classes`** are used to create *user-defined data structures*.**`Classes`** define functions called **`methods`**, which will define the *behaviors* and *actions* that an object created from the class can perform with its own data.
	So a `class` is kind of a **blueprint** for how something should be defined.(No data in it actually)
	While the class is a **blueprint**, an **`instance`** is an `object` that is build from the class and contains **real data.** An **`Instance`** of the **`class`** is not a **blueprint** anymore.
	So when you are being said: "Hey man, `Instantiate` the class with blablabla..." it's just a fancy, obnoxious, overly smart way to say "create".
	When you `instantiate`a class what you get is called an `object`.
- **What is an attribute:**
	Attributes are created inside a class definition. an attribute is a property a class has, that are from composition and usually variables. <br>
	Achtung ! **Class vs. Instance Attributes:** <br>
		

- **What are and how to use public, protected and private attributes:**
	| Naming | Type | Meaning |
	|--------|------|---------|
	| name   | Public| these attributes can be freely used  inside or outide a class definition |
	|_name | Protected | Protected attribute should'nt be used outside the class definition, unless inside a subclass definition |
	| __name | Private | This kind os attribute is inaccessible and invisible? It's neither possible to read nor write to those attributes, except inside the class definition itself | 


- What is self
- What is a method
- What is the special __init__ method and how to use it
- What is Data Abstraction, Data Encapsulation, and Information Hiding
- What is a property
- What is the difference between an attribute and a property in Python
- What is the Pythonic way to write getters and setters in Python
- How to dynamically create arbitrary new attributes for existing instances of a class
- How to bind attributes to object and classes
- What is the __dict__ of a class and/or instance of a class and what does it contain
- How does Python find the attributes of an object or class
- How to use the getattr function
