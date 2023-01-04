import pyodbc


# Connect to the database server


server = 'localhost'
database = 'master'
username = 'sa'
password = '123Tralala^'
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+username+';PWD='+ password)

# Create the database
cursor = conn.cursor()
conn.autocommit = True
# cursor.execute("CREATE DATABASE mydatabase")
cursor.execute("if not exists (select * from sys.databases where name = 'users2') begin create database users2 end")
cursor.execute("USE users2")


"""

cursor.execute('''
	CREATE TABLE users (
        id INT PRIMARY KEY IDENTITY,
        name VARCHAR(255),
        email VARCHAR(255),
        password VARCHAR(255)
    )
''')
conn.commit()

# Insert some rows
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", "Alice", "alice@temp.com")
cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", "Bob", "bob@temp.com")
conn.commit()
"""
# Close the connection
cursor.close()



