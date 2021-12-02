# Cs30
# Period 1
# October/4th/2021
# Ethan currie
# This is the inventory
# the four locations when you follow the signs
locations = {
        "(forest_lake)":
            {"description": " lies within the forest the "
                "+ its north"},
        "(The_cave)":
            {"description": " deep and dark place"
                "+ its south"},
        "(The_old_windmill)":
            {"description": " a mysterious mill "
                "+ its west"},
        "(The_old_wizard_hut)":
            {"a great wizard once lived here"
                "+ its east"}
            }
# the locations call into menu
def locations_print():
    for map in locations:
        print(f"{map} {locations[map]}")
