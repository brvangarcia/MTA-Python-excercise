import os

file_to_modify = open('/Users/bryan/Documents/Dev/Python/Chapter 3/cities.txt', 'a')

new_city = input("Enter a new city: ")
file_to_modify.write('\n' + new_city)
print(new_city, "was added to file.")

file_to_modify.close()