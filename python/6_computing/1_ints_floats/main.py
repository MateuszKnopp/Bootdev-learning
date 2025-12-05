# Integers are simply whole numbers, positive or negative. For example, 3 and -3 are both examples of integers.
# A float is, as you may have guessed, the number type that allows for decimal values.
# double isn’t a built-in Python type!


def calculate_damage(sword, arrow, spear, dagger, fireball):
    total_damage = sword + arrow + spear + dagger + fireball
    average_damage = total_damage / 5
    return total_damage, average_damage
