import random
print('Welcome to Rock-Paper-Scissors')
Choices=['rock','paper','scissors']

while True:
    user=input('Enter rock,paper or scissors(or q to quit):').lower()

    if user=='q':
        print('Thanks for playing!')
        break
    if user not in Choices:
        print('Invalid choices please types rock, paper or scissors')
        continue
    computer=random.choice(Choices)
    print(f'computer chose:{computer}')

    if user== computer:
        print('It''s a draw!')
    elif(user=='rock' and computer =='Scissors')or \
        (user =='paper' and computer == 'Rock') or \
        (user == 'scissors'and computer == 'paper'):
        print('you win')
    else:
        print('Computer Wins')

2
