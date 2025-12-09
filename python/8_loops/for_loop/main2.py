# As a reminder, a "for loop" in Python is written like this:

# for i in range(0, 10):
#    print(i)

# In English, the code says:

# 1. Start with i equals 0. (i in range(0))
# 2. If i is greater than or equal to 10 (range(0, 10)), exit the loop.
# 3. Print i to the console. (print(i))
# 4. Add 1 to i. (range defaults to incrementing by 1)
# 5. Go back to step 2

# The result is that the numbers 0-9 are logged to the console in order.


def print_numbers():
    for i in range(0, 200):
        print(i)


def test():
    print("Printing numbers from 0 to 199:")
    print_numbers()
    print("=====================================")


def main():
    test()


main()
