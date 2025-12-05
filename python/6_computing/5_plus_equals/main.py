# Python makes reassignment easy when doing math. In JavaScript or Go, you might be familiar with
# the ++ syntax for incrementing a number variable by 1. In Python, we use the += in-place operator instead.

star_rating = 4
star_rating += 1
# star_rating is now 5

# Other Operators
# The other in-place operators work similarly:

star_rating = 4
star_rating -= 1
# star_rating is now 3

star_rating = 4
star_rating *= 2
# star_rating is now 8

star_rating = 4
star_rating /= 2


# star_rating is now 2.0
###################################################################
def get_hurt(current_health, damage):
    current_health = current_health - damage
    return current_health
    pass
