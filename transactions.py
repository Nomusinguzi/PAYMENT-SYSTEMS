import json

transactions = []

def save_transactions():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)


def send_money(balances, sender, receiver, amount):

    # 1. Validate users exist
    if sender not in balances:
        print(f"Error: Sender '{sender}' does not exist.")
        return

    if receiver not in balances:
        print(f"Error: Receiver '{receiver}' does not exist.")
        return

    # 2. Validate amount
    if amount <= 0:
        print("Error: Amount must be greater than 0.")
        return

    # 3. Check balance
    if balances[sender] < amount:
        print("Error: Insufficient balance.")
        return

    # 4. Perform transaction
    balances[sender] -= amount
    balances[receiver] += amount

    transaction = {
        "sender": sender,
        "receiver": receiver,
        "amount": amount
    }

    transactions.append(transaction)
    save_transactions()

    print("Transaction successful.")
