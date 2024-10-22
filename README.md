# 🏰 Solving Jane Street Puzzle: Knight Moves 6 
## 🗓️ October 2024

Hi! 👋 Welcome to my solution for the Jane Street Puzzle of October 2024. You can find the original puzzle [here](https://www.janestreet.com/puzzles/knight-moves-6-index/). ♟️

<details><summary> 📜  Problem Description</summary>

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

I used the following properties to solve the problem:

1. **Strictly Increasing Score**: The score of each trip is strictly increasing due to the positive integer values of A, B, C, and the scoring rules.

2. **Early Termination**: We can immediately disqualify a solution if the score exceeds 2024, allowing for efficient pruning of the search space.

3. **Backtracking Algorithm**: We employ a backtracking algorithm to explore different knight moves, stepping back when a path exceeds 2024 points.

### 🔍 Key Functions

1. `find_path(row, col, score, visited, path, target, board)`:
   - Implements a recursive backtracking algorithm to find a valid knight's path.
   - Returns the path if found, otherwise None.

2. `check_numbers(A, B, C, start, end)`:
   - Creates a board with given A, B, C values and checks for a valid path between start and end points.
   - Returns True if a valid path is found, False otherwise.

3. `check_solutions(A, B, C)`:
   - Verifies if both required paths (a1 to f6 and a6 to f1) are valid for given A, B, C values.
   - Returns True if both paths are valid, False otherwise.

4. `calculate_new_score(current_score, current_value, next_value)`:
   - Calculates the new score based on the current score and the values of the current and next squares.

### 🧠 Algorithm Overview

1. Implement a recursive backtracking function (`find_path`) to explore possible knight moves.
2. Use `check_numbers` to validate paths for specific start and end points.
3. Employ `check_solutions` to verify both required paths for given A, B, C values.
4. Maintain a set of visited squares to prevent revisits.
5. Store the current path to return the solution if found.
6. Use `calculate_new_score` to update the score according to the puzzle rules.

### 🚀 Optimization Note

The non-commutativity of A, B, C necessitates checking all permutations. For instance, while (1, 2, 253) is a valid solution, (253, 1, 2) is not.

### 🎉 Results

After testing different combinations, I found one optimal solution:

- A = 3
- B = 2
- C = 1

This results in a sum of 6, which is the lowest possible value for A + B + C.

The paths for both required knight's tours are:

1. From a1 to f6:
   `a1,b3,a5,c6,e5,c4,b6,d5,f4,e6,c5,a6,b4,a2,c1,e2,d4,b5,d6,f5,e3,f1,d2,f3,e1,d3,f2,e4,f6`

2. From a6 to f1:
   `a6,c5,e6,d4,c6,a5,c4,e5,d3,b4,d5,f4,e2,c3,e4,d2,f1`

### 🖥️ Running the Code
If you want to run the code yourself, you can do so by cloning the repo and running `python jane_street_oct_22/main.py <A> <B> <C>`.

Happy puzzling! 🧩

Sebastian
