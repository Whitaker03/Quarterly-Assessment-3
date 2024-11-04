import sqlite3

# Connect to the existing questions.db
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create a new table called DS3860
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DS3860 (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_option TEXT
    )
''')

# List of SQL questions with options and correct answers
sql_questions = [
    ("Which SQL keyword is used to retrieve data from a database?", "GET", "SELECT", "RETRIEVE", "SHOW", "b"),
    ("What does the SQL 'WHERE' clause do?", "Limits results to specified conditions", "Sorts the data", "Combines two tables", "Removes duplicates", "a"),
    ("How do you sort the result set in ascending order in SQL?", "SORT BY", "ORDER ASC", "ORDER BY", "GROUP BY", "c"),
    ("Which SQL function is used to calculate the number of rows in a table?", "COUNT()", "SUM()", "TOTAL()", "ROWS()", "a"),
    ("What SQL command is used to delete a table?", "REMOVE TABLE", "DROP TABLE", "DELETE TABLE", "CLEAR TABLE", "b"),
    ("Which SQL clause is used to group rows that have the same values in specified columns?", "GROUP BY", "ORDER BY", "PARTITION BY", "FILTER BY", "a"),
    ("What keyword is used in SQL to eliminate duplicate rows in the result set?", "REMOVE", "DELETE", "DISTINCT", "UNIQUE", "c"),
    ("How do you retrieve only unique records in SQL?", "SELECT UNIQUE", "SELECT DISTINCT", "SELECT DISTINCTROW", "SELECT ONLY", "b"),
    ("Which SQL statement is used to update data in a table?", "UPDATE", "MODIFY", "CHANGE", "REVISE", "a"),
    ("What SQL command is used to add a new row to a table?", "INSERT INTO", "ADD ROW", "ADD RECORD", "NEW ROW", "a")
]

# Insert SQL questions into the DS3860 table
cursor.executemany('''
    INSERT INTO DS3860 (question, option_a, option_b, option_c, option_d, correct_option) 
    VALUES (?, ?, ?, ?, ?, ?)
''', sql_questions)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
