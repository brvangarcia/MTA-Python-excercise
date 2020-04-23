import os

filename = "/Users/bryan/Documents/Dev/Python/Chapter 3/cities.txt"


if os.path.exists(filename):
    file_to_open = open(filename, 'r')
    print(file_to_open.read())
    file_to_open.close()
else:
    print(f"{filename} does not exist.")