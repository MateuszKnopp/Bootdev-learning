# Tworzymy listę (obiekt)
a = [1, 2, 3]

b = a

# Sprawdzamy czy to ten sam obiekt?
print(a is b)  # True! (To ta sama lista)

# Modyfikujemy przez "b"
b.append(99)

# Sprawdzamy co widzi "a"
print(a)  # [1, 2, 3, 99]
