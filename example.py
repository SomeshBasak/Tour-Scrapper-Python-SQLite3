import sqlite3

# To establish a connection
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data based on a condition
cursor.execute("SELECT * FROM events WHERE band='Fire'")
rows = cursor.fetchall()
print(rows)

# Query certain column based on a condition
cursor.execute("SELECT band,city FROM events WHERE date='10.02.2025'")
rows = cursor.fetchall()
print(rows)

# Delete columns
delete_query = "DELETE FROM events WHERE band='Rock Band'"
cursor.execute(delete_query)
connection.commit()

# Insert new rows
new_rows = [('Water', 'Agra', '16.05.2026'), ('Eagle', 'Delhi', '28.12.2029')]
cursor.executemany("INSERT INTO events VALUES (?,?,?)", new_rows)
connection.commit()

# Insert new row
new_rows = [('Champs', 'Bangalore', '11.09.2030')]
cursor.executemany("INSERT INTO events VALUES (?,?,?)", new_rows)
connection.commit()

# Query all data
cursor.execute("SELECT * FROM events")
rows = cursor.fetchall()
print(rows)