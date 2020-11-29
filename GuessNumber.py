from random import randint

computer_choice = randint(1, 10)

print('Hey.. what\'s your name ?')
player_name = input('My name : ')
print('Ok, ' + player_name +
      ' i will pick a random number between 1 to 10.. can you guess it ?')
print('ok i picked number :)')

limit = 0
while limit <= 3:
    guess = int(input())
    limit += 1
    if guess < computer_choice:
        print('Your guess is low')
    elif guess > computer_choice:
        print('Your guess is high')
    elif guess == computer_choice:
        print('Correct :))))))')
        break
else:
    print('oh , your out of your limit :( ... my choice was ' + str(computer_choice))
