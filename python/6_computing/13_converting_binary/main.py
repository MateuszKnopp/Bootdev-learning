# "100" -> 4
# "101" -> 5
# "10010" -> 18
# The built-in int() function can convert a binary string to an integer.
# It takes a second argument that specifies the base of the number (binary is base 2). For example:

# this is a binary string
binary_string = "100"

# convert binary string to integer
num = int(binary_string, 2)
print(num)
# 4
##################################################################


def binary_string_to_int(num_servers, num_players, num_admins):
    servers = int(num_servers, 2)
    players = int(num_players, 2)
    admins = int(num_admins, 2)
    return servers, players, admins
    pass
