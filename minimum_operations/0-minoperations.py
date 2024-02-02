#!/usr/bin/python3
"""
This script defines a function minOperations that calculates\
the sum of prime factors of a given number.
"""


def minOperations(n):
    """
    Calculate the sum of prime factors of a given number.

    Parameters:
    - n (int): The input number

    Returns:
    - int: The sum of prime factors
    """
    if n <= 1:
        return 0
    # Set the minimum operation variable to 0
    min_operations = 0
    # Set the current length variable to 1 as we start with 1 character 'H'
    current_length = 1
    # Set the clipboard variable to 0 as we are not copying anything yet
    clipboard = 0

    # Loop until current length is equal to n
    while current_length < n:
        # If n is divisible by current length, we can copy all
        if n % current_length == 0:
            # This is the only time we can copy
            clipboard = current_length
            # Minimum operation is incremented by 1 because we copied
            min_operations += 1

        # Paste the clipboard
        current_length += clipboard
        # Minimum operation is incremented by 1 because we pasted
        min_operations += 1

    # Return minimum operation
    return min_operations
