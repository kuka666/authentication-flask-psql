# Authentication-flask-psql
Flask postgreSQL Login Register System with checking token

### Instalation
Install my repoisitory 
```bash
git clone https://github.com/kuka666/authentication-flask-psql.git
pip install -r requirements.txt

Also create table in postgresql:

Create the database with name kuka

CREATE TABLE accounts (
	id serial PRIMARY KEY,
	username VARCHAR ( 50 ) NOT NULL,
	password VARCHAR ( 255 ) NOT NULL,
	token VARCHAR ( 300 ) NOT NULL
);




```

### Usage
```bash
cd authentication-flask-psql
cd src
```

### in the 19 and 20 rows write the usernmae and password
```bash
run the server in compilator 
web.py
http://127.0.0.1:5000/
```



### Examples

Usage examples:
```python
# get the login
http://127.0.0.1:5000/login/
```
![image](https://user-images.githubusercontent.com/80199144/138552960-bb60f7be-c78d-4f55-9e85-86be5144f0eb.png)
```python
# get rhe register
http://127.0.0.1:5000/register
```
![image](https://user-images.githubusercontent.com/80199144/138553002-4deaf614-3ad4-4d9b-8725-437e7b4cdb97.png)
```python
# get the protected
http://127.0.0.1:5000/protected?token=(write ther token)
```
![image](https://user-images.githubusercontent.com/80199144/138553040-87142734-217c-4d2b-84be-8bd7e95b1ada.png)




## License
[MIT](https://choosealicense.com/licenses/mit/)
