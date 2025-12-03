import os  # Celowo nieużywany import


def main():
    name = "Użytkowniku"
    print(f"Witaj, {name}!")  # F-string


if __name__ == "__main__":
    main()


a = 100
b = 100
print(a is b)  # True (To ten sam adres w RAM, Python użył cache)

x = 99999
y = 99999
print(x is y)  # False (Dla dużych liczb Python stworzył dwa osobne obiekty PyObject!)
