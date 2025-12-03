# In Python, we can create strings that contain dynamic values with the f-string syntax.

num_bananas = 10
bananas = f"You have {num_bananas} bananas"
print(bananas)
# You have 10 bananas

name = "Yarl"
age = 37
race = "dwarf"

# Don't edit above this line

dwarf = f"{name} is a {race} who is {age} years old."
print(dwarf)


# When working with strings the + operator performs a "concatenation",
# which is a fancy word that means "joining two strings". Generally speaking, it's better to use
# string interpolation with f-strings over + concatenation.

first_name = "Lane "
last_name = "Wagner"
full_name = first_name + last_name
print(full_name)
# prints "Lane Wagner"

# full_name now holds the value "Lane Wagner".
# Notice the extra space at the end of "Lane " in the first_name variable.

# Task:
sentence_start = "You have "
sentence_end = " health"

player1_health = "1200"
player2_health = "1100"

# concatenation
print(sentence_start + player1_health + sentence_end)
print(sentence_start + player2_health + sentence_end)

# interpolation
sentence1 = f"{sentence_start}{player1_health}{sentence_end}"
sentence2 = f"{sentence_start}{player2_health}{sentence_end}"

print(sentence1)
print(sentence2)
