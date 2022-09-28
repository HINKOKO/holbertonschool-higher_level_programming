# **Python :snake: - Inheritance**

## **Learning Objectives**

- **What is a superclass, baseclass or parentclass:**
	A **superclass** is a class *that is being inherited from*. BE aware of this: Technically, every class we create use inheritance. All Python classes are subclasses of the special class named object. This class provides very little in terms of data and behaviors (those behaviors it does provide are all double-underscore methods intended for internal use only - Have a look at [Module-0-lookup.py](0-lookup.py)), but it does allow Python to treat all objects in the same way. If we do:
	```
	class MySubClass(obj):
		pass
	```
	THis is Inheritance !! Since Python 3 automatically inherits from object if we don’t explicitly provide a different superclass. Let's say it again: A superclass, or parent class, **is a class that is being inherited from**
	If we don’t explicitly inherit from a different class, our classes will automatically inherit from object. 
- **What is a subclass:**
	 A subclass is a **class that is inheriting from a superclass.** In previous case (previous entry), the **superclass** is *object*, and *MySubClass* is the **subclass.** A subclass is also said to be derived from its parent class or that the subclass extends the parent.
- **How to list all attributes and methods of a class or instance:**
	WE can use the **dir()** built-in method, actually, this is the simpliest method, just call it like this:
	``dir(objectname)`` . Note that it returns an object of **type <class 'list'>**
- **When can an instance have new attributes:**
- How to inherit class from another
- How to define a class with multiple base classes
- What is the default class every class inherit from
- How to override a method or attribute inherited from the base class
- Which attributes or methods are available by heritage to subclasses
- **What is the purpose of inheritance:**
	Used the proper way, Inheritance can reduce the amount of code you write, while simultaneously reflecting the real-world relationship between "objects" and the links between their properties.
- **What are, when and how to use isinstance, issubclass, type and super built-in functions:**
	Don’t get confused between **isinstance()** and **issubclass()** as both these method are quite similar. However, the name itself explain the differences. *isinstance()* checks whether or not the object is an instance or subclass of the classinfo. Whereas, issubclass() only check whether it is a subclass of classinfo or not (not check for object relation).
