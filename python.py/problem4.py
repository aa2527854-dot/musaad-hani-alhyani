n = float(input("Enter number: "))

if n < -100:
    print("Negative large")
elif n < 0:
    print("Negative small")
elif n == 0:
    print("Zero")
elif n < 100:
    print("Positive small")
else:
    print("Positive large")
