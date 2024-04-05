#!/usr/bin/python3
import sys


def is_safe(x_new, y_new, queens_positions):
    """
    Checks if a new queen can be safely placed at position (x_new, y_new)
    relative to the queens already placed on the chessboard.

    Args:
        x_new (int): x-coordinate of the new queen.
        y_new (int): y-coordinate of the new queen.
        queens_positions (list): List of tuples containing
        coordinates of queens already placed.

    Returns:
        bool: True if the new queen can be safely placed,
        False otherwise.
    """
    for queen_x, queen_y in queens_positions:
        if queen_x == x_new or queen_y == y_new:
            return False
        if abs(queen_x - x_new) == abs(queen_y - y_new):
            return False
    return True


def solve_nqueens(N, queens_positions, row=0, solutions=[]):
    """
   Solves the N-queens problem on a chessboard of size N x N.

    Args:
        N (int): Size of the chessboard and the number of queens to place.
        queens_positions (list): List of tuples containing
        coordinates of queens already placed.
        row (int): Current row of the chessboard where to place the next queen.
        solutions (list): List to store valid solutions.

    Returns:
        list: List of all valid solutions.
    """
    if row == N:
        solutions.append(queens_positions.copy())
    else:
        for col in range(N):
            if is_safe(row, col, queens_positions):
                queens_positions.append([row, col])
                solve_nqueens(N, queens_positions, row + 1, solutions)
                queens_positions.pop()
    return solutions


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        if N < 4:
            print("N must be at least 4")
            sys.exit(1)
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solutions = solve_nqueens(N, [])
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    main()
