#Controller class allows us to execute commands
#uses bank to execute transactions
#managing undos and redos as well -> keep track of this list , rollback and go back to prev state

from dataclasses import dataclass, field

from banking.transaction import Transaction


@dataclass
class BankController:
    undo_stack: list[Transaction] = field(default_factory=list)  #list to keep track so know what do when undo/redo something
    redo_stack: list[Transaction] = field(default_factory=list)

    def execute(self, transaction: Transaction) -> None:
        transaction.execute()  #execute transaction
        self.redo_stack.clear() #when do new txn, clear redo stack as not redo prev txn 
        self.undo_stack.append(transaction) #add txn so can undo if reqd 

    def undo(self) -> None: #undoes last txn
        if not self.undo_stack:  #if nothing undo, then do nothing 
            return
        transaction = self.undo_stack.pop()  #get last txn 
        transaction.undo()
        self.redo_stack.append(transaction)  #add so redo anything that we have undone 

    def redo(self) -> None:   #redo last txn 
        if not self.redo_stack:
            return
        transaction = self.redo_stack.pop()
        transaction.execute()
        self.undo_stack.append(transaction)
