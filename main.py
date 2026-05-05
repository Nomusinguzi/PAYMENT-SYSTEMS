import users

print(users.users)
print(users.balances)

from users import balances
from transactions import send_money, transactions

send_money(balances, "Ciara", "Calvin", 20000)
send_money(balances, "Lisa", "Jerry", 15000)
print(balances)
print(transactions)