#!/usr/bin/python3
"""
Determines the minimum number of coins needed to meet a
given amount using available coin denominations.
"""


def makeChange(coins, total):
    """
    This function determines the fewest number of coins
    needed to meet a given amount.

    Args:
        coins: A list of coin denominations (integers greater than 0)
        total: The target amount to reach (integer).

    Returns:
        The fewest number of coins needed to meet the total,
        or -1 if it's impossible.
    """

    # Base cases:
    if total < 0:
        return 0

    # Initialize a table to store minimum coin counts for subproblems
    dp = [float('inf')] * (total + 1)
    # Initialize with infinity (largest possible value)
    dp[0] = 0  # 0 amount requires 0 coins

    # Iterate through coins and subproblems
    for coin in coins:
        for amount in range(coin, total + 1):
            # Check if current coin can be used and update minimum count
            if amount >= coin:
                dp[amount] = min(dp[amount], dp[amount - coin] + 1)

    # Return minimum coin count for the target amount
    return dp[total] if dp[total] != float('inf') else -1
    # Check for unreachable total
