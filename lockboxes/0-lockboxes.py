#!/usr/bin/python3

"""
Module: unlock_boxes

This module provides a function to determine if all the boxes can be opened.
"""


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
    - boxes (List[List[int]]): A list of lists where each sublist\
        represents a box and contains keys to other boxes.

    Returns:
    - bool: True if all boxes can be opened, else False.
    """
    # Set to keep track of opened boxes
    opened_boxes = set()

    # Function to perform depth-first search
    def dfs(box_index):
        """
        Perform depth-first search starting from the given box.

        Args:
        - box_index (int): Index of the current box.

        Returns:
        - None
        """
        # Mark the current box as opened
        opened_boxes.add(box_index)

        # Check the keys in the current box
        keys = boxes[box_index]

        # Explore each key in the current box
        for key in keys:
            # If the key opens a box that hasn't been opened yet,
            #recursively explore that box
            if key < len(boxes) and key not in opened_boxes:
                dfs(key)

    # Start the DFS from the first box (index 0)
    dfs(0)

    # Check if all boxes have been opened
    return len(opened_boxes) == len(boxes)
