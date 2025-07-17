import tkinter as tk
import tkinter.scrolledtext as scrolledtext
import io
import sys
from main_game import snake

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Quiz")
        self.geometry("800x600")
        self.configure(bg='#00A0A0')

        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, PageOne, PageTwo):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

        self.score = 0

    def show_frame(self, c):
        frame = self.frames[c]
        frame.tkraise()

class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#00A0A0')
        self.controller = controller
        self.questions = [
            {
                "question": "Question 1: What is Python primarily known for?",
                "options": [
                    "A. Handling databases",
                    "B. Data visualization",
                    "C. High-level programming language",
                    "D. Playing games"
                ],
                "correct_option": "C. High-level programming language"
            },
            {
                "question": "Question 2: Which of the following is a valid Python comment?",
                "options": [
                    "A. # This is a comment",
                    "B. /* This is a comment */",
                    "C. <!-- This is a comment -->",
                    "D. comment(This is a comment)"
                ],
                "correct_option": "A. # This is a comment"
            },
            {
                "question": "Question 3: What does the print() function do in Python?",
                "options": [
                    "A. Calculate mathematical expressions",
                    "B. Play audio files",
                    "C. Display text and variables",
                    "D. Generate random numbers"
                ],
                "correct_option": "C. Display text and variables"
            }
        ]
        self.current_question = 0

        self.label = tk.Label(self, text=self.questions[self.current_question]["question"], font=("Helvetica", 20), bg='#00A0A0', fg='white')
        self.label.pack(pady=20)

        self.selected_option = tk.StringVar()
        self.radio_buttons = []
        for i, option in enumerate(self.questions[self.current_question]["options"]):
            radio_button = tk.Radiobutton(self, text=option, font=("Helvetica", 16), variable=self.selected_option, value=option, bg='#00A0A0', fg='white')
            radio_button.pack(anchor='w')
            self.radio_buttons.append(radio_button)

        check_button = tk.Button(self, text="Check Answer", command=self.check_answer, width=15, height=2, bg='#005050', fg='white')
        check_button.pack(pady=10)

        self.score_label = tk.Label(self, text="Score: 0", font=("Helvetica", 16), bg='#00A0A0', fg='white')
        self.score_label.pack(pady=20)

    def check_answer(self):
        selected_option = self.selected_option.get()
        correct_option = self.questions[self.current_question]["correct_option"]
        if selected_option == correct_option:
            self.controller.score += 1  # Update the score
            self.score_label.config(text=f"Score: {self.controller.score}")  # Update the score label
            print("Correct!")
        else:
            print("Incorrect. The correct answer is:", correct_option)

        self.current_question += 1
        if self.current_question < len(self.questions):
            self.label.config(text=self.questions[self.current_question]["question"])
            self.selected_option.set("")

            question_options = self.questions[self.current_question]["options"]
            for i in range(len(self.radio_buttons)):
                self.radio_buttons[i].config(text=question_options[i])

        else:
            self.label.config(text="Quiz Complete!")
            self.score_label.config(text=f"Score: {self.controller.score}")
            if self.current_question == 3:
                print("You answered all questions. Total score:", self.controller.score)
            else:
                print("You answered", self.current_question, "questions.")
            self.after(0000, lambda: self.controller.show_frame(PageOne))

class PageOne(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#00A0A0')
        self.controller = controller

        content_block = tk.Label(self, bg='#007070', fg='white')
        content_block.pack(pady=20, fill='both', expand=True)

        label = tk.Label(content_block, text="QUESTION", font=("Helvetica", 20), bg='#007070', fg='white')
        label.pack(pady=10)

        question_label = tk.Label(content_block, text=" HOW TO USE PRINT FUNCTION IN PYTHON", font=("Helvetica", 24), bg='#007070', fg='white')
        question_label.pack(pady=10)

        comment_text = """      
                     The print function in Python is used to display or output information to the console or terminal. 
                     It allows you to show messages, values, or variables to the user or programmer for various purposes,
                     such as debugging, providing information, or interacting with the user..

                              SYNTAX

                               print("write  any statement which you want to print")

                        """

        comment_box = tk.Label(content_block, text=comment_text, font=("Helvetica", 12), justify='left', anchor='w', bg='#007070', fg='white')
        comment_box.pack(pady=10)

        button_frame = tk.Frame(content_block)
        button_frame.pack(pady=20)

        video_button = tk.Button(button_frame, text="Play Video", command=self.play_video, width=15, height=2, bg='#005050', fg='white')
        visit_button = tk.Button(button_frame, text="Next", command=lambda: controller.show_frame(PageTwo), width=15, height=2, bg='#005050', fg='white')
        go_back_button = tk.Button(button_frame, text="Go back to start page", command=lambda: controller.show_frame(StartPage), width=15, height=2, bg='#005050', fg='white')

        video_button.grid(row=0, column=0, padx=10)
        visit_button.grid(row=0, column=1, padx=10)
        go_back_button.grid(row=0, column=2, padx=10)

    def play_video(self):
        print("Video button clicked. Play the video here.")

class PageTwo(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent, bg='#00A0A0')
        self.controller = controller

        label = tk.Label(self, text="Print your name using print function ", font=("Helvetica", 20), bg='#00A0A0', fg='white')
        label.pack(pady=20)

        self.text_editor = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=60, height=10, bg='#007070', fg='white')
        self.text_editor.pack(padx=10, pady=10)

        run_button = tk.Button(self, text="Run Code", command=self.run_python_code, width=15, height=2, bg='#005050', fg='white')
        run_button.pack(pady=10)

        self.output_text = scrolledtext.ScrolledText(self, wrap=tk.WORD, width=60, height=10, bg='#007070', fg='white')
        self.output_text.pack(padx=10, pady=10)

        finish_button = tk.Button(self, text="Finish", command=self.finish_page_two, width=15, height=2, bg='#005050', fg='white')
        finish_button.pack(pady=10)

        button_frame = tk.Frame(self)
        button_frame.pack(pady=20)
        go_back_button = tk.Button(button_frame, text="Go back to start page", command=lambda: controller.show_frame(StartPage), width=15, height=2, bg='#005050', fg='white')
        go_back_button.grid(row=0, column=0, padx=10)

    def run_python_code(self):
        code = self.text_editor.get("1.0", "end-1c")
        stdout_backup = sys.stdout
        sys.stdout = io.StringIO()
        sys.stderr = sys.stdout

        try:
            exec(code)
        except Exception as e:
            print("Error:", e)
        finally:
            output = sys.stdout.getvalue()
            sys.stdout = stdout_backup

        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.INSERT, "Output:\n" + output)

    def finish_page_two(self):
        self.text_editor.delete("1.0", tk.END)
        self.output_text.delete("1.0", tk.END)
        print("Finished using Page Two")

        # Continue the game by calling the snake function with continue_game=True
        snake(3, continue_game=True)  # Continue from the third game block

if __name__ == "__main__":
    app = App()
    app.mainloop()
