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
    unboxed = [0]

    for box in unboxed:
        for key in boxes[box]:
            if key not in unboxed and key < len(boxes):
                unboxed.append(key)
            if len(unboxed) == len(boxes):
                return True
    return False
