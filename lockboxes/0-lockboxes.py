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
    list_keys = [0]
    for i in list_keys:
        for j in boxes[i]:
            if j < len(boxes) and j not in list_keys:
                list_keys.append(j)
        if len(list_keys) == len(boxes):
            return True
    return False
