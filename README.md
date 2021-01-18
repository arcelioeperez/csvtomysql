[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)  ![GitHub commit activity](https://img.shields.io/github/commit-activity/w/arcelioeperez/csvtomysql) [![PyPI - Python Version](https://img.shields.io/pypi/pyversions/Pandas)](https://www.sqlalchemy.org/)

# CSV to MySQL  

### How to use the `tomysqlv2-1` executable:  

**Use `tomysqlv2-1` which contains exception handlers -- in case you mistype your filename, or if the filename is not in the same work directory it lets you type it again.**

```
git clone https://github.com/arcelioeperez/csvtomysql.git && cd csvtomysql
chmod +x tomysqlv2-1
./tomysqlv2-1
```  

Check that the command to run **Python 3** is `python3` or `python`. In Unix like systems (MacOS and GNU-Linux it's `python3`), but in Windows it might be `python` depending on the terminal that you use    

### Structure of the program  
Two classes 
- Csv: reads csv file, creates the table with the appropiate data types  
- MysqlConnection: creates the MySQL statement, connects to the database, and exports the dataframe to MySQL    

### Sample case:  

- The prompts will appear on the terminal.  

### Requirements:   
*If using a virtual environment, use `pip`. If using the terminal, then use `pip3`.*   
pandas==1.1.5   
SQLAlchemy==1.3.21  
PyMySQL==0.10.1   
mysqlclient==2.0.2

### Limitations:  
- Only works for MySQL  
  - It has only been tested with the terminal version of MySQL  
  - Commands MySQL terminal  
  ```
  #open mysql and type your password. 
  #change **root** to your username in mysql 
  mysql -u root -p 
  
  #to view the databases
  show databases; 
  
  #select a database 
  use test; 
  
  #to show the tables inside the database 
  show tables; 
  
  #test query -- show first 10 rows 
  select * from test limit 10; 
  
  #quit mysql 
  \quit 
  ```  
- If the CSV file doesn't contain headers it doesn't work. The user would have to create the table manually in MySQL  
- The program has only been tested on the GNU-Linux Ubuntu Distribution  
  - Several packages had to be downloaded in order to achieve the connection to MySQL  
  - According to PyPI's documentation of `mysqlclient`, Ubuntu users should install the following libraries:  
  
  ```
  sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
  #then -- in a virtual environment, if not then pip3
  pip install mysqlclient
  ```  
  More information here: [PyPI - mysqlclient](https://pypi.org/project/mysqlclient/)    
  
- It doesn't have a GUI - all the prompts appear on the terminal  

**Image from the terminal:**    
![image](./csvtomysql-image.png)  

### References:  
[StackOverflow - "How to create a new table in MySQL from a pandas dataframe"](https://stackoverflow.com/questions/51236304/how-to-create-a-new-table-in-a-mysql-db-from-a-pandas-dataframe)    
[Buttons - Shields.io](http://shields.io/)
