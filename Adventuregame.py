name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input(
    "You are on a hunt for some gold, your path begins now and you have the option to go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer = input(
        "You come to a river, you can walk around it or swim accross? Type walk to walk around and swim to swim accross: ")

    if answer == "swim":
        print("You swam acrross and were eaten by an alligator.")
    elif answer == "walk":
        answer = input("You walked for many miles and got lost. If you want to got back, type back or you lose.")
 
        if answer == "back":
        	print("You stubble upon the gold on your way back, congratulations you WIN!")	
        else:
        	 print("Too bad your too lazy to try, good luck next time.")

elif answer == "right":
    answer = input(
        "You come to a bridge, it looks wobbly, do you want to cross it or head back (cross/back)? ")

    if answer == "back":
        print("You go back and lose.")
    elif answer == "cross":
        answer = input(
            "You cross the bridge and meet a stranger. Do you talk to them (yes/no)? ")

        if answer == "yes":
            print("You talk to the stanger and they give you gold. You WIN!")
        elif answer == "no":
            print("You ignore the stranger and they are offended and push you into a ditch. You lose:(")
        else:
            print('Not a valid option. You lose.')
    else:
        print('Not a valid option. You lose.')

else:
    print('Not a valid option. You lose.')

print("Thank you for trying", name)