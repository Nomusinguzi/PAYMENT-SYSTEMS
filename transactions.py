transactions = []
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
        print("Transaction successful.")
    else:
        print("Insufficient funds.")
