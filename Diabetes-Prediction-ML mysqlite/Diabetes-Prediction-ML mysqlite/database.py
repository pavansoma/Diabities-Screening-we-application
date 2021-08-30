import sqlite3

conn = sqlite3.connect('signup.db')
print( "Opened database successfully");

cursor = conn.execute("SELECT name, mail, password from details")
for row in cursor:
   print( "ID = ", row[0])
   print ("NAME = ", row[1])
   print ("ADDRESS = ", row[2])

print ("Operation done successfully")
conn.close()