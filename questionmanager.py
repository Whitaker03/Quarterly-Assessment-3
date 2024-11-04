import sqlite3
import random

class QuestionManager:
    def __init__(self, database, table_name):
        self.database = database
        self.table_name = table_name
        self.questions = self._fetch_questions()
        self.current_index = 0

    def _fetch_questions(self):
        """Fetch questions from the specified table."""
        conn = sqlite3.connect(self.database)
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM {self.table_name} LIMIT 10")
        rows = cursor.fetchall()
        conn.close()

        # Structure questions as a list of dictionaries for easy access
        questions = [
            {
                "id": row[0],
                "question": row[1],
                "options": [row[2], row[3], row[4], row[5]],
                "correct_option": row[6]
            }
            for row in rows
        ]
        random.shuffle(questions)  # Shuffle questions for randomness
        return questions

    def get_current_question(self):
        """Return the current question and options."""
        if self.current_index < len(self.questions):
            return self.questions[self.current_index]
        return None

    def check_answer(self, selected_option):
        """Check if the selected answer is correct."""
        question = self.questions[self.current_index]
        is_correct = (selected_option == question["correct_option"])
        self.current_index += 1  # Move to the next question
        return is_correct
