import sqlite3

# Connect to the existing questions.db
conn = sqlite3.connect('questions.db')
cursor = conn.cursor()

# Create a new table called DS3810
cursor.execute('''
    CREATE TABLE IF NOT EXISTS DS3810 (
        id INTEGER PRIMARY KEY,
        question TEXT,
        option_a TEXT,
        option_b TEXT,
        option_c TEXT,
        option_d TEXT,
        correct_option TEXT
    )
''')

# List of Python and analytic thinking questions with options and correct answers
logic_questions = [
    ("What is the output of 'print(3 + 4 * 2)' in Python?", "14", "11", "8", "7", "b"),
    ("Which operator is used for integer division in Python?", "/", "//", "%", "**", "b"),
    ("What is the purpose of the 'len()' function in Python?", "Adds two numbers", "Calculates the square root", "Counts characters or items", "Sorts a list", "c"),
    ("If you need to check multiple conditions in an `if` statement, which keyword would you use?", "OR", "WITH", "AND", "THEN", "c"),
    ("What is the output of 'print(10 % 3)'?", "1", "3", "0", "2", "a"),
    ("If a list in Python has 5 elements, what is the index of the last element?", "4", "5", "-1", "0", "a"),
    ("Which function would you use to round a number to the nearest integer in Python?", "ceil()", "floor()", "round()", "int()", "c"),
    ("Which data structure would be best for storing unique values only?", "List", "Tuple", "Set", "Dictionary", "c"),
    ("What is the logic term for a statement that is either true or false?", "Condition", "Argument", "Statement", "Boolean", "d"),
    ("In an algorithm, what is the term for a step that repeats until a condition is met?", "Decision", "Loop", "Process", "Break", "b")
]

# Insert questions into the DS3810 table
cursor.executemany('''
    INSERT INTO DS3810 (question, option_a, option_b, option_c, option_d, correct_option) 
    VALUES (?, ?, ?, ?, ?, ?)
''', logic_questions)

# Commit the transaction
conn.commit()

# Close the connection
conn.close()
