import sqlite3

def create_mkt3400():
    try:
        # Connect to the existing questions.db
        conn = sqlite3.connect('questions.db')
        cursor = conn.cursor()

        # Check if the MKT3400 table already exists
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='MKT3400';")
        if cursor.fetchone():
            print("MKT3400 table already exists.")
        else:
            # Create MKT3400 table
            print("Creating MKT3400 table...")
            cursor.execute('''
                CREATE TABLE MKT3400 (
                    id INTEGER PRIMARY KEY,
                    question TEXT,
                    option_a TEXT,
                    option_b TEXT,
                    option_c TEXT,
                    option_d TEXT,
                    correct_option TEXT
                )
            ''')

            # List of marketing questions with options and correct answers
            marketing_questions = [
                ("What is the primary goal of marketing?", "To increase profit", "To satisfy customer needs", "To advertise products", "To expand globally", "b"),
                ("Which 'P' in the marketing mix refers to the distribution of products?", "Product", "Price", "Promotion", "Place", "d"),
                ("What is a target market?", "A segment of consumers to focus on", "A general consumer group", "A type of product", "A pricing strategy", "a"),
                ("Which marketing mix element includes advertising and sales promotion?", "Product", "Place", "Promotion", "Price", "c"),
                ("What does 'branding' mean in marketing?", "Lowering prices", "Creating a unique identity", "Expanding into new markets", "Hiring new employees", "b"),
                ("What is market segmentation?", "Setting prices based on demand", "Dividing a market into distinct groups", "Creating new products", "Promoting a brand", "b"),
                ("Which term describes the end customer for a product?", "Consumer", "Vendor", "Supplier", "Manufacturer", "a"),
                ("What is the purpose of a SWOT analysis?", "To price products", "To evaluate strengths, weaknesses, opportunities, and threats", "To survey customer satisfaction", "To create a marketing budget", "b"),
                ("Which pricing strategy involves setting high prices initially?", "Penetration pricing", "Cost-plus pricing", "Skimming pricing", "Competitive pricing", "c"),
                ("What is a 'product lifecycle'?", "The process of manufacturing a product", "The duration of a product's development", "Stages a product goes through in the market", "A marketing budget plan", "c")
            ]

            # Insert questions into the MKT3400 table
            print("Inserting data into MKT3400 table...")
            cursor.executemany('''
                INSERT INTO MKT3400 (question, option_a, option_b, option_c, option_d, correct_option) 
                VALUES (?, ?, ?, ?, ?, ?)
            ''', marketing_questions)

            # Commit the transaction
            conn.commit()
            print("MKT3400 table created and data inserted successfully.")

    except sqlite3.Error as e:
        print(f"An error occurred: {e}")

    finally:
        # Close the connection
        conn.close()

# Run the function to create MKT3400
create_mkt3400()
