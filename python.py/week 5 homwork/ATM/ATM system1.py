balance = 1000

while True:
    print("\n===== ATM MENU =====")
    print("1 - Show Balance")
    print("2 - Deposit")
    print("3 - Withdraw")
    print("0 - Exit")

    choice = input("Choose an option: ")

    # ---------------- EXIT ----------------
    if choice == "0":
        print("Goodbye!")
        break

    # ---------------- SHOW BALANCE ----------------
    elif choice == "1":
        print("Current balance:", balance)

    # ---------------- DEPOSIT ----------------
    elif choice == "2":
        while True:
            print("\nDeposit amounts: 50, 100, 200, 500")
            amount = int(input("Enter amount (0 to cancel): "))

            if amount == 0:
                print("Deposit cancelled.")
                break

            if amount in (50, 100, 200, 500):
                balance += amount
                print("Deposited:", amount)
                print("New balance:", balance)
                break
            else:
                print("Invalid amount, try again.")

    # ---------------- WITHDRAW ----------------
    elif choice == "3":
        while True:
            print("\nWithdraw amounts: 50, 100, 200, 500")
            amount = int(input("Enter amount (0 to cancel): "))

            if amount == 0:
                print("Withdrawal cancelled.")
                break

            if amount in (50, 100, 200, 500):
                if amount <= balance:
                    balance -= amount
                    print("Withdrew:", amount)
                    print("New balance:", balance)
                    break
                else:
                    print("Insufficient funds.")
            else:
                print("Invalid amount, try again.")

    else:
        print("Invalid option, try again.")
