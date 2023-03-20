from dataclasses import dataclass, field

from banking.transaction import Transaction

#keeping track of transactions without executing them. compute_balance executes them  
@dataclass
class BankController:
    ledger: list[Transaction] = field(default_factory=list)  # transaction history
    current: int = 0  #pointer - position in ledger where we are 

    # register new txn in ledger here -> ledger where keep transaction history
    def register(self, transaction: Transaction) -> None:
        #ex 3 txns -> undo one - current pts to last and then add new txn - remove last txn 
        del self.ledger[self.current :]  #clear redo stack when add new txn , delete txn after current stack (index)
        self.ledger.append(transaction)
        self.current += 1

    def undo(self) -> None:  #keep track of where we are on ledger, go step back using pointer called current
        if self.current > 0:
            self.current -= 1

    def redo(self) -> None:
        if self.current < len(self.ledger): #room to redo things
            self.current += 1

    def compute_balances(self) -> None: #this method executes transactions and get balance
        for transaction in self.ledger[: self.current]:
            transaction.execute()
