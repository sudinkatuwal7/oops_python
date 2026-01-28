# 🐍 OOPS_Python — Snake Game (Learning Project)

A beginner-friendly **Snake game built in Python using the `turtle` module**, designed to practice and understand **Object-Oriented Programming (OOP)** concepts.

This repository represents a **learning process**, including rough code snippets, experiments, and refactoring while building the classic Snake game step by step.

---

## 📌 Project Overview

This project demonstrates how a simple procedural Snake game can be structured using **classes and objects**.  
The logic is separated into multiple files to improve readability, reusability, and maintainability.

The focus of this repository is **learning**, not perfection.

---

## 🎮 Gameplay

### **Playing Game**

<img width="2560" height="1171" alt="Screenshot (170)" src="https://github.com/user-attachments/assets/f77536a2-51ac-43eb-8265-a0f9834a9e84" />

### **Game Over**

<img width="2560" height="1317" alt="Screenshot (171)" src="https://github.com/user-attachments/assets/c207d467-73e2-4500-beaa-b00589566c8d" />

---

## 🧠 Key Concepts Practiced

- Object-Oriented Programming (classes, objects, inheritance, methods)
- File separation (`main.py`, `snake.py`, `food.py`, `scoreboard.py`)
- Turtle graphics and screen control
- Keyboard event handling
- Game loops and animation timing
- Collision detection (walls, food, and tail)
- Score tracking and dynamic updates
- Preventing invalid snake movement (reverse direction)

---

## 📁 Project Structure

```bash
oops_python/
│
├── main.py         # Main game loop, input handling, and collision detection
├── snake.py        # Snake class with movement, direction, and growth logic
├── food.py         # Food class for spawning random collectible items
├── scoreboard.py   # Scoreboard class to track score and show game-over messages
├── README.md       # Project documentation
```

---

## ▶️ How the Game Works

- Opens a 600x600 black screen using Turtle graphics
- The snake starts with 3 segments
- Arrow keys control the snake’s direction
- Eating the red turtle grows the snake and increases the score
- Collision detection:
  - Hitting walls ends the game
  - Hitting the snake’s own tail ends the game
- The score is displayed at the top, updating whenever food is eaten
- The game ends with a game-over message when a collision occurs

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

## `Snake` Class (`snake.py`)

### Responsibilities
- Creating the initial snake body
- Managing movement of each segment
- Handling direction changes safely
- Extending the snake when food is eaten

### Key attributes
- `segments`: list of turtle segments
- `head`: reference to the first segment

### Key methods
- `create_snake()`
- `add_segment(position)`
- `extend()`
- `move()`
- `up()`, `down()`, `left()`, `right()`

---

## `Food` Class (`food.py`)

### Responsibilities
- Spawning food at random positions on the screen
- Refreshing location after the snake eats the food

### Key attributes
- `food`: turtle object representing the food

### Key methods
- `refresh()`

---

## `Scoreboard` Class (`scoreboard.py`)

### Responsibilities
- Tracking the player’s score
- Displaying the score at the top of the screen
- Showing a game-over message on collision

### Key attributes
- `score`: current player score
- `display`: turtle object for showing score

### Key methods
- `update_score()`
- `increase_score()`
- `game_over()`

---

## 🚧 Current Status

✅ Snake movement

✅ Keyboard controls

✅ Snake growth after eating food

✅ Food spawning

✅ Scoreboard updates

✅ Collision detection with walls and tail

## 🚧 Upcoming features:
- Add levels or increasing speed
- Add sound effects
- Customize snake and food appearance
- High-score tracking

---

## 🎓 Learning Note

This repository intentionally includes **rough code snippets and commented experiments** to document the learning journey.  
Refactoring, modular design, and problem-solving are key learning points.

---

## 🛠️ Requirements

- Python 3.6 or higher  
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

