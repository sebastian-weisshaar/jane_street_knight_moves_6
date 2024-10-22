from helpers import create_board, get_knight_moves
import sys

def calculate_new_score(current_score: int, current_value: int, next_value: int) -> int:
    return current_score * next_value if current_value != next_value else current_score + next_value

def find_path(
    row: int,
    col: int,
    score: int,
    visited: set[tuple[int, int]],
    path: list[tuple[int, int]],
    target: tuple[int, int],
    board: list[list[int]],
) -> list[tuple[int, int]] | None:
    if score > 2024 or (row, col) in visited:
        return None

    if (row, col) == target and score == 2024:
        return path

    visited.add((row, col))
    
    for d_row, d_col in get_knight_moves():
        new_row, new_col = row + d_row, col + d_col
        if 0 <= new_row < 6 and 0 <= new_col < 6:
            new_score = calculate_new_score(score, board[row][col], board[new_row][new_col])
            result = find_path(
                new_row,
                new_col,
                new_score,
                visited,
                path + [(new_row, new_col)],
                target,
                board,
            )
            if result:
                return result

    visited.remove((row, col))
    return None

def check_numbers(A: int, B: int, C: int, start: tuple[int, int], end: tuple[int, int]):
    board = create_board(A, B, C)

    initial_score = board[start[0]][start[1]]
    result_path = find_path(
        start[0],
        start[1],
        initial_score,
        set(),
        [start],
        end,
        board,
    )

    if result_path:
        path_in_chess_notation = [
            chr(y + ord("a")) + str(6 - x) for x, y in result_path
        ]
        return ",".join(path_in_chess_notation)
    else:
        print("No valid path found.")
        return None
    
def check_solutions(A: int, B: int, C: int):
    a1, f6 = (5, 0), (0, 5)
    a6, f1 = (0, 0), (5, 5)
    first_solution = check_numbers(A, B, C, a1, f6)
    second_solution = check_numbers(A, B, C, a6, f1)
    print(f"Solution a1 to f6: {first_solution}")
    print(f"Solution a6 to f1: {second_solution}")
    if first_solution and second_solution:
        print(f"Jane Street solution: {A},{B},{C},{first_solution},{second_solution}")
    else:
        print("No solutions found.")
    return first_solution and second_solution

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <A> <B> <C>")
        sys.exit(1)
    
    try:
        A = int(sys.argv[1])
        B = int(sys.argv[2])
        C = int(sys.argv[3])
    except ValueError:
        print("Error: A, B, and C must be integers")
        sys.exit(1)

    check_solutions(A, B, C)

if __name__ == "__main__":
    main()
