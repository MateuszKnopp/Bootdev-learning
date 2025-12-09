# The "step" parameter determines how much to add to i in each iteration of the loop. You can even go backwards:

# for i in range(3, 0, -1):
#    print(i)

## prints:
## 3
## 2
## 1


def count_down(start, end):
    for i in range(start, end, -1):
        print(i)


def test(start, end):
    print(f"Using inputs start: {start} and end: {end}")
    print(f"Printing numbers from {start} to {end + 1}:")
    count_down(start, end)
    print("=====================================")


def main():
    test(10, 0)
    test(20, 10)
    test(15, 11)


main()
