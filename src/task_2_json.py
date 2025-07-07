import json


def filtered_transaction(transactions, currency):
    filtered_by_currency = []
    for transaction in transactions:
        if transaction['currency'] == currency:
            filtered_by_currency.append(transaction)
    return filtered_by_currency


with open('../data/transactions.json', 'r') as file:
    operations = json.load(file)
    print(operations)

filtered_data = filtered_transaction(operations, currency='USD')

with open('../data/transactions_filtered.json', 'w') as file:
    json.dump(filtered_data, file)
