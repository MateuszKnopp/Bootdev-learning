first = 5
second = 7
third = 9
average_value = (first + second + third) / 3
print(average_value)  # 7.0

#############################################

player_health = 1000
armor_multiplier = 2

armored_health = player_health * armor_multiplier

print(armored_health)  # 2000

#############################################

player_health = 100
poison_damage = 10

player_poison_health = player_health - poison_damage

print(player_poison_health)  # 90

#############################################

# Variable names
"""
Snake Case - num_new_users
Camel Case - numNewUsers
Pascal Case - NumNewUsers

"""

#############################################
# An integer (or "int") is a number without a decimal part:

x = 5  # positive integer
y = -5  # negative integer

# A float is a number with a decimal part:

x = 5.2
y = -5.2

# Booleans
# A "Boolean" (or "bool") is a type that can only have one of two values:
# True or False. As you may have heard, computers really only use 1's and 0's.
# These 1's and 0's are just True/False boolean values.

is_tall = True
is_short = False

#############################################

player_health = 100
player_has_magic = True

print(
    "player_health is a/an", type(player_health).__name__
)  # player_healthi is a/an int
print(
    "player_has_magic is a/an", type(player_has_magic).__name__
)  # player_has_magic is a/an bool

#############################################

name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

print("NAME is a RACE who is AGE years old.")

#############################################
