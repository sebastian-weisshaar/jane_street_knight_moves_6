# 🏰 Solving Jane Street Puzzle: Knight Moves 6 
## 🗓️ October 2024

Hi! 👋 Welcome to my solution for the Jane Street Puzzle of October 2024. You can find the original puzzle [here](https://www.janestreet.com/puzzles/knight-moves-6-index/). ♟️

<details><summary> 📜 Problem Description</summary>

### 🎯 Objective
Pick distinct positive integers A, B, and C, and place them in the grid. Create two corner-to-corner trips that each score exactly 2024 points.

### 🐴 Rules
- Trips use knight's moves
- No square revisits allowed
- Two required trips: a1 to f6, and a6 to f1

### 🧮 Scoring
1. Start with A points
2. For each move:
   - Between different integers: Multiply score by destination value
   - Within same integer: Add destination value to score

### 🏆 Challenge
Find A, B, C, and trips that meet the criteria. Minimize A + B + C.

### 📝 Submission Format
`A,B,C,a1-to-f6-tour,a6-to-f1-tour`  
Example: `1,2,253,a1,b3,c5,d3,f4,d5,f6,a6,c5,a4,b2,c4,d2,f1`

### 🏅 Leaderboard Qualification
A + B + C must be less than 50.

</details>

## 💡 Solution Approach

My approach to solving the puzzle is the following:

1. **Strictly Increasing Score**: The score of each trip is strictly increasing due to the positive integer values of A, B, C, and the scoring rules.

2. **Early Termination**: We can immediately disqualify a solution if the score exceeds 2024. 

3. **Backtracking Algorithm**: We employ a backtracking algorithm to explore different knight moves, stepping back when a path exceeds 2024 points.

### 🔍 Functions

1. `calculate_new_score(current_score, current_value, next_value)`:
   - Calculates the new score based on the current score and the values of the current and next squares.
   - Implements the scoring rules: multiply if the knight jumps into a different zone, add if it's the same.

2. `find_path(row, col, score, visited, path, target, board)`:
   - Implements a recursive backtracking algorithm to find a valid knight's path.
   - Terminates early if the score exceeds 2024 or if the square has been visited.
   - Returns the path if found, otherwise None.

3. `check_numbers(A, B, C, start, end)`:
   - Creates a board with given A, B, C values and checks for a valid path between start and end points.
   - Initializes the search with the starting score and position.
   - Returns the path in chess notation if a valid path is found, None otherwise.

4. `check_solutions(A, B, C)`:
   - Verifies if both required paths (a1 to f6 and a6 to f1) are valid for given A, B, C values.
   - Prints the solutions if found.
   - Returns True if both paths are valid, False otherwise.

5. `main()`:
   - Handles command-line arguments for A, B, and C.
   - Calls `check_solutions` with the provided values.

### 📝 Note

A, B, C are non-commutative, so we need to check all permutations. For instance, while (1, 2, 253) is a valid solution, (253, 1, 2) is not.

### 🎉 Results

After testing different combinations, I found one optimal solution:

- A = 3
- B = 2
- C = 1

This results in a sum of 6, which is the lowest possible value for A + B + C.

The paths for both knight's tours are:

1. From a1 to f6:
   `a1,b3,a5,c6,e5,c4,b6,d5,f4,e6,c5,a6,b4,a2,c1,e2,d4,b5,d6,f5,e3,f1,d2,f3,e1,d3,f2,e4,f6`

2. From a6 to f1:
   `a6,c5,e6,d4,c6,a5,c4,e5,d3,b4,d5,f4,e2,c3,e4,d2,f1`

### 🖥️ Running the Code
If you want to run the code, you can clone the repo and run `python src/main.py <A> <B> <C>`.
The code will check whether your choice of A, B, C is valid and if so return the two paths.

Happy puzzling! 🧩

Sebastian
