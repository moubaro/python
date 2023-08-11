"""
A class representing details of someone account
"""
def __init__(self, name:str) -> None:
    """
    function to get name and set balance to 0
    :param self: self
    :param name: name
    """
    self.__account_name = name
    self.__account_balance = 0


def deposit(self, amount:float)-> bool:
    """
    function to add amount to balance
    :param self: self
    :param amount: amount added
    :return: true for account balance
    """
    if amount > 0:
        self.__account_balance += amount
        return True
    else:
        return False


def withdraw(self, amount:float) -> bool:
    """
    function to withdraw amount from balance
    :param self: self
    :param amount: amount to be withdrawn
    :return: true if amount is less than bal and more than 0
        """
    if amount <= self.__account_balance and amount > 0:
        self.__account_balance -= amount
        return True
    else:
        return False


def get_balance(self) -> float:
    """
    :return: account balance
    """
    return self.__account_balance


def get_name(self) -> str:
    """
    :return: account name
    """
    return self.__account_name



















def __init__(self, name):
    self.__account_name = name
    self.__account_balance = 0

def deposit(self, amount):
    if amount > 0:
        self.__account_balance += amount
        return True
    else:
        return False

def withdraw(self, amount):
    if amount <= self.__account_balance and amount > 0:
        self.__account_balance -= amount
        return True
    else:
        return False


def get_balance(self):
    return self.__account_balance
    
def get_name(self):
    return self.__account_name