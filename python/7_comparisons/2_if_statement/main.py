# It's often useful to only execute code if a certain condition is met:

# if CONDITION:
# # do some stuff here

# code after the if block may still run regardless

# For example, in this code:

# def show_status(boss_health):
#    if boss_health > 0:
#        print("Ganondorf is alive!")
#        return
#    print("Ganondorf is unalive!")

# if boss_health is greater than 0, then this will be printed:

# Ganondorf is alive!

# Otherwise, this will be printed:

# Ganondorf is unalive!

# Without a return in the if block, Ganondorf is unalive would always be printed:

# def show_status(boss_health):
#    if boss_health > 0:
#        print("Ganondorf is alive!")
#    print("Ganondorf is unalive!")
# This code could print both messages:

# Ganondorf is alive!
# Ganondorf is unalive!
#############################################################


def print_status(player_health):
    if player_health <= 0:
        print("dead")
        print("status check complete")
        return
    print("status check complete")
    pass


def test(health):
    print(f"Player Health: {health}")
    print("Checking status...")
    print_status(health)
    print("=====================================")


def main():
    test(0)
    test(5)
    test(-1)
    test(3)


main()
