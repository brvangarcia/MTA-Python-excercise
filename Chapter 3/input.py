print("---Simple Sum Program---")
print("Enter 'q' to exit program")
while True:
    number1 = input("\nFirst Number: ")
    if number1 == 'q':
        break
    number2 = input("Second Number: ")
    if number2 == 'q':
        break
    result = int(number1) + int(number2)
    print(number1, "+", number2,"=",result)