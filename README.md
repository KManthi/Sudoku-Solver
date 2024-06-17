# SUDOKU SOLVER
This is a CLI-based Sudoku solver written in Python.

It takes an unsolved Sudoku grid as input, where empty cells are represented by zeros, and outputs the solved grid.

## Setting Up
1. Fork and clone this repository.
2. Navigate to the project directory in your terminal.
3. Run the following command:
   ```bash
   python3 src/sudoku.py
4. Enter your unsolved Sudoku grid. Use spaces to separate numbers for each row. Use 0 to represent empty cells. Here's an example grid:<br>

    0 0 0 0 3 0 0 8 0 <br>
    0 4 9 7 0 0 0 0 0 <br>
    3 5 0 1 0 0 0 0 9 <br>
    0 0 0 0 0 0 0 2 6 <br>
    0 0 0 0 0 0 7 9 0 <br>
    0 0 0 5 2 0 0 0 8 <br>
    0 1 0 0 0 0 0 0 4 <br>
    0 0 5 2 0 0 0 0 0 <br>
    0 6 8 0 0 4 0 3 0 <br>

5. Each vertical line represents a column while each horizontal line represents a row.

6. Squares of three represent the 3x3 grid. From the above example, the top 3x3 (left, centre, right ) would be represented like this in a typical Sudoku board: <br>
    0 0 0| 0 3 0 |0 8 0 <br>
    0 4 9| 7 0 0 |0 0 0 <br>
    3 5 0| 1 0 0 |0 0 9 <br>
    
---

## Technologies used
Python version 3.8

