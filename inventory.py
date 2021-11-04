# Cs30
# Period 1
# October/4th/2021
# Ethan currie
# This is the inventory

inventory = {"(shiny sword)":{"description": " Its shiny but its sharp",
                            "damage": 75},
              "(Big OL Stick)":
                          {"description": " Its big and chunky",
                            "damage": 100},
              "(Crossybow)":
                          {"description": "Its a bit accurate",
                            "damage": 75}}


def inventory_print():
  for weapon in inventory:
    print(f"{weapon} {inventory[weapon]}")
