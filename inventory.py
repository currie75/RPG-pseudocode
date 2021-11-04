# Cs30
# Period 1
# October/4th/2021
# Ethan currie
# This is the inventory
# the three types of weapons in you inventory
inventory = {"(shiny sword)":{"description": " Its shiny but its sharp",
                            "damage": 75},
              "(Big OL Stick)":
                          {"description": " Its big and chunky",
                            "damage": 100},
              "(Crossybow)":
                          {"description": "Its a bit accurate",
                            "damage": 75}}
# this the inventory that is called into the menu
def inventory_print():
  for weapon in inventory:
    print(f"{weapon} {inventory[weapon]}")
