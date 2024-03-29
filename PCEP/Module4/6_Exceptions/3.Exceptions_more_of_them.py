'''You can manage several Exceptions the next way:'''

try:
    user_number=int(input('Type a number: '))
    result=1/user_number
    print('The reciprocal of number:', user_number,'is:', result)
except ValueError:
    print('Your data is invalid, you need to put only numbers')
except ZeroDivisionError:
    print('This is impossible, division by zero won\'t be possible')

#Note: Remember only one exception can runs 
    
'''You even can put both of the last exceptions on the same line:'''
try:
    user_number=int(input('Type a number: '))
    result=1/user_number
    print('The reciprocal of number:', user_number,'is:', result)
except (ValueError, ZeroDivisionError):
    print('Your data is invalid, you need to put only numbers but omit the 0')
