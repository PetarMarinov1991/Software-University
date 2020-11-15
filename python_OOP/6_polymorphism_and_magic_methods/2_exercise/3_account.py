class Account:
    def __init__(self, owner: str, amount=None):
        self.owner = owner
        self.amount = 0 if amount is None else amount
        self._transactions = []

    def add_transaction(self, amount):
        if not isinstance(amount, int):
            raise ValueError('please use int for amount')
        else:
            self._transactions.append(amount)

    @property
    def balance(self):
        return self.amount + sum(self._transactions)

    @staticmethod
    def validate_transaction(account, amount_to_add):
        if account.balance + amount_to_add < 0:
            raise ValueError('sorry cannot go in debt!')
        account.add_transaction(amount_to_add)
        return f'New balance: {account.ballance}'

    def __len__(self):
        return len(self._transactions)

    def __str__(self):
        return f'Account of {self.owner} with starting amount: {self.balance}'

    def __repr__(self):
        return f'Account({self.owner}, {self.amount})'

    def __getitem__(self, i):
        return self._transactions[i]

    def __reversed__(self):
        return self._transactions[::-1]

    def __gt__(self, other):
        return self.balance > other.balance

    def __ge__(self, other):
        return self.balance >= other.balance

    def __eq__(self, other):
        return self.balance == other.balance

    def __ne__(self, other):
        return self.balance != other.balance

    def __add__(self, other):
        account = Account(owner=f'{self.owner}&{other.owner}', amount=self.amount + other.amount)
        account._transactions.extend(self._transactions + other._transactions)
        return account
