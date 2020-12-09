#1. Описать класс "Банковский счет", атрибуты у которого:
#   имя аккаунта - str
#   уникальный id (uuid)
#   баланс float
#   транзакции (список)
#   Методы
#    депозит средств
#    вывод средств
#    получить баланс

#   При изменении баланса записывать в транзакции (сумма, тип операции, текущая_дата)
#   * доп. добавить и учитывать банковские комиссии (1%)

from datetime import datetime
import uuid

class BankAccount:


    """Банковский счет."""
    def __init__(self, name):
        """Инициализирует атрибуты."""
        self.name = name
        self.account_id = uuid.uuid4()
        self.balance = 0.0
        self.transactions = []

    def deposit_of_funds(self, amount):
        """Депозит средств."""
        self.balance += amount - (amount * 0.01)
        self.transactions.append((amount, 'deposit', datetime.now()))

    def withdrawal_of_funds(self, amount):
        """Вывод средств."""
        self.balance -= amount + (amount * 0.01)
        self.transactions.append((amount, 'withdrawal', datetime.now()))

    def get_balance(self):
        """Получить баланс."""
        return self.balance

first_client = BankAccount('First_client')
first_client.deposit_of_funds(200)
print(first_client.get_balance())
first_client.withdrawal_of_funds(100)
print(first_client.get_balance())
first_client.withdrawal_of_funds(300)
print(first_client.get_balance())
print(first_client.transactions)