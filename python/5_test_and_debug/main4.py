# A stack trace (or "traceback") is a scary-looking error message that the Python interpreter
# prints to the console when it encounters certain problems. Stack traces are most common
# (at least for you right now) when you're trying to run invalid Python code.


#########################EXAMPLE CODE###############################
# def create_stats_message(strength, wisdom, dexterity):
#      total = strength + wisdom + dexterity
#    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
#    return msg

######################RESULT############################
# PythonError: Traceback (most recent call last):
#  File "<exec>", line 17, in <module>
#  File "<string>", line 1, in <module>
#  File "/home/pyodide/main.py", line 3
#    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
#                                                                                                                  ^
# IndentationError: unindent does not match any outer indentation level

# msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
# This is the line of code that caused the error.

# IndentationError: unindent does not match any outer indentation level
# This is the type of error that was raised. In this case, it's an IndentationError, which means that
# the Python interpreter was expecting a certain amount of indentation (whitespace at the beginning of the line) but it didn't get what it was expecting.

# Don't be fooled! The proper amount of indentation in Python is 4 spaces (or one <tab> stroke).
# In this case, line 2 is actually indented 6 spaces, which is why the interpreter is confused.

#################################################
# Po porawieniu wciecia jest kolejny blad jak ponizej

# def create_stats_message(strength, wisdom, dexterity):
#    total = strength + wisdom + dexterity
#    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
#    return msg

# PythonError: Traceback (most recent call last):
#  File "<exec>", line 17, in <module>
#  File "<string>", line 1, in <module>
#    File "/home/pyodide/main.py", line 3
#    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats.
#                                                                             ^
# SyntaxError: unterminated string literal (detected at line 3)


#########################CORRECT CODE##############################

# Brakowalo zamkniecia f-stringa


def create_stats_message(strength, wisdom, dexterity):
    total = strength + wisdom + dexterity
    msg = f"You have {strength} strength, {wisdom} wisdom, and {dexterity} dexterity for a total of {total} stats."
    return msg
