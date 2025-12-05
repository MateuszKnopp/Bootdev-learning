# Bitwise operators are similar to logical operators, but instead of operating on boolean values,
# they apply the same logic to all the bits in a value by column. For example, say you had the numbers
# 5 and 7 represented in binary. You could perform a bitwise AND operation and the result would be 5.

# 0101 is 5
# 0111 is 7
# 0101
# &
# 0111
# =
# 0101

# A 1 in binary is the same as True, while 0 is False. So really a bitwise operation is just a bunch of
# logical operations that are completed in tandem by column.

# 0 & 0 = 0

# 1 & 1 = 1

# 1 & 0 = 0

# Ampersand & is the bitwise AND operator in Python. "AND" is the name of the bitwise operation, while
# ampersand & is the symbol for that operation. For example, 5 & 7 = 5, while 5 & 2 = 0.

# 0101 is 5
# 0010 is 2
# 0101
# &
# 0010
# =
# 0000

# Binary Notation
# When writing a number in binary, the prefix 0b is used to indicate that what follows is a binary number.
# 0b10 is two in binary, but 10 without the 0b prefix is simply ten.
##############################################################

can_create_guild = 0b1000
can_review_guild = 0b0100
can_delete_guild = 0b0010
can_edit_guild = 0b0001


def get_create_bits(user_permissions):
    return user_permissions & can_create_guild
    pass


def get_review_bits(user_permissions):
    return user_permissions & can_review_guild
    pass


def get_delete_bits(user_permissions):
    return user_permissions & can_delete_guild
    pass


def get_edit_bits(user_permissions):
    return user_permissions & can_edit_guild
    pass
