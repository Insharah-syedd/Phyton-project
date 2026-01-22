print('Welcome to my computer quiz!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()

print("Okay! Let's play :)")
Score = 0

# Question 1
answer = input("What does HTML stand for? ")
if answer.lower() == "hypertext markup language":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

# Question 2
answer = input("What does CSS stand for? ")
if answer.lower() == "cascading style sheets":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

# Question 3
answer = input("What does HTTP stand for? ")
if answer.lower() == "hypertext transfer protocol":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

# Question 4
answer = input("What does URL stand for? ")
if answer.lower() == "uniform resource locator":
    print("Correct!")
    Score += 1
else:
    print("Incorrect!")

# Final score
print("You got " + str(Score) + " questions correct")
print("You got " + str((Score/4) * 100) + "%.")

