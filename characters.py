# Cs30
# Period 1
# October/4th/2021
# Ethan currie
# This is the character choice

character_options = {
        "(Adventurer)":
            {"description": " has the ability to use any weapon"
                "+ 10 in damage and + 10 in defense"},
        "(The Explorer)":
            {"description": " has the ability to explore any where"
                "+ 5 damage and + 15 defense "}
            }

# this is the charcter is called in to menu
def character_print():
  for character in character_options:
    print(f"{character} - {character_options[character]}")
