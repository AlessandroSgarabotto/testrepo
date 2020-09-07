## This program tests the candidate's age
import math
age=input(' How old are you? ')
age=int(age)

if age >= 18:
    print( ' You can vote ')
else:
    print( ' You cannot vote ')
    c_age=18-age
    print( ' You have to wait', c_age, 'years.')


if 18 <=age <= 32:
    print( ' You can start a PostDoc ')
elif age > 32:
    print( ' I am sorry, we are looking for younger candidates. ' )
else:
    c_age=18-age
    print( ' You are too young to work with us! ')
