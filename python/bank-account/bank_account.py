from threading import Lock
from queue import SimpleQueue


class BankAccount:

    str_acc_not_open = "Account not Open/Active !!"
    str_acc_already_open = "Account is already Open/Active !!"
    str_acc_already_closed = "Account is already Closed !!"

    def __init__(self):
        self._balance = None
        self._mutex = Lock()

    def _verify_active(self, exc_txt=None):
        if self._balance is None:
            raise ValueError(exc_txt or "Account not Open/Active !!")

    def _verify_inactive(self, exc_txt=None):
        if self._balance is not None:
            raise ValueError(exc_txt or "Account already Open !!")

    def _validate_val(self, val):
        if val < 0:
            raise ValueError("Invalid transaction !!")

    @property
    def balance(self):
        self._verify_active()
        return self._balance

    def debit(self, val):
        self._validate_val(val)
        self._update_balance(-val)

    def credit(self, val):
        self._validate_val(val)
        self._update_balance(val)

    def _update_balance(self, val):
        self._verify_active()
        self._validate_val(self._balance + val)
        self._balance += val

    def get_balance(self):
        return self.balance

    def open(self):
        self._verify_inactive()
        with self._mutex:
            self._balance = 0

    def deposit(self, amount):
        with self._mutex:
            self.credit(amount)

    def withdraw(self, amount):
        with self._mutex:
            self.debit(amount)

    def close(self):
        self._verify_active("Account already closed !!")
        with self._mutex:
            self._balance = None

    def __del__(self):
        self._balance is None or self.close()
