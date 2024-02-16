#!/usr/bin/python3
"""
    script that reads stdin line by line and computes metrics
"""
import sys


def print_msg(codes, file_size):
    print("File size: {}".format(file_size))
    for key, val in sorted(codes.items()):
        if val != 0:
            print("{}: {}".format(key, val))


file_size = 0
code = 0
count_lines = 0
codes = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

try:
    for line in sys.stdin:
        parsed_line = line.split()
        parsed_line = parsed_line[::-1]

        if len(parsed_line) > 2:
            count_lines += 1

            if count_lines <= 10:
                file_size += int(parsed_line[0])
                code = parsed_line[1]

                if (code in codes.keys()):
                    codes[code] += 1

            if (count_lines == 10):
                print_msg(codes, file_size)
                count_lines = 0

finally:
    print_msg(codes, file_size)

# #!/usr/bin/python3
# """
#     script that reads stdin line by line and computes metrics
# """
# import sys
# import re


# def computes_metric():
#     """Function that reads stdin line by line and computes metrics"""

#     pattern = (
#         r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) "
#         r"\- \[\d{4}\-\d{2}\-\d{2} \d{2}\:\d{2}\:\d{2}\.\d{6}\] "
#         r"\"GET /projects/260 HTTP/1\.1\" "
#         r"(200|301|400|401|403|404|405|500) "
#         r"(\d{0,10})\s"
#     )

#     logs = {
#         'File size': 0,
#         '200': 0,
#         '301': 0,
#         '400': 0,
#         '401': 0,
#         '403': 0,
#         '404': 0,
#         '405': 0,
#         '500': 0
#         }

#     try:
#         counter = 0
#         for line in sys.stdin:
#             match = re.fullmatch(pattern, line)
#             counter += 1
#             status_code = match.group(2)
#             size = int(match.group(3))
#             logs[status_code] += 1
#             logs['File size'] += size

#             if counter % 10 == 0:

#                 for key, value in logs.items():
#                     if logs[key] > 0:
#                         print(f"{key}: {value}")
#                         if key != 'File size':
#                             logs[key] = 0

#     except KeyboardInterrupt:
#         for key, value in logs.items():
#             if logs[key] > 0:
#                 print(f"{key}: {value}")
#                 if key != 'File size':
#                     logs[key] = 0


# if __name__ == '__main__':
#     computes_metric()
