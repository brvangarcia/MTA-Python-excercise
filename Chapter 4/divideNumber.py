def divideNumber(n1,n2):
    """ Python Program """
    try: #In the tru statement
        result = float(n1) / float(n2)
    except ZeroDivisionError:
        print('n2 cannot be zero')
        result = 'N/A'
    except ValueError:
        print('numbers cannot be strings!')
        result = 'N/A'
    else:
        print(f'{n1} and {n2} are numerical values!')
    return result

n1 = input('Enter first number: ')
n2 = input('Enter second number: ')

print(f'{n1} / {n2} = {divideNumber(n1,n2)}')