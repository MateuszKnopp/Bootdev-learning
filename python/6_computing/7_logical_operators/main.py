True and True == True
True and False == False
False and False == False

True or True == True
True or False == True
False or False == False


# We can nest logical expressions using parentheses.

print((True or False) and False)

# First, we evaluate the expression in the parentheses, (True or False). It evaluates to True:

print(True and False)

# True and False evaluates to False:

print(False)

# So, print((True or False) and False) prints "False" to the console.
