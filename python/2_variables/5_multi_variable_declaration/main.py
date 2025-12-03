# We can save space when creating many new variables by declaring them on the same line:

sword_name, sword_damage, sword_length = "Excalibur", 10, 200

# Which is the same as:

sword_name = "Excalibur"
sword_damage = 10
sword_length = 200

# Any number of variables can be declared on the same line, and variables declared
# on the same line should be related to one another in some way so that the code remains easy to understand.

# We call code that's easy to understand "clean code".

#########
# New assignment

quest_start = "You there! Adventurer!"
quest_middle = "The local mine has been taken over by orcs!"
quest_end = "We need your help taking it back."
quest_objective = "Bring back 8 of their axes as proof of your hard work."
space = " "

sentence = f"{quest_start}\n{quest_middle}\n{quest_end}{space}{quest_objective}"
print(sentence)

# assignment
game_one_score = 97
game_two_score = 92
game_three_score = 106
game_four_score = 105

# Don't touch above this line

average_score = (
    game_one_score + game_two_score + game_three_score + game_four_score
) / 4

print(round(average_score))

###############
# assignment


name = "Lopen"
level = 25
character_class = "Windrunner"
magic_resistance = 15.0
account_active = True

# Don't edit below this line

print("Character Report")
print(f"{name} is a level {level} {character_class}.")
print(f"They have {magic_resistance} magic resistance.")
print(f"Their account is currently active: {account_active}")

print("=========================")
print("Character Report Complete")
print("Data types:")
print(
    f"name: {type(name).__name__}, level: {type(level).__name__}, character_class: {type(character_class).__name__}"
)
print(f"magic_resistance: {type(magic_resistance).__name__}")
print(f"account_active: {type(account_active).__name__}")
