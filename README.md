# CSV to MySQL  

### How to use the `tomysql` executable:  

```
git clone https://github.com/arcelioeperez/csvtomysql.git && cd csvtomysql
chmod +x tomysql 
./tomysql
```  

**Alternatively run with**  

```
python3 main.py
```  

### Sample case:  

-The prompts will appear on the terminal.  

### Requirements:   
*If using a virtual environment, use `pip`. If using the terminal, then use `pip3`.*  
pandas==1.1.5   
SQLAlchemy==1.3.21  
PyMySQL==0.10.1   
mysqlclient==2.0.2

### Limitation:  
- Only works for MySQL  
- The program has only been tested on the GNU-Linux Ubuntu Distribution  
  - Several packages had to be downloaded in order to achieve the connection to MySQL  
  - Packages include -- this was installed just to get the `mysqlclient` package:   
  ```
  sudo apt-get install python3-dev default-libmysqlclient-dev build-essential
  #then -- in a virtual environment, if not then pip3
  pip install mysqlclient
  ```  
- It doesn't have a GUI - all the prompts appear on the terminal  

### Citation:  
[StackOverflow - "How to create a new table in MySQL from a pandas dataframe"](https://stackoverflow.com/questions/51236304/how-to-create-a-new-table-in-a-mysql-db-from-a-pandas-dataframe)  
