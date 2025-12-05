# It's fairly common to want to change the value of a variable based on its current value.

player_score = 4
player_score = player_score + 1
# player_score now equals 5

player_score = 4
player_score = player_score - 1
# player_score now equals 3

# Don't let the fact that the expression player_score = player_score - 1 is not a valid mathematical
# expression be confusing. It doesn't matter, it is valid code. It's valid because the way the expression should be read in English is:

# Assign to player_score the current value of player_score minus 1


# In this operation, the right-hand side (player_score - 1) is calculated first.
# Once we have the result, we update player_score with this new value.
#
###############################################################
def update_player_score(current_score, increment):
    current_score = current_score + increment
    return current_score
    pass
