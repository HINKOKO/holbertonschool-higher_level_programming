# **Python - Import & Modules**

<br>

<p align="center">
  <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/640px-Python.svg.png" />
</p>


## **General**

- Why Python programming is awesome
- How to import functions from another file
- How to use imported functions
- How to create a module
- *How to use the built-in function dir()*
    The dir() method returns the list of valid attributes of the passed object.
    the syntax of dir() method is like so:
    ```
    dir(object)
    ```
    dir() method takes in a **single parameter**: <br>
    - ***object*** can be an empty/filled tuple, list, set, dictionnary or any user-defined object
    dir() method returns: <br>
    - the list of attributes of the object passed to the method. 
- *How to prevent code in your script from being executed when imported*
    To prevent code in your module from being executed when imported, but only when run directly,
    you can guard it with this ```if```
    ```
    if __name__ == "__main__":
        # this won't be run when imported
    ```
    ==> **What does if __name__ == "__main__": do in Python?**
    We use the if-statement to run blocks of code only if our program is the main program executed. This allows our program to be executable by itself, but friendly to other Python modules who may want to import some functionality without having to run the code.
- *How to use command line arguments with your Python programs*
    
