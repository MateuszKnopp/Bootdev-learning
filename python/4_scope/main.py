# Scope refers to where a variable or function name is available to be used.
# For example, when we create variables in a function (such as by giving names to our parameters),
# that data is not available outside of that function.


def subtract(x, y):
    return x - y


result = subtract(5, 3)
# print(x) # ERROR! "name 'x' is not defined"

##############################################
pi = 3.14


def get_area_of_circle(radius):
    return pi * radius * radius


# Because pi was declared in the parent "global" scope, it is usable within the get_area_of_circle() function.
##############################################
player_level = 4
# Don't touch below this line


def calculate_health(modifier):
    return player_level * modifier


def calculate_primary_stats(armor_bonus, modifier):
    return armor_bonus + modifier + player_level


print(f"Character has {calculate_health(10)} max health.")

print(f"Character has {calculate_primary_stats(3, 8)} primary stats.")
