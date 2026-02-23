from dataclasses import dataclass

from user_repo import AccountStatus

from enum import StrEnum

from typing import Protocol


class AccountStatus(StrEnum):
    ACTIVE = "active"
    SUSPENDED = "suspended"
    CLOSED = "closed"

# define interfacte for user accounts
class UserAccountView(Protocol):
    @property
    def username(self) -> str: ...
    @property
    def email(self) -> str: ...
    @property
    def status(self) -> AccountStatus: ...
    # @property
    # def is_active(self) -> bool: ...
    # @is_active.setter
    # def is_active(self, value: bool) -> None: ...
    # of
    is_active: bool # read and write property

def do_seomething_with_user_account(account: UserAccountView) -> None:
    print("Username:", account.username)
    print("Email:", account.email)
    print("Status:", account.status)
    print("Is active:", account.is_active)
    account.is_active = False

# Using methods for accessing variable
@dataclass
class UserAccount:
    user_id: int
    _username: str
    _email: str
    _status: AccountStatus

    # ---- Methods for everything ----
    # Method - work is happening, but looks expensive to call
    def get_username(self) -> str:
        return self._username

    def get_email(self) -> str:
        return self._email

    def get_status(self) -> AccountStatus:
        return self._status

    # derived state
    def is_active(self) -> bool:
        return self.get_status() is AccountStatus.ACTIVE


# Property
@dataclass
class UserAccount1:
    user_id: int
    _username: str
    _email: str
    _status: AccountStatus

    # ---- Methods for everything ----
    # Communicate cheap and easy to access - just return state
    @property
    def username(self) -> str:
        return self._username

    @property
    def email(self) -> str:
        return self._email

    @property
    def status(self) -> AccountStatus:
        return self._status

    # deterministic and no side effects and reflect status
    # property uses descriptor protocol, defines reading and assigning value; property decorator specific to read - what happens and not have setter
    @property
    def is_active(self) -> bool:
        return self.status is AccountStatus.ACTIVE
    
    # setter for property
    @is_active.setter
    def is_active(self, value: bool) -> None:
        if value:
            self._status = AccountStatus.ACTIVE
        else:
            self._status = AccountStatus.CLOSED
        #self.save() # Not good practice - fail with IO - break property contract - side effect and not deterministic - not just setting value but also doing work, property local and explicit method to save to database

    def save(self) -> None:
        # save to database
        print("Saving to database...")


# ---- Demo ----


def main() -> None:
    account = UserAccount(
        user_id=101,
        _username="mason",
        _email="mason@arjancodes.com",
        _status=AccountStatus.ACTIVE,
    )

    print("Username:", account.get_username())
    print("Email:", account.get_email())
    print("Status:", account.get_status())
    print("Is active:", account.is_active())


    account1 = UserAccount1(
        user_id=101,
        _username="mason",
        _email="mason@arjancodes.com",
        _status=AccountStatus.ACTIVE,
    )
    # account1.is_active = False
    # account1.save() # better to have explicit method to save to database, not have side effect in property setter, not deterministic, not just setting value but also doing work, property local and explicit method to save to database
    do_seomething_with_user_account(account1)
    print("Username:", account1.username)
    print("Email:", account1.email)
    print("Status:", account1.status)
    print("Is active:", account1.is_active)

if __name__ == "__main__":
    main()