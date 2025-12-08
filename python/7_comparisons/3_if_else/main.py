# First the if statement is evaluated. If it is True then the if statement's body is executed
# and all the other elifs and the else are ignored.

# If the first if is false then the next elif is evaluated.
# Likewise, if it is True then its body is executed and the rest are ignored.

# If none of the if or elif statements evaluate to True then the final else statement will be
# the only body executed.


#################################


def player_status(health):
    if health <= 0:
        return "dead"
    elif health <= 5:
        return "injured"
    else:
        return "healthy"
