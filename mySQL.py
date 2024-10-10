import csv
import MySQLdb


#Create a Connection
myconnection = MySQLdb.Connection(host = "localhost", user = "root", passwd = "ceit")

#Create a Cursor Object use to hold connection
mycursor = myconnection.cursor()

#now lets start with SQL quiries
#mycursor.execute('CREATE DATABASE CEITLIBRARY')
#mycursor.execute('USE CEITLIBRARY')
#tablebook = """CREATE TABLE book(bookID int primary key, title varchar(20), author varchar(20), genre varchar(20))"""
#tablereader= """CREATE TABLE reader(readerID int primary key ,rname Varchar(20),Phone varchar(10), BookID int)"""
#mycursor.execute('SHOW DATABASES')
file = open('book.csv')
contents = csv.reader(file)
insertVal = "INSERT INTO book (bookID, title, author,genre) VALUES (?,?,?,?)"
mycursor.executemany(insertVal,contents)
selectall = "SELECT * FROM book"
rows = mycursor.execute(selectall).fetchall()
for row in rows:
    print(row)


#book1 =  """INSERT INTO book VALUES(101,"Intro to Phyton","Tom Jerry","Programming")"""
#reader1 = """INSERT INTO reader VALUES(201,"Peter Parker",3267424,101)"""

#To execute tablebook
#mycursor.execute(tablebook)
#mycursor.execute(reader1)
#To Fetch data and display output
#result = mycursor.fetchall()

#Commit change
myconnection.commit()

myconnection.close()










