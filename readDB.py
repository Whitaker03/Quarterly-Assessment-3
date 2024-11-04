import sqlite3

def read_database():
    # Connect to the questions.db database
    conn = sqlite3.connect('questions.db')
    cursor = conn.cursor()
    
    # Retrieve all table names in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()
    
    # Print all table names
    print("Tables in the database:")
    for i, table in enumerate(tables, start=1):
        print(f"{i}. {table[0]}")
    
    # Ask user to choose a table
    table_choice = input("Enter the name of the table you want data from: ")
    
    # Check if the chosen table exists in the database
    if (table_choice,) in tables:
        # Fetch and display all data from the chosen table
        cursor.execute(f"SELECT * FROM {table_choice}")
        rows = cursor.fetchall()
        
        # Print each row from the selected table
        print(f"\nData from table '{table_choice}':")
        for row in rows:
            print(row)
    else:
        print("Invalid table name. Please try again.")
    
    # Close the database connection
    conn.close()
