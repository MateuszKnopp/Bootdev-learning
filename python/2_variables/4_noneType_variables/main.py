# https://docs.python.org/3/library/constants.html#None
# Not all variables have a value. We can make an "empty" variable by setting it to None.
# None is a special value in Python that represents the absence of a value. It is not the same as zero, False, or an empty string.

my_mental_acuity = None

# The value of my_mental_acuity in this case is None until we use the assignment operator, =, to give it a value.

# 0 != None
# None Is NOT a String
# NoneType is not the same as a string with a value of "None":

my_none = None  # this is a None-type
my_none_str = "None"  # this is a string with the value "None"


######Task########
# create the empty "enemy" variable here
enemy = None

print(enemy is None)

# sprawdzenie typu wartosci
print(type(my_none))
print(type(my_none_str))
