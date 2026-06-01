colors = ("red", "green", "blue")
try:
    colors[0] = "yellow"
except TypeError as e:
    print("Error:", e)

print("Length of tuple:", len(colors))

print("Is 'red' in tuple?:", "red" in colors)
PROBLEM 1: ATM SYSTEM