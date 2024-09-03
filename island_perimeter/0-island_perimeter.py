#!/usr/bin/python3
"""
0-island perimeter
This module contains a function to calculate the perimeter of an island
represented in a grid.
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the grid.

    Parameters:
    grid (list of list of int): A rectangular grid where 0 represents water and
                                1 represents land. Each cell is square
                                with a side length of 1. Cells are
                                connected horizontally/vertically
                                (not diagonally). The grid is completely
                                surrounded by water.

    Returns:
    int: The perimeter of the island.
    """

    # Check if the grid is empty
    if not grid or not grid[0]:
        return 0

    # Get the number of rows and columns in the grid
    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    # Iterate over each cell in the grid
    for r in range(rows):
        for c in range(cols):
            # If the cell is land
            if grid[r][c] == 1:
                # Check all four directions

                # Check above the cell
                if r == 0 or grid[r - 1][c] == 0:
                    perimeter += 1

                # Check below the cell
                if r == rows - 1 or grid[r + 1][c] == 0:
                    perimeter += 1

                # Check to the left of the cell
                if c == 0 or grid[r][c - 1] == 0:
                    perimeter += 1

                # Check to the right of the cell
                if c == cols - 1 or grid[r][c + 1] == 0:
                    perimeter += 1

    return perimeter
