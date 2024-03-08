#!/usr/bin/python3
"""UTF8 validator
"""


def validUTF8(data):
    """Determine if a given data set represents a valid UTF-8 encoding."""
    bytes_to_follow = 0

    for byte in data:
        mask = 1 << 7
        if bytes_to_follow == 0:
            while byte & mask:
                bytes_to_follow += 1
                mask >>= 1
            if bytes_to_follow == 0:
                continue

            elif bytes_to_follow == 1 or bytes_to_follow > 4:
                return False
        else:
            if not (byte & (1 << 7) and not (byte & (1 << 6))):
                return False
        bytes_to_follow -= 1

    return bytes_to_follow == 0
