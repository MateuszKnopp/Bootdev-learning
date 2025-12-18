# With this operator, you can specify where to start and end the slice, and how to step through the original list. List slicing returns a new list from the existing list.

# The syntax is as follows:

# my_list[ start : stop : step ]

# For example:

# scores = [50, 70, 30, 20, 90, 10, 50]
## Display list
# print(scores[1:5:2])
## Prints [70, 20]

# The above reads as "give me a slice of the scores list from index 1, up to but not including 5, skipping every 2nd value". All of the sections are optional.

# Omitting Sections
# You can also omit various sections ("start", "stop", or "step"). For example, numbers[:3] means "get all items from the start up to (but not including) index 3". numbers[3:] means "get all items from index 3 to the end".

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers[:3] # Gives [0, 1, 2]
# numbers[3:] # Gives [3, 4, 5, 6, 7, 8, 9]

# Using Only the “step” Section
# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers[::2] # Gives [0, 2, 4, 6, 8]

# Negative Indices
# Negative indices count from the end of the list. For example, numbers[-1] gives the last item in the list, numbers[-2] gives the second last item, and so on.

# numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# numbers[-3:] # Gives [7, 8, 9]
######################################################
# Assignment
# Complete the given get_champion_slices function. It takes a list of champions and should return three new lists based on the given champions:

# First, return a slice of the champions list that starts with the third champion and goes to the end of the list.
# Next, return a slice of the champions list that starts at the beginning of the list and includes all champions except for the very last champion.
# Last, return a slice of the champions list that only includes the champions in even numbered indexes.
########################################################


def get_champion_slices(champions):
    champ1 = champions[2:]
    champ2 = champions[0 : len(champions) - 1 : 1]
    champ3 = champions[0::2]
    return champ1, champ2, champ3


#    return champions[2:], champions[:-1], champions[::2]
