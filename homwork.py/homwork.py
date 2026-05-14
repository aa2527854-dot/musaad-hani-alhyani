total = 287

hundreds = total // 100
remaining = total % 100

fifties = remaining // 50
remaining = remaining % 50

twenties_five = remaining // 25
remaining = remaining % 25

tens = remaining // 10
remaining = remaining % 10

fives = remaining // 5
remaining = remaining % 5

ones = remaining

print("Total halalas:", total)
print()
print(" 100-halala coins:", hundreds)
print("  50-halala coins:", fifties)
print("  25-halala coins:", twenties_five)
print("  10-halala coins:", tens)
print("   5-halala coins:", fives)
print("   1-halala coins:", ones)
