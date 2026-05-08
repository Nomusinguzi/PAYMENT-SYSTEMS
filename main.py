from users import balances
from transactions import send_money, transactions

print("MINI PAYMENT SYSTEM")

while True:
    print("\n1. Send Money")
    print("2. View Transactions")
    print("3. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        sender = input("Sender: ")
        receiver = input("Receiver: ")
        amount = int(input("Amount: "))

        send_money(balances, sender, receiver, amount)

    elif choice == "2":
        print("\n===== TRANSACTION HISTORY =====\n")

        if not transactions:
            print("No transactions yet.")
        else:
            for i, t in enumerate(transactions, start=1):
                print(f"Transaction {i}")
                print(f"From: {t['sender']}")
                print(f"To: {t['receiver']}")
                print(f"Amount: {t['amount']}")
                print("---------------------------")

    elif choice == "3":
        break

    else:
        print("Invalid option.")