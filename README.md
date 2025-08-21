# Sudoku Solver

> written by AI

A Python implementation of a Sudoku solver using backtracking algorithm. This project demonstrates how to solve Sudoku puzzles efficiently with a recursive backtracking approach.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Algorithm Explanation](#algorithm-explanation)
- [Installation](#installation)
- [Usage](#usage)
- [Code Structure](#code-structure)
- [Example](#example)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Sudoku solver is built using Python and implements the backtracking algorithm to efficiently solve 9x9 Sudoku puzzles. The backtracking algorithm is particularly suitable for Sudoku solving as it explores all possible values for empty cells while adhering to Sudoku rules, backtracking when a dead end is reached.

## Features

- Solve any valid 9x9 Sudoku puzzle
- Clear and concise implementation
- Visualization of the solved puzzle with proper formatting
- Efficient backtracking algorithm
- Well-documented code

## Algorithm Explanation

The solver uses a backtracking algorithm with the following steps:

1. **Find an empty cell** in the Sudoku grid (represented by 0)
2. **Try numbers 1 through 9** in that cell
3. **Check if the number is valid** according to Sudoku rules (no duplicates in the same row, column, or 3x3 subgrid)
4. If valid, **recursively attempt to solve** the rest of the puzzle with this number in place
5. If the recursive attempt fails (dead end), **backtrack** by resetting the cell to 0 and trying the next number
6. If all numbers 1-9 have been tried without success, return false to indicate no solution exists
7. If all cells are filled correctly, return true to indicate the puzzle has been solved

## Installation

1. Ensure you have Python 3.x installed on your system
2. Clone this repository:

```bash
git clone https://github.com/JonathanSssst/SudokuSolver.git
cd sudoku-solver
```

No additional dependencies are required as the implementation uses only Python's standard library.

## Usage

1. Open the `main.py` file
2. Modify the `sudoku` matrix at the top of the file to represent your puzzle (use 0 for empty cells)
3. Run the script:
   
```bash
python main.py
```

4. The solution will be printed to the console, or a message will indicate if no solution exists

## Code Structure

- **main.py**: Contains the complete implementation of the Sudoku solver
  - `sudoku`: A 9x9 matrix representing the Sudoku puzzle
  - `print_sudoku()`: Formats and prints the Sudoku grid
  - `is_valid()`: Checks if a number can be placed in a specific cell
  - `solve()`: Implements the backtracking algorithm to solve the puzzle
  - Main execution code to solve and print the result

- **blog.md**: A detailed explanation of the backtracking algorithm and implementation (in Chinese)

## Example

Here's an example of a Sudoku puzzle and its solution:

### Input Puzzle
```
0 0 0 9 0 0 0 7 1
9 0 0 0 0 3 0 5 0
0 2 5 0 4 0 0 0 0
5 0 0 0 0 0 1 6 0
0 4 0 8 0 1 0 0 0
0 0 6 5 0 0 0 0 0
0 0 7 0 9 2 6 0 0
2 9 8 0 5 0 0 0 0
0 0 0 0 0 0 2 0 9
```

### Solution
```
3 6 4 | 9 2 5 | 8 7 1
9 7 1 | 6 8 3 | 4 5 2
8 2 5 | 7 4 1 | 9 3 6
- - - - - - - - - - - -
5 3 2 | 4 7 9 | 1 6 8
7 4 9 | 8 6 1 | 5 2 3
1 8 6 | 5 3 2 | 7 9 4
- - - - - - - - - - - -
4 5 7 | 1 9 2 | 6 8 3
2 9 8 | 3 5 6 | 7 1 4
6 1 3 | 7 8 4 | 2 9 5
```

## Contributing

Contributions are welcome! If you have any suggestions for improvements or find any issues, please feel free to create an issue or submit a pull request.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
