employee = 'Bryan Garcia'
months_as_employee = -99
new_employee = False

msg = 'Hi, ' + employee + '!'
if months_as_employee < 0:
    print('Hi, ', employee, '\n Error in moths')

elif months_as_employee < 3 :
    new_employee = True
    if new_employee:
        print(msg + ' Welcome to the company!')
elif months_as_employee == 3:
    new_employee = False    
    print(msg + "You've been here for 3 months!")
else:
    print(msg)