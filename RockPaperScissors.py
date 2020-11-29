from random import randint

uses = ['حجر', 'ورقه', 'مقص']

choice = uses[randint(0, 2)]

print('تقدر تختار في ايش راح تلعب من بين ' +
      uses[0] + ' , ' + uses[1] + ' , ' + uses[2])
user_choice = input('انا بلعب ')

print('انا اخترت ' + choice)

if choice == user_choice:
    print('تعادل')

elif user_choice == 'ورقه':
    if choice != 'مقص':
        print('انت فزت')
    else:
        print('انا فزت')

elif user_choice == 'حجر':
    if choice != 'ورقه':
        print('انت فزت')
    else:
        print('انا فزت')

elif user_choice == 'مقص':
    if choice != 'حجر':
        print('انت فزت')
    else:
        print('انا فزت')
