# **JAvaScript Web-scrapping**

## **Learnings**

- **Why JavaScript programming is amazing**
  JavaScript is a scripting or programming language that allows you to implement complex features on web pages — every time a web page does more than just sit there and display static information for you to look at — displaying timely content updates, interactive maps, animated 2D/3D graphics, scrolling video jukeboxes, etc. — you can bet that JavaScript is probably involved. It is the third layer of the layer cake of standard web technologies, two of which (HTML and CSS) we have covered in much more detail in other parts of the Learning Area." (source: MDN)
- **How to manipulate JSON data**
  **JSON** is for **JavaScript Object Notation**, a standard text-based format for representing structured data based on JavaScript object syntax. It is commonly used for transmitting data in web applications (e.g., sending some data from the server to the client, so it can be displayed on a web page, or vice versa). JSON exists as a string — useful when you want to transmit data across a network !
  JSON structure very much resembles JavaScript object literal format. This is constructed like so:

  ```
   {
  "squadName": "Super hero squad",
  "homeTown": "Metro City",
  "formed": 2016,
  "secretBase": "Super tower",
  "active": true,
  "members": [
    {
      "name": "Molecule Man",
      "age": 29,
      "secretIdentity": "Dan Jukes",
      "powers": ["Radiation resistance", "Turning tiny", "Radiation blast"]
    },
    {
      "name": "Madame Uppercut",
      "age": 39,
      "secretIdentity": "Jane Wilson",
      "powers": [
        "Million tonne punch",
        "Damage resistance",
        "Superhuman reflexes"
      ]
    },
  ]
  }
  ```

  So we can load this script/JSON file inside a program, parsing it into a variable called heroesStuff, then we could access the data inside it using the same mechanism/notations , i.e. dot/brackets notation used for JavaScript Objects.
  `JSON.parse()` method **parses a JSON string**, **_constructing the JavaScript value or object_** described by the string in JSON.
  Now, how to "load" those kind of JSON file ? with `request module` or `fetch API`.

- **How to use request and fetch API**
- How to read and write a file using fs module
