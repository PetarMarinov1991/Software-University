import unittest


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
        return f'New balance: {account.balance}'

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


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('Petar', 100)
        self.account_2 = Account('Ines', 50)

    def test_add_transaction_not_valid(self):
        with self.assertRaises(ValueError):
            self.account.add_transaction(50.50)

    def test_add_transaction_valid(self):
        self.assertEqual(len(self.account._transactions), 0)
        self.account.add_transaction(50)
        self.assertEqual(len(self.account._transactions), 1)

    def test_balance_property(self):
        self.assertEqual(self.account.balance, 100)
        self.account.add_transaction(50)
        self.assertEqual(self.account.balance, 150)

    def test_validate_transaction_raises_exception_when_less_then_zero(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.account, -102)

    def test_validate_transaction_raises_exception_when_invalid_amount(self):
        with self.assertRaises(ValueError):
            Account.validate_transaction(self.account, 50.50)

    def test_validate_transaction_valid(self):
        result = Account.validate_transaction(self.account, 100)
        self.assertEqual(result, 'New balance: 200')

    def test_validate_transaction_is_static_method(self):
        import types
        self.assertTrue(isinstance(self.account.validate_transaction, types.FunctionType))

    def test_custom_str(self):
        self.assertEqual(str(self.account), 'Account of Petar with starting amount: 100')

    def test_custom_repr(self):
        self.assertEqual(repr(self.account), 'Account(Petar, 100)')

    def test_custom_len(self):
        self.account.add_transaction(50)
        self.assertEqual(len(self.account), 1)

    def test_custom_iter(self):
        self.account.add_transaction(50)
        self.account.add_transaction(50)
        for t in self.account:
            self.assertEqual(t, 50)

    def test_custom_get_item(self):
        self.account.add_transaction(50)
        self.account.add_transaction(150)
        self.assertEqual(self.account[1], 150)

    def test_custom_gt(self):
        self.assertGreater(self.account, self.account_2)
        self.assertTrue(self.account > self.account_2)

    def test_custom_ge(self):
        self.assertGreaterEqual(self.account, self.account_2)
        self.assertTrue(self.account >= self.account_2)
        self.assertEqual(self.account, self.account_2)

    def test_custom_glt(self):
        self.account_2.add_transaction(50)
        self.assertLessEqual(self.account, self.account_2)
        self.assertTrue(self.account <= self.account_2)

    def test_custom_le(self):
        self.account_2.add_transaction(100)
        self.assertLess(self.account, self.account_2)
        self.assertTrue(self.account < self.account_2)

    def test_custom_eq(self):
        self.account_2.add_transaction(50)
        self.assertEqual(self.account, self.account_2)
        self.assertTrue(self.account == self.account_2)

    def test_custom_ne(self):
        self.assertNotEqual(self.account, self.account_2)
        self.assertTrue(self.account != self.account_2)

    def test_custom_reversed(self):
        self.account.add_transaction(50)
        self.account.add_transaction(150)
        result = list(reversed(self.account))
        self.assertEqual(result, [150, 50])

    def test_custom_add(self):
        account_3 = self.account + self.account_2
        self.assertEqual(repr(account_3), 'Account(Petar&Ines, 150)')
        self.assertEqual(account_3.balance, 150)
        self.assertEqual(account_3.owner, 'Petar&Ines')


if __name__ == "__main__":
    unittest.main()
