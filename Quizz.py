import tkinter as tk
from tkinter import messagebox

# ---------- Quiz Data ----------
quiz_data = [
    {"question": "What is the capital of India?",
     "options": ["Mumbai", "New Delhi", "Kolkata", "Chennai"],
     "answer": "New Delhi"},

    {"question": "Which language is used for web apps?",
     "options": ["Python", "Java", "HTML", "All of the above"],
     "answer": "All of the above"},

    {"question": "What does CPU stand for?",
     "options": ["Central Processing Unit", "Central Programming Unit", "Computer Personal Unit", "Central Power Unit"],
     "answer": "Central Processing Unit"},

    {"question": "Which company developed Windows?",
     "options": ["Apple", "Google", "Microsoft", "IBM"],
     "answer": "Microsoft"},

    {"question": "Which one is a Python web framework?",
     "options": ["Django", "React", "Angular", "Vue"],
     "answer": "Django"},
]

# ---------- Quiz App ----------
class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App 🧠")
        self.root.geometry("600x400")
        self.root.config(bg="#f2f2f2")

        self.q_no = 0
        self.score = 0

        self.question_label = tk.Label(root, text="", font=("Helvetica", 16, "bold"),
                                       bg="#f2f2f2", wraplength=500)
        self.question_label.pack(pady=20)

        self.var = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            btn = tk.Radiobutton(root, text="", variable=self.var, value="",
                                 font=("Helvetica", 12), bg="#f2f2f2", anchor="w")
            btn.pack(fill="x", padx=50, pady=5)
            self.option_buttons.append(btn)

        self.next_btn = tk.Button(root, text="Next ➜", command=self.next_question,
                                  bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"), width=10)
        self.next_btn.pack(pady=10)

        self.restart_btn = tk.Button(root, text="🔄 Restart", command=self.restart_quiz,
                                     bg="#2196F3", fg="white", font=("Helvetica", 12, "bold"), width=10)
        self.restart_btn.pack(pady=10)
        self.restart_btn.config(state="disabled")

        self.display_question()

    # ---------- Display Current Question ----------
    def display_question(self):
        question_data = quiz_data[self.q_no]
        self.question_label.config(text=f"Q{self.q_no + 1}. {question_data['question']}")
        self.var.set(None)
        for i, opt in enumerate(question_data["options"]):
            self.option_buttons[i].config(text=opt, value=opt)

    # ---------- Move to Next Question ----------
    def next_question(self):
        selected = self.var.get()
        if not selected:
            messagebox.showwarning("Select an answer", "Please select an option before proceeding!")
            return

        if selected == quiz_data[self.q_no]["answer"]:
            self.score += 1

        self.q_no += 1

        if self.q_no < len(quiz_data):
            self.display_question()
        else:
            self.show_result()

    # ---------- Show Final Result ----------
    def show_result(self):
        messagebox.showinfo("Quiz Completed 🎉",
                            f"Your Score: {self.score}/{len(quiz_data)}\n\nClick 'Restart' to play again!")
        self.next_btn.config(state="disabled")
        self.restart_btn.config(state="normal")

    # ---------- Restart Quiz ----------
    def restart_quiz(self):
        self.q_no = 0
        self.score = 0
        self.next_btn.config(state="normal")
        self.restart_btn.config(state="disabled")
        self.display_question()


# ---------- Run App ----------
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()
