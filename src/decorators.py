from functools import wraps


def count_filtered_transactions(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        summ_transaction = sum(item['amount'] for item in result)
        print(f'Количество отфильтрованных транзакций {len(result)}. Сумма {summ_transaction}')
        return result

    return wrapper


