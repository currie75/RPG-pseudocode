# Cs30
# Period 1
# October/4th/2021
# Ethan currie
# This is text-base adventure game
import sys

# Welcome message
print("Welcome to the dark forest of bloodhornbog")
# The person will pick there username
print("Traveler what is your name")
name = input()
# General actions for the game
actions = ["follow signs", "attack", "heal", "inventory", "leave", " "]
# Possible actions for the game
possible_direction_actions = ["east", "west", "south", "north", " "]
attack_actions = ["stab ", "shoot ", "punch "]
heal_actions = ["eat mushroom", "eat chicken", "health potion", " "]

# While true loop for the story
while True:
    # Main menu, loop will return to this menu
    print("Choose one options below,leave by typing 'leave'.")
    for initial_choice in actions:
        print(initial_choice)
    user_input = input()
    # option menu for explore
    if user_input.lower() == "follow signs":
        for direction_options in possible_direction_actions:
            print(direction_options)
        user_input1 = input("Choose one out of the four options.\n")
        # Options in following signs
        if user_input1.lower() == "east":
            print(" you went east!")
        elif user_input1.lower() == "west":
            print(" you went west!")
        elif user_input1.lower() == "south":
            print(" you went south!")
        elif user_input1.lower() == "north":
            print(" you went north!")
    # option menu for combat
    elif user_input.lower() == "attack":
        for attack_options in attack_actions:
            print(attack_options)
        user_input2 = input("choose one out of three options. \n")
        # options in attacking
        if user_input2.lower() == "punch":
            print(" you punch it!")
        elif user_input2.lower() == "stab":
            print(" you stabed it!")
        elif user_input2.lower() == "shoot":
            print(" you shot it!")
    # options menu for healing
    elif user_input.lower() == "heal":
        for heal_options in heal_actions:
            print(heal_options)
        user_input3 = input("choose one out of three options. \n")
        # options in healing
        if user_input3.lower() == "eat mushroom":
            print("you ate mushrrom!")
        elif user_input3.lower() == "eat jerky":
            print("you ate jerky!")
        elif user_input3.lower() == "health potion":
            print("you drank health potion!")
