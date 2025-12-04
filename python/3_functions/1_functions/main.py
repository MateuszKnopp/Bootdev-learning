def area_of_circle(r):
    pi = 3.14
    result = pi * r * r
    return result


radius = 5
area = area_of_circle(radius)
print(area)
# 78.5

# Why is the variable called 'radius' outside the function, but 'r' inside the function?
####
# Because only the value of the variable is passed to the function. It is then assigned to the new variable called 'r'
###########################################################################


def create_introduction(name, age, height, weight):
    first_part = "Your name is " + name + " and you are " + age + " years old."
    second_part = (
        "You are " + height + " meters tall and weigh " + weight + " kilograms."
    )
    full_intro = first_part + " " + second_part
    return full_intro


my_name = "John"
my_age = "30"

intro = create_introduction(my_name, my_age, "1.8", "80")
print(intro)
# Your name is John and you are 30 years old. You are 1.8 meters tall and weigh 80 kilograms.


# Functions can have multiple parameters ("parameter" being a fancy word for "input").
# It's the argument's position that determines which parameter receives it (at least, for now).
# The first argument goes to the first parameter, the second to the second, and so on.

# print() is a function that:
###Prints a value to the console
###Does not return a value
# return is a keyword that:
###Ends the current function's execution
###Provides a value (or values) back to the caller of the function
###Does not print anything to the console (unless the return value is later print()ed)
###########################################################################


def get_title(first_name, last_name, job):
    title = first_name + " " + last_name + " the " + job
    return title


# Don't touch below this line


def test(first_name, last_name, job):
    title = get_title(first_name, last_name, job)
    print("First name:", first_name)
    print("Last name:", last_name)
    print("Job:", job)
    print("Title:", title)
    print("=====================================")


test("Frodo", "Baggins", "warrior")
test("Bilbo", "Baggins", "thief")
test("Gandalf", "The Grey", "wizard")
test("Aragorn", "Son of Arathorn", "ranger")
###########################################################################

my_name = "Mateusz Knopp"
print(my_name)
# Mateusz Knopp

# Code executes in order from top to bottom, so a variable needs to be created before it can be used.
# That means that if you define a function, you can't call that function until after it has been defined.
###########################################################################
# Order of Functions
# Most Python developers solve this problem by defining all the functions in their program first, then they call an "entry point" function last.
# That way all of the functions have been read by the Python interpreter before the first one is called.
# Conventionally this "entry point" function is usually called main to keep things simple and consistent.


def main2():
    health = 10
    armor = 5
    add_armor(health, armor)


def add_armor(h, a):
    new_health = h + a
    print_health(new_health)


def print_health(new_health):
    print(f"The player now has {new_health} health")


# call entrypoint last
main2()


###########################################################################
def to_celsius(f):
    a = 5 / 9 * (f - 32)
    return a


def test1(f):
    c = round(to_celsius(f), 2)
    print(f, "degrees fahrenheit is", c, "degrees celsius")


test1(100)
test1(88)
test1(104)
test1(112)
###########################################################################
# When no return value is specified in a function, it will automatically return None.
# For example, maybe it's a function that prints some text to the console, but doesn't explicitly return a value.
# The following code snippets all return the same value, None:


def my_func():
    print("I do nothing")
    return None


def my_func1():
    print("I do nothing")
    return


def my_func2():
    print("I do nothing")


###########################################################################
def become_warrior(full_name, power):
    title = f"{full_name} the warrior"
    new_power = power + 1
    return title, new_power


def main3():
    test2("Frodo Baggins", 5)
    test2("Bilbo Baggins", 10)
    test2("Gandalf The Grey", 9000)


def test2(input1, input2):
    result1, result2 = become_warrior(input1, input2)
    print(result1, "has a power level of:", result2)


main3()
###########################################################################
# Parameters are the names used for inputs when defining a function.
# Arguments are the values of the inputs supplied when a function is called.


# a and b are parameters
def add(a, b):
    return a + b


# 5 and 6 are arguments
sum = add(5, 6)


###########################################################################
# A default value is created by using the assignment (=) operator in the function signature.
def get_punched(health, armor=0):
    damage = 50 - armor
    new_health = health - damage
    return new_health


def get_slashed(health, armor=0):
    damage = 100 - armor
    new_health = health - damage
    return new_health


# Don't touch below this line


def test3(health, armor):
    print(f"Running tests for health {health} and armor {armor}")
    print("========================================")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after punch: {get_punched(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: {armor}")
    print(f"Health after slash: {get_slashed(health, armor)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after slash: {get_slashed(health)}")
    print("----------------------------------------")
    print(f"Health: {health}, Armor: no armor!")
    print(f"Health after punch: {get_punched(health)}")
    print("----------------------------------------\n")


test3(400, 5)
test3(300, 3)
test3(200, 1)
# Hello there welcome! You've registered your email: lane@example.com


# As you may have guessed, for this structure to work, optional parameters (the ones with defaults) must come after all required parameters.
###########################################################################
def enchant_and_attack(target_health, damage, weapon):
    enchanted_damage = damage + 10
    new_health = target_health - enchanted_damage
    enachanted_weapon = f"enchanted {weapon}"
    return enachanted_weapon, new_health


# Don't modify below this line


def test4(target_health, damage, weapon):
    print(f"The target has {target_health} health.")
    print(f"{weapon} base damage: {damage}... Enchanting and attacking.")
    enchanted_weapon, new_health = enchant_and_attack(target_health, damage, weapon)
    print(f"The target has been attacked with the {enchanted_weapon}.")
    print(f"The target has {new_health} health remaining.")
    print("=====================================")


def main4():
    test4(100, 50, "sword")
    test4(500, 100, "axe")
    test4(1000, 250, "bow")


main4()
###########################################################################

###########################################################################

###########################################################################
###########################################################################


###########################################################################


###########################################################################

###########################################################################
