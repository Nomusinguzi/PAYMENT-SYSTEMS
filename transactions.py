import json

transactions = []
def save_transactions():
    with open("transactions.json", "w") as file:
        json.dump(transactions, file, indent=4)

def send_money(balances, sender, receiver, amount):
    if balances[sender] >= amount:
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
    else:
        
        print("Insufficient funds.")
