import tkinter as tk
from tkinter import messagebox
from questionmanager import QuestionManager  # Import the QuestionManager class

# Global variable to store selected course for quiz
selected_course = None

# Main Window: Course Selection
def open_main_window():
    def start_quiz():
        global selected_course
        selected_course = course_var.get()
        if selected_course:
            root.destroy()  # Close main window
            open_quiz_window(selected_course)
        else:
            messagebox.showwarning("Warning", "Please select a course.")

    root = tk.Tk()
    root.title("Course Selection")
    root.geometry("300x200")

    tk.Label(root, text="Select a course:").pack(pady=10)
    course_var = tk.StringVar(value="")

    # Add radio buttons for course selection
    for course in ["DS3850", "DS3860", "DS3810", "LAW2810", "MKT3400"]:
        tk.Radiobutton(root, text=course, variable=course_var, value=course).pack(anchor="w")

    start_button = tk.Button(root, text="Start Quiz Now", command=start_quiz)
    start_button.pack(pady=20)

    root.mainloop()

# Quiz Window
def open_quiz_window(course):
    # Initialize question manager with the selected course
    manager = QuestionManager("questions.db", course)

    # Function to display the next question
    def display_question():
        question = manager.get_current_question()
        if question:
            question_label.config(text=question["question"])
            option_a.config(text="A: " + question["options"][0])
            option_b.config(text="B: " + question["options"][1])
            option_c.config(text="C: " + question["options"][2])
            option_d.config(text="D: " + question["options"][3])
        else:
            # End of quiz
            messagebox.showinfo("Quiz Completed", "You've completed the quiz!")
            quiz_window.destroy()  # Close quiz window
            open_main_window()  # Return to course selection

    # Check answer and give feedback
    def submit_answer():
        selected = answer_var.get()
        if selected:
            is_correct = manager.check_answer(selected)
            feedback = "Correct!" if is_correct else "Incorrect."
            messagebox.showinfo("Feedback", feedback)
            answer_var.set("")  # Reset selected answer
            display_question()  # Load next question
        else:
            messagebox.showwarning("Warning", "Please select an answer.")

    # Create quiz window
    quiz_window = tk.Tk()
    quiz_window.title(f"Quiz - {course}")
    quiz_window.geometry("400x300")

    question_label = tk.Label(quiz_window, text="", wraplength=350, font=("Arial", 12))
    question_label.pack(pady=20)

    answer_var = tk.StringVar(value="")

    # Option buttons
    option_a = tk.Radiobutton(quiz_window, text="", variable=answer_var, value="a", font=("Arial", 10))
    option_b = tk.Radiobutton(quiz_window, text="", variable=answer_var, value="b", font=("Arial", 10))
    option_c = tk.Radiobutton(quiz_window, text="", variable=answer_var, value="c", font=("Arial", 10))
    option_d = tk.Radiobutton(quiz_window, text="", variable=answer_var, value="d", font=("Arial", 10))

    option_a.pack(anchor="w", padx=20)
    option_b.pack(anchor="w", padx=20)
    option_c.pack(anchor="w", padx=20)
    option_d.pack(anchor="w", padx=20)

    submit_button = tk.Button(quiz_window, text="Submit Answer", command=submit_answer)
    submit_button.pack(pady=20)

    display_question()  # Display the first question

    quiz_window.mainloop()

# Start the GUI by opening the main window
open_main_window()
