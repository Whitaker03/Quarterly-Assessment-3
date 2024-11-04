import sqlite3

def read_database():
    try:
        # Connect to the questions.db database
        conn = sqlite3.connect('questions.db')
        cursor = conn.cursor()
        
        # Retrieve all table names in the database
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = cursor.fetchall()
        
        # Check if there are any tables
        if not tables:
            print("No tables found in the database.")
            return
        
        # Print all table names
        print("Tables in the database:")
        for i, table in enumerate(tables, start=1):
            print(f"{i}. {table[0]}")
        
        # Ask user to choose a table
        table_choice = input("Enter the name of the table you want data from: ")
        
        # Verify the chosen table exists
        if (table_choice,) in tables:
            # Fetch and display all data from the chosen table
            cursor.execute(f"SELECT * FROM {table_choice}")
            rows = cursor.fetchall()
            
            # Check if there is data in the table
            if rows:
                print(f"\nData from table '{table_choice}':")
                for row in rows:
                    print(row)
            else:
                print(f"No data found in table '{table_choice}'.")
        else:
            print("Invalid table name. Please try again.")
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    
    finally:
        # Close the database connection
        conn.close()

# Run the function to test
read_database()
