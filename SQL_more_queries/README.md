# **SQL - More queries**

## **Learning Objectives**

- **How to create a new MySQL user**
	We use the ``CREATE USER`` statement to...create one or more new user(s) (with no privileges)
	Here's the basic command for creating one:
	```
	mysql > CREATE USER 'Layla'@'localhost' IDENTIFIED BY 'password';
	```
	Be sure to change ``Layla`` with the name you want, and ``password`` with a strong pass of your choosing
- **How to manage privileges for a user to a database or table**
	We manage privileges with the MySQL **GRANT** Statement
- What’s a PRIMARY KEY
- What’s a FOREIGN KEY
- How to use NOT NULL and UNIQUE constraints
- How to retrieve datas from multiple tables in one request
- What are subqueries
- What are JOIN and UNION
