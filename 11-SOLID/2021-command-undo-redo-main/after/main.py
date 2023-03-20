from banking.bank import Bank
from banking.commands import Batch, Deposit, Transfer, Withdrawal
from banking.controller import BankController


def main() -> None:

    # create a bank
    bank = Bank()

    # create a bank controller
    controller = BankController()

    # create some accounts
    account1 = bank.create_account("ArjanCodes")
    account2 = bank.create_account("Google")
    account3 = bank.create_account("Microsoft")

    # deposit some money in my account
    controller.execute(Deposit(account1, 100000))
    #controller.execute(Deposit(account2, 100000))
    #controller.execute(Transfer(from_account=account2, to_account=account1, amount=50000))
    ##controller.execute(Withdraw(account1, 150000))
    controller.undo()
    controller.redo()

    # execute a batch of commands - can have nested batches -> command 
    controller.execute(
        Batch(
            commands=[
                Deposit(account2, 100000),
                Deposit(account3, 100000),
                # Withdrawal(account1, 100000000),
                Transfer(account2, account1, 50000),
            ]
        )
    )

    # undo and redo
    controller.undo()  #undo all batch commands
    controller.undo()
    controller.redo()
    controller.redo()

    # get the money out of my account
    controller.execute(Withdrawal(account1, 150000))
    controller.undo()
    print(bank)


if __name__ == "__main__":
    main()
