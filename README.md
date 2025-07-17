# 🐍 PayGuru – Python Learning Through Snake Game

**PayGuru** is a game-based Python learning application designed to make coding fun for students. It uses the classic **snake game** as a learning engine, integrating Python MCQs and live coding tasks into the gameplay.

---

## 🎮 How It Works

- The player controls a snake using the keyboard.
- As the snake collects special dots, the game:
  - Displays a **Python MCQ** and a **concept explanation**
  - Prompts a **coding question** based on the concept
  - Opens an embedded **Python terminal** for the user to code
- ✅ If the code runs correctly, the snake game **continues**
- ❌ If incorrect, the game **restarts from the beginning**

---

## ✨ Features

- 🎓 Learn Python while playing
- 📚 Step-by-step Python concept unlocking
- ❓ Multiple choice quizzes in-game
- 💻 Live Python code editor using `exec()`
- 🔁 Game reset on incorrect code execution
- 💡 Designed for beginners and schools

---

## 🛠 Tech Stack

- **Language**: Python
- **GUI/Game Engine**: `tkinter` or `pygame` (whichever you used)
- **Code Execution**: In-app using `exec()` or custom evaluator
- **No backend required** (fully offline)

---

## 📂 How to Run

1. Clone the repository:

```bash
git clone https://github.com/Darshan9922/payguru-learning-app.git
cd payguru-learning-app
