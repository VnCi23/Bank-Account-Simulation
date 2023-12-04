# Vince Christian Gaurino
# 2nd year BSIS 2A

# My balance
balance = 500

while True:
    print("Bank Account Simulation:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = int(input("Enter your choice (1/2/3/4): "))

    if choice == 1:
        deposit_amount = float(input("Enter the deposit amount: "))
        balance += deposit_amount
        print("Deposit successful. Current balance: P" + str(balance))
    elif choice == 2:
        withdrawal_amount = float(input("Enter the withdrawal amount: "))
        if withdrawal_amount > balance:
            print("Insufficient funds. Withdrawal failed.")
        else:
            balance -= withdrawal_amount
            print("Withdrawal successful. Current balance: P" + str(balance))
    elif choice == 3:
        print("Current balance: P" + str(balance))
    elif choice == 4:
        print("Exiting bank account simulation.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")

# Countdown
print("Let's do a countdown:")
for i in range(10, 0, -1):
    print(i)
print("Blast off!")
print("Activity complete. Thank you!")
