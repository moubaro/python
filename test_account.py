import pytest
from account import *
class Test:
    def setup(self):
        self.a1 = Account('John')

    def teardown(self):
        del self.a1

    def test_init(self):
        assert self.a1.get_name() == 'John'
        assert self.a1.get_balance() == pytest.approx(0)


    def test_deposit(self):
        self.a1.deposit(1000)
        assert self.a1.get_balance()== pytest.approx(1000)
        assert self.a1.deposit(0) is False
        assert self.a1.get_balance() == pytest.approx(1000)
        assert self.a1.deposit(-1) is False
        assert self.a1.get_balance() == pytest.approx(1000)

    def test_withdraw(self):
        assert self.a1.withdraw(500) is False
        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.withdraw(0) is False
        assert self.a1.get_balance() == pytest.approx(0)
        assert self.a1.withdraw(-1) is False
        assert self.a1.get_balance() == pytest.approx(0)
        self.a1.deposit(200)
        assert self.a1.withdraw(100) is True
        assert self.a1.get_balance()== pytest.approx(10