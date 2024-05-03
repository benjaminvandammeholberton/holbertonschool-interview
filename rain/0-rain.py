#!/usr/bin/python3
"""
Rain
"""


def rain(walls):
    """Calculates how much rainwater is retained after raining"""
    if not walls or len(walls) < 3:
        return 0

    total_water = 0
    left_max = [0] * len(walls)
    right_max = [0] * len(walls)

    left_max[0] = walls[0]
    for i in range(1, len(walls)):
        left_max[i] = max(left_max[i - 1], walls[i])

    right_max[len(walls) - 1] = walls[len(walls) - 1]
    for i in range(len(walls) - 2, -1, -1):
        right_max[i] = max(right_max[i + 1], walls[i])

    for i in range(len(walls)):
        total_water += min(left_max[i], right_max[i]) - walls[i]

    return total_water
