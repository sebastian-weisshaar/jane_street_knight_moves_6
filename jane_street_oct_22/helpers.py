def create_board(A: int, B: int, C: int) -> list[list[int]]:
    # Define the board as a list of lists
    # 'A' -> A, 'B' -> B, 'C' -> C
    board = [
        [A, B, B, C, C, C],
        [A, B, B, C, C, C],
        [A, A, B, B, C, C],
        [A, A, B, B, C, C],
        [A, A, A, B, B, C],
        [A, A, A, B, B, C],
    ]
    return board


def get_knight_moves() -> list[tuple[int, int]]:
    # Define all possible knight moves
    knight_moves = [
        (-2, -1),
        (-2, 1),
        (-1, -2),
        (-1, 2),
        (1, -2),
        (1, 2),
        (2, -1),
        (2, 1),
    ]
    return knight_moves
