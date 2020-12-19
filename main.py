import sqlalchemy 
import pandas as pd
import pymysql 
from sqlalchemy import create_engine

"""
-----------------------
Run an executable with: 
$ chmod +x tomysql
$ ./tomysql
-----------------------
Needed user input: 
file_name string
db user string
db password string
db host string
db database name string
------------------------
First class - Csv (inner class Sql) 


Flow of the program: 
1. create an object 
>>>firsttable = Csv("file.csv")

2.get the table columns
>>>firsttable.table_columns()

3.create a user
>>>user = firsttable.Sql(user = "root", password = "lacortes9", host
= "localhost", database = "test")

4.create a table
>>>user.create_table(table_name = "newtable")

5.implement the cursor
>>>user.cur_conn()

6.trasnfer to database 
>>>user.df_to_sql()
"""

class Csv:
    def __init__(self, file_name): 
        self.file_name = file_name
        global data
        data = pd.read_csv(self.file_name)
        global headers 
        headers = data.dtypes.index

    def table_columns(self): 
        self.stmt = "id INT AUTO_INCREMENT PRIMARY KEY"
        self.tmap = {'object' : 'TEXT',
        'int64' : 'INT',
        'float64' : 'FLOAT',
        'datetime64' : 'DATETIME',
        'bool' : 'TINYINT',
        'category' : 'TEXT',
        'timedelta[ns]' : 'TEXT'}
        self.headers_list = [(i, str(data.dtypes[i])) for i in headers]
        for i, h1 in enumerate(self.headers_list): 
            self.stmt += f", {h1[0]} {self.tmap[h1[1]]}"
        return self.stmt 
    class Sql: 
        def __init__(self, user, password, host, database):
            self.user = user
            self.password = password
            self.host = host 
            self.database = database 
        def create_table(self, table_name): 
            self.table_name = table_name
            self.sql = f"CREATE TABLE IF NOT EXISTS {self.table_name} ({Csv.table_columns(self)});"
            return self.sql
        def cur_conn(self): 
            self.sql_engine=create_engine(f"mysql+pymysql://{self.user}:{self.password}@{self.host}/{self.database}")
            self.connection = self.sql_engine.raw_connection()
            self.cursor = self.connection.cursor()
            self.execute = self.cursor.execute(self.sql)
            self.cursor.close()
            self.connection.commit()
        def df_to_sql(self, h_file): 
            self.h_file = h_file
            self.df = pd.read_csv((self.h_file), delimiter = ",", header = None)
            self.df.to_sql(self.table_name, con = self.sql_engine, if_exists = "replace", index = False, index_label = False)

#Sample Case

#Creating Objects from classes
csv_name = str(input("Please enter the name of the CSV file: "))
atable = Csv(csv_name)
atable.table_columns()
#User info
username = str(input("Please enter the username for MySQL: ")) 
p = str(input("Please enter your password: "))
hostname = str(input("Please enter your hostname, i.e. localhost: "))
database = str(input("Please enter the database name: ")) 
user = atable.Sql(user = username, password = p, host
= hostname, database = database)
#Connection 
t_name = str(input("Please enter the table name: "))
user.create_table(table_name = t_name)
user.cur_conn()
#To database
user.df_to_sql(csv_name)
