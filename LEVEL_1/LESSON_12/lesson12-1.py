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

class Bank_account():
    """Банковский счет."""
    def __init__(self, name,id, balance, transaction):
        """Инициализирует атрибуты str, uuid, float, list."""
        self.name = name
        self.id = id
        self.balance = balance
        self.transactions = transaction
    def deposit_of_funds(self):
        """Депозит средств."""
        print(f"{self.} is now deposit_of_funds.")
    def withdrawal_of_funds(self):
        """Вывод средств."""
        print(f"{self.transactions} is now withdrawal_of_funds")
    def get_balance(self):
        """Получить баланс."""
        print(f"{self.balance} is now balance")