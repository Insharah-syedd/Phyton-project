name = input("Type your name: ")
print(f"Welcome {name} to the Epic Adventure Quest! 🌲🗡️")

# First decision
answer = input("You find yourself at a crossroads in a dark forest. Do you go 'left' towards the mountains or 'right' into the valley? ").lower()

if answer == "left":
    answer = input("You reach the base of a towering mountain. Do you 'climb' it or 'walk' around it? ").lower()
    if answer == "climb":
        answer = input("Halfway up, a storm hits! Do you 'keep going' or 'descend'? ").lower()
        if answer == "keep going":
            print("You reach the peak and find a hidden treasure! You WIN! 🏔️💰")
        elif answer == "descend":
            print("You slip on the rocks and fall. Game Over! 💀")
        else:
            print("Indecision costs you. A rockslide buries you. Game Over!")
    elif answer == "walk":
        answer = input("You walk around and find a mysterious cabin. Do you 'enter' or 'ignore' it? ").lower()
        if answer == "enter":
            print("The cabin is home to a friendly wizard who gives you magical gold. You WIN! ✨🏠")
        elif answer == "ignore":
            print("You continue walking, but get lost in the forest forever. Game Over! 🌲")
        else:
            print("Invalid choice! You wander until night falls. Game Over!")
    else:
        print("Not a valid option. You lose in the wilderness. Game Over!")

elif answer == "right":
    answer = input("You enter a misty valley and see a river. Do you 'swim' across or 'follow' it downstream? ").lower()
    if answer == "swim":
        print("The current is too strong! You are swept away. Game Over! 🌊")
    elif answer == "follow":
        answer = input("You find an old bridge. Do you 'cross' it or 'rest' by the river? ").lower()
        if answer == "cross":
            answer = input("On the other side, a stranger offers you a choice of two doors: 'gold' or 'mystery'. Which do you pick? ").lower()
            if answer == "gold":
                print("The gold is cursed! You turn into stone. Game Over! 🪨")
            elif answer == "mystery":
                print("The mystery door leads to a secret paradise. You WIN! 🌟")
            else:
                print("Indecision costs you. The stranger disappears and you are lost. Game Over!")
        elif answer == "rest":
            print("While resting, a wild wolf attacks you. Game Over! 🐺")
        else:
            print("Not a valid choice. You wander until you can't go further. Game Over!")
    else:
        print("Invalid option. You are trapped in the mist forever. Game Over!")

else:
    print("Not a valid option! You stand still until night falls. Game Over!")
