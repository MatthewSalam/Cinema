#import required modules
import mysql.connector

#create connection object
con  = mysql.connector.connect(
    host = "localhost", user = "root",
    password = "", database = "cinema_db"
)

#create cursor object
cursor = con.cursor()

#assign data query
query1 = "desc users"

#execute cursor
cursor.execute(query1)

#display all
table = cursor.fetchall()

#describe tables
print("/n Table Description: ")
for attr in table:
    print(attr)

#assign data query
query2 = "select * from users"

#executing cursor
cursor.execute(query2)

#display all records
table = cursor.fetchall()

#fetch all columns 
print("/n Table Data: ")
for row in table:
    print(row[0], end=" ")
    print(row[1], end=" ")
    print(row[2], end = " ")
    print(row[3], end = " ")

#close cursor connection
cursor.close()

#closing connection object
con.close()