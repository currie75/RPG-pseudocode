
 def enemygen(levelBoss):
    """
    :param levelBoss:
    :return: This function will return an enemy or a boss depending if
    the variable 'level boss' is True or False
    """
    temp = []
    with open('adjective.txt', 'r') as file:
        lines = file.readlines()
        # as we want to choose a random adjective, our adjective is going to be between
        # the first adjective (0) and the lenght of the file -1 because of how Python operates the numbers
        # we're putting the [:-1] to eliminate from the text the '/n' that appears in each letter
        adjective = lines[random.randint(0, len(lines)-1)][:-1]
    with open('animal.txt', 'r') as file2:
        lines2 = file2.readlines()
        animal = lines2[random.randint(0, len(lines)-1)][:-1]

    if levelBoss == False:
        health = random.randint(50, 100)
        attack = random.randint(5,10)
        special = random.randint(10,20)
        chance = random.randint(1,10)

        # In here we're saying: call the class Enemy and give those attributes
        return Enemy(health, attack, special, chance, adjective + " " + animal)

    else:
        health = random.randint(200, 250)
        attack = random.randint(20, 40)
        special = random.randint(50, 60)
        chance = random.randint(1, 8)
        superMove = random.randint(100,200)

        # Return the Boss object and give it those attributes
        return Boss(health, attack, special, chance, adjective + " " + animal, superMove)
