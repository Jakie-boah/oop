import unittest

from .ex import *


class CompositeBankAccountCommand(Command, list):
    def __init__(self, items=[]):
        super().__init__(items)
        for item in self:
            self.append(item)

    def invoke(self):
        for x in self:
            x.invoke()

    def undo(self):
        for x in reversed(self):
            x.undo()


class MoneyTransferCommand(CompositeBankAccountCommand):
    def __init__(self, from_acct, to_acct, amount):
        super().__init__([
            BankAccountCommand(from_acct, BankAccountCommand.Action.WITHDRAW, amount),
            BankAccountCommand(to_acct, BankAccountCommand.Action.DEPOSIT, amount)
        ])

    def invoke(self):
        ok = True
        for cmd in self:
            if ok:
                cmd.invoke()
                ok = cmd.success
            else:
                cmd.success = False
        self.success = ok


class TestSuite(unittest.TestCase):
    def test_composite_deposit(self):
        ba = BankAccount()
        deposit1 = BankAccountCommand(
            ba, BankAccountCommand.Action.DEPOSIT, 100
        )
        deposit2 = BankAccountCommand(
            ba, BankAccountCommand.Action.DEPOSIT, 50
        )
        composite = CompositeBankAccountCommand(
            [deposit1, deposit2]
        )
        composite.invoke()
        print(ba)
        composite.undo()
        print(ba)

    def test_transfer_fail(self):
        ba1 = BankAccount(100)
        ba2 = BankAccount()

        amount = 100
        wd = BankAccountCommand(
            ba1, BankAccountCommand.Action.WITHDRAW, amount
        )
        dc = BankAccountCommand(
            ba2, BankAccountCommand.Action.DEPOSIT, amount
        )
        transfer = CompositeBankAccountCommand([wd, dc])
        transfer.invoke()
        print(f'ba1: {ba1}, ba2: {ba2}')
        transfer.undo()
        print(f'ba1: {ba1}, ba2: {ba2}')


if __name__ == '__main__':
    unittest.main()
