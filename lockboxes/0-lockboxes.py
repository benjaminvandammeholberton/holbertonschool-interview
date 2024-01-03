#!/usr/bin/python3

"""
Module: unlock_boxes

This module provides a function to determine if all the boxes can be opened.
"""

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
    - boxes (List[List[int]]): A list of lists where each sublist represents a box and contains keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    # Set to keep track of opened boxes
    opened_boxes = set()

    # Function to perform depth-first search
    def dfs(box_index, visited):
        """
        Perform depth-first search starting from the given box.

        Args:
        - box_index (int): Index of the current box.
        - visited (set): Set of boxes that have been visited.

        Returns:
        - None
        """
        # Mark the current box as visited
        visited.add(box_index)

        # Check the keys in the current box
        keys = boxes[box_index]

        # Explore each key in the current box
        for key in keys:
            # If the key opens a box that hasn't been visited yet, recursively explore that box
            if key < len(boxes) and key not in visited:
                dfs(key, visited)

    # Update the call to DFS in the main function
    dfs(0, set())

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
