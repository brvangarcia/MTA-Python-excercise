file_to_open = open('/Users/bryan/Documents/Dev/Python/Chapter 3/cities.txt', 'r')
msg = ''
for line in file_to_open:
    if line == 'Bayamon\n':
        continue
    msg = msg + line
print(msg)
file_to_open.close()