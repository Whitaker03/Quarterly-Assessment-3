import sqlite3

def check_tables():
    # Connect to the questions.db database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    
    # Retrieve all table names
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Print all table names
    print("Tables in the database:")
    for table in tables:
        print(table[0])
    
    # Close the connection
    conn.close()

# Run the function to check tables
check_tables()
