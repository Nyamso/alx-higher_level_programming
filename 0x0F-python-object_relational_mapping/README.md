Object Relational Mapping
Each file in this repository holds code that illustrates an essential concept of programming, specific to databases and uses MySQLdb and sqlAlchemy with Python scripts

Resources
ORMs, SQLAlchemy, MySQLdb documentation, Python MySQL documentation, SQLAlchemy documentation, prevent SQL injections

Environment
Language: Python 3.4.3
Databases: MySQL 5.7, MySQLdb v1.3.10, sqlAlchemy v1.2.5
OS: Ubuntu 14.04 LTS
Compiler: python3
Style guidelines: PEP 8 (version 1.7) for Python 3.5 || Google Style Python Docstrings
MySQLdb

$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
...
$ python3
>>> import MySQLdb
>>> MySQLdb.__version__ 
'1.3.13'
SQLAlchemy

$ pip3 install SQLAlchemy
...
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__ 
'1.2.10'
