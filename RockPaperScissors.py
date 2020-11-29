from random import randint

uses = ['ROCK', 'PAPER', 'SCISSORS']

choice = uses[randint(0, 2)]

print('Hey , you can pick your choice play ' +
      uses[0] + ' , ' + uses[1] + ' , ' + uses[2])
user_choice = input('i\'ll play with : ').upper()

print('Ok , i choiced ' + choice)

if choice == user_choice:
    print('draw')

elif user_choice == uses[1]:
    if choice != uses[2]:
        print('u won :)')
    else:
        print('i won :|')

elif user_choice == uses[0]:
    if choice != uses[1]:
        print('u won :)')
    else:
        print('i won :|')

elif user_choice == uses[2]:
    if choice != uses[0]:
        print('u won :)')
    else:
        print('i won :|')
