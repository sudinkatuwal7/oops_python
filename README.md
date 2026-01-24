# 🐍 OOPS_Python — Snake Game (Learning Project)

A beginner-friendly **Snake game built in Python using the `turtle` module**, designed to practice and understand **Object-Oriented Programming (OOP)** concepts.

This repository represents a **learning process**, including rough code snippets, experiments, and refactoring while building the classic Snake game step by step.

---

## 📌 Project Overview

This project demonstrates how a simple procedural Snake game can be structured using **classes and objects**.  
The logic is separated into multiple files to improve readability, reusability, and maintainability.

The focus of this repository is **learning**, not perfection.

---

## 🧠 Key Concepts Practiced

- Object-Oriented Programming (classes, objects, methods)
- File separation (`main.py` and `snake.py`)
- Turtle graphics and screen control
- Keyboard event handling
- Game loops and animation timing
- Preventing invalid snake movement (reverse direction)

---

## 📁 Project Structure

```bash
oops_python/
│
├── main.py # Main game loop and screen setup
├── snake.py # Snake class and movement logic
├── README.md # Project documentation
```

---

## ▶️ How the Game Works

- A game window opens using the `turtle` screen
- The snake starts with three segments
- Arrow keys control the snake’s direction
- The snake moves continuously using a game loop
- Movement is handled by shifting segments forward from tail to head

---

## 🎮 Controls

| Key | Action |
|---|---|
| ⬆️ Up Arrow | Move Up |
| ⬇️ Down Arrow | Move Down |
| ⬅️ Left Arrow | Move Left |
| ➡️ Right Arrow | Move Right |

The snake is prevented from reversing directly into itself.

---

## 🧩 Code Design (OOP)

### `Snake` Class (`snake.py`)
```Responsibilities:```
- Creating the initial snake body
- Managing movement of each segment
- Handling direction changes safely

```Key attributes:```
- `segments`: list of turtle segments
- `head`: reference to the first segment

```Key methods:```
- `create_snake()`
- `move()`
- `up()`, `down()`, `left()`, `right()`

---

## 🚧 Current Status

✅ Snake movement  
✅ Keyboard controls  
✅ OOP-based structure  

## 🚧 Upcoming features:
- Food and snake growth
- Scoreboard
- Wall collision detection
- Self-collision detection
- Game over screen

---

## 🎓 Learning Note

This repository intentionally includes **rough code snippets and commented experiments** to document the learning journey.  
Refactoring and improvements are part of the process.

---

## 🛠️ Requirements

- Python 3.x  
- No external libraries required (uses built-in `turtle` module)

---

## 🚀 How to Run

```bash
python main.py
```
---
## 📌 Author
Sudin Katuwal

Learning Python, OOP, and building projects one step at a time.

