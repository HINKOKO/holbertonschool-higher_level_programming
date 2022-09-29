# **Python :snake: - Input/Output**

## **Learning Objectives**

- **How to open a file:**
	Use the built-in function **open()** wich returns a file object, and has a read() method for readind the content of the file.
	If the file is in the same folder, you call direclty its name, otherwise if it is located elsewhere, you'll have to specify the path:
	```
	open("demo.txt", "r")

	open("D:\\mypython\demo.txt", "r")
	```
	open() is most commonly used with 2 argument, and one keyword argument like so 
	```
	file = open('work', 'w', encoding="utf-8")
- **How to write text in a file:**

- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the with statement
- **What is JSON:**
	A JSON file is a file that stores simple data structures and objects in JavaScript Object Notation (JSON) format, which is a standard data interchange format. It is primarily used for transmitting data between a web application and a server. JSON files are lightweight, text-based, human-readable, and can be edited using a text editor.
	- **JSON** is an abbreviation of JavaScript Object Notation
		JSON is a text-based data format following JavaScript object syntax, which was popularized by Douglas Crockford. Even though it closely resembles JavaScript object literal syntax, it can be used independently from JavaScript, and many programming environments feature the ability to read (parse) and generate JSON.
		*JSON exists as a string — useful when you want to transmit data across a network.*
	- Though the name has "JavaScript" on it, JSON is a language independent **data interchange format**
	- JSON is a text-based data interchange format
	- Any Python object can be **serialized** into JSON format and vice-versa
	- All popular programming languages supports converting objects into JSON and vice-versa
	- Without involving any objects as well, JSON strings can be formed and interchanged between any two processes, client and server as data.
	- Several REST APIs and web services return data as JSON. Even the error messages from the REST APIs are returned as JSON strings.
- **What is serialization:**
	Serialization refers to the process of **converting a data object** (e.g., Python objects, Tensorflow models) into a format that allows us *to store or transmit the data* and then *recreate the object when needed using the reverse process of **deserialization.**
	
	There are different formats for the serialization of data, such as **JSON!**, XML, HDF5, and Python’s pickle, for different purposes. JSON, for instance, returns a ***human-readable string form**, while Python’s pickle library can return a byte array.

	**<u>?WHy do we serialize?</u>**
	Think about storing an integer; how would you store that in a file or transmit it? That’s easy! We can just write the integer to a file and store or transmit that file.
	...
	Now Think about storing a **Python object** (e.g., a Python dictionary or a Pandas DataFrame), which has a complex structure and many attributes (e.g., the columns and index of the DataFrame, and the data type of each column)? How would you store it as a file or transmit it to another computer?
	**Here comes serialization**
	Like we said previously: **Serialization** is the process of converting the object into a format that can be *stored or transmitted.* After transmitting or storing the serialized data, we are able to reconstruct the object later and obtain the exact same structure/object, which makes it really convenient for us to continue using the stored object later on instead of reconstructing the object from scratch.

	In Python, there are many different formats for serialization available. One common example of *hash maps* (Python dictionaries dudes!) that works across many languages is the JSON file format which is human-readable and allows us to store the dictionary and recreate it with the same structure. But JSON can only store basic structures such as a **list and dictionary**, and it can **only keep strings and numbers.** <u>We cannot ask JSON to remember the data type</u> (e.g., numpy float32 vs. float64). It also <u>cannot distinguish between Python tuples and lists.</u>

	[More powerful serialization formats exist. (two common serialization libraries in Python, namely pickle and h5py.)]


- **What is deserialization:**
	The invert process of what we described just before !
- **How to convert a Python data structure to a JSON string:**
	Have a look at [3-to_json_string](3-to_json_string.py)<br>
	>Don't forget to: **import json** then just use the command **json.dumps** on your `object` you want to convert:<br>
	```
	import json

	json.dumps(object)
	```

- **How to convert a JSON string to a Python data structure:**
	Don't forget again to: **import json**, and use the command **json.loads() on the JSON `string` you want to get into an object (Python data structure)
	```
	import json 

	json.loads(string)
	```

- **dump/dumps and load/loads**

	|     Method       |             Explanation                                              |
	|:----------------:|:--------------------------------------------------------------------:|   
	| **json.dumps()** | This method converts a Python object into a *serialized* JSON Object |
	| **json.dump()**  | This method converts a Python object into JSON and additionally      |
	|				 | and additionally allows you to store the information into a text file  |
	| **json.loads()** | Deserializes a JSON object to a standard Python object               |
	| **json.load()**  | Deserializes a JSON file object into a standard Python object        |
