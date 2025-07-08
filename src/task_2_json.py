import json

from src.decorators import count_filtered_transactions


@count_filtered_transactions
def filtered_transaction(transactions, currency):
    filtered_by_currency = [transaction for transaction in transactions if transaction['currency'] == currency]
    return filtered_by_currency


with open('../data/transactions.json', 'r') as file:
    operations = json.load(file)

filtered_data = filtered_transaction(operations, currency='USD')

with open('../data/transactions_filtered.json', 'w') as file:
    json.dump(filtered_data, file, indent=4)
