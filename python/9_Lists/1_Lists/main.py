# A natural way to organize and store data is in a List. Some languages call them "arrays", but in Python we just call them lists. Think of all the apps you use and how many of the items in the app are organized into lists.

# For example:

# An X (formerly Twitter) feed is a list of posts
# An online store is a list of products
# The state of a chess game is a list of moves
# This list is a list of things that are lists
# Lists in Python are declared using square brackets, with commas separating each item:
#
# inventory = ["Iron Breastplate", "Healing Potion", "Leather Scraps"]

# Lists can contain items of any data type, in our example above we have a List of strings.
###########################################################


def get_inventory():
    return ["Healing Potion", "Leather Scraps", "Iron Helmet", "Shortsword"]


def test():
    inventory = get_inventory()
    print(f"Inventory contains: {inventory}")
    print("=====================================")


def main():
    test()


main()


#################################################
# Sometimes when we're manually creating lists it can be hard to read if all the items are on the same
# line of code. We can declare the list using multiple lines if we want to:

# flower_types = [
#    "daffodil",
#    "rose",
#    "chrysanthemum"
# ]

# player_ages = [
#    23,
#    18,
#    31,
#    42
# ]

# Writing it this way helps with readability and organization, especially if there are many items
# or if some of the items are too long. Keep in mind this is just a styling change. The code will run correctly either way.
#
# #########################################################################
# In the world of programming, counting is a bit strange!

# We don't start counting at 1, we start at 0 instead.

# Indexes
# Each item in a list has an index that refers to its spot in the list.

# Take the following list as an example:

# names = ["Bob", "Lane", "Alice", "Breanna"]

# Index 0: Bob
# Index 1: Lane
# Index 2: Alice
# Index 3: Breanna
