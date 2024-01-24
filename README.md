# Maze Solver

## Description

This Python application creates and solves a randomly generated maze. The maze is displayed graphically using a simple GUI. The maze generator uses a randomized depth-first search algorithm to create a unique maze each time, and the solver also uses a recursive depth-first search to find a path from the start to the finish.

## Features
- Random maze generation.
- Graphical display of maze creation and solving process.
- Recursive maze-solving algorithm.
- Customizable maze size and screen dimensions.

## Requirements
Python 3.x
Tkinter library (usually comes pre-installed with Python).

## Customization
You can customize the size of the maze, the dimensions of the screen, and the margin around the maze. These settings are found at the beginning of the `main()` function in `main.py`.

Example customization:
```python
num_rows = 12  # Number of rows in the maze
num_cols = 16  # Number of columns in the maze
margin = 50    # Margin around the maze
screen_x = 800 # Width of the window
screen_y = 600 # Height of the window
```