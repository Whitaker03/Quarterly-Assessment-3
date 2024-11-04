import sqlite3

def create_law2810():
    try:
        # Connect to the existing questions.db
        conn = sqlite3.connect('questions.db')
        cursor = conn.cursor()

        # Check if the LAW2810 table already exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='LAW2810';")
        if cursor.fetchone():
            print("LAW2810 table already exists.")
        else:
            # Create LAW2810 table
            print("Creating LAW2810 table...")
            cursor.execute('''
                CREATE TABLE LAW2810 (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    option_a TEXT,
                    option_b TEXT,
                    option_c TEXT,
                    option_d TEXT,
                    correct_option TEXT
                )
            ''')

            # List of business law and ethics questions with options and correct answers
            law_questions = [
                ("Which document is essential for legally forming a corporation?", "Contract", "Bylaws", "Articles of Incorporation", "Code of Conduct", "c"),
                ("What is the primary role of a business contract?", "To create a partnership", "To establish legal obligations", "To increase profit", "To monitor employees", "b"),
                ("Which law protects consumers from deceptive business practices?", "Environmental Law", "Consumer Protection Law", "Labor Law", "Tax Law", "b"),
                ("What does 'ethics' in business primarily refer to?", "Company profitability", "Corporate structure", "Moral principles", "Market position", "c"),
                ("Which agency oversees workplace safety in the U.S.?", "OSHA", "FDA", "SEC", "IRS", "a"),
                ("What is considered a conflict of interest in business?", "Working overtime", "Hiring employees", "Personal gain from decisions", "Following company policies", "c"),
                ("What is intellectual property?", "Physical assets of a business", "Innovative ideas or creations", "A type of contract", "Public domain material", "b"),
                ("Which law protects employees against discrimination?", "Tax Law", "Employment Law", "Intellectual Property Law", "Corporate Law", "b"),
                ("What is the purpose of antitrust laws?", "To promote competition", "To protect intellectual property", "To monitor employee conduct", "To standardize contracts", "a"),
                ("Which term describes a legal obligation to act in another's best interest?", "Trustworthiness", "Loyalty", "Fiduciary duty", "Confidentiality", "c")
            ]

            # Insert questions into the LAW2810 table
            print("Inserting data into LAW2810 table...")
            cursor.executemany('''
                INSERT INTO LAW2810 (question, option_a, option_b, option_c, option_d, correct_option) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', law_questions)

            # Commit the transaction
            conn.commit()
            print("LAW2810 table created and data inserted successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        conn.close()

# Run the function to create LAW2810
create_law2810()
