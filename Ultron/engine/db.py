import csv
import sqlite3

con = sqlite3.connect("ultron.db")
cursor = con.cursor()

'''query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
cursor.execute(query)

query = "INSERT INTO sys_command VALUES (null,'one note', 'C:\\Program Files\\Microsoft Office\\root\\Office16\\ONENOTE.exe')"
cursor.execute(query)
con.commit()'''

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
cursor.execute(query)

cursor.execute("""INSERT INTO web_command VALUES (NULL, 'chatgpt', 'https://chatgpt.com/')""")
con.commit()
#query = "INSERT INTO web_command VALUES (null,'youtube', 'https://www.youtube.com/')"
#cursor.execute(query)
#con.commit()

#cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#print(cursor.fetchall())



# testing module
# app_name = "android studio"
# cursor.execute('SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
# results = cursor.fetchall()
# print(results[0][0])

# Create a table with the desired columns
#cursor.execute('''CREATE TABLE IF NOT EXISTS contacts (id integer primary key, name VARCHAR(200), mobile_no VARCHAR(255), email VARCHAR(255) NULL)''')


# Specify the column indices you want to import (0-based index)
# Example: Importing the 1st and 3rd columns
# desired_columns_indices = [0, 30]

# # Read data from CSV and insert into SQLite table for the desired columns
# with open('contacts.csv', 'r', encoding='utf-8') as csvfile:
#     csvreader = csv.reader(csvfile)
#     for row in csvreader:
#         selected_data = [row[i] for i in desired_columns_indices]
#         cursor.execute(''' INSERT INTO contacts (id, 'name', 'mobile_no') VALUES (null, ?, ?);''', tuple(selected_data))

# # Commit changes and close connection
# con.commit()
# con.close()

# query = "INSERT INTO contacts VALUES (null,'pawan', '1234567890', 'null')"
# cursor.execute(query)
# con.commit()

# query = 'kunal'
# query = query.strip().lower()

# cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
# results = cursor.fetchall()
# print(results[0][0])


# Define a function to display all records from a given table
def display_table_records(table_name):
    try:
        # Select all rows from the specified table
        cursor.execute(f"SELECT * FROM {table_name}")
        records = cursor.fetchall()
        
        # Print each record
        print(f"Records in table '{table_name}':")
        for row in records:
            print(row)
            
    except sqlite3.OperationalError as e:
        print(f"Error: {e}")

# View records in sys_command table
display_table_records("sys_command")

# View records in web_command table
display_table_records("web_command")

# Close the connection
con.close()
