# Here are some basic rules with if/else blocks.

# You can't have an elif or an else without an if
# You can have an else without an elif
# Remember, to check if two values are the same use the == operator.

#######################################################################
def check_high_score(current_player_name, high_scoring_player_name):
    if current_player_name == high_scoring_player_name:
        return "You are the highest scoring player!"
    else:
        return "You are not the highest scoring player!"
