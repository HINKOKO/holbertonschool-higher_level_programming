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
- What is JSON
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure
