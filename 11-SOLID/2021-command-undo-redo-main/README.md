## Command pattern with undo and redo

This repository contains the example code of the Command pattern with undo and redo. 

- represent commands that have control over when they are executed and build undo / redo behavior
- behavioral pattern that provides way to encapsulate all knowledge about performing certain operation into single object 
- Ex.transactions in banking system flexible and how to undo/redo behaviour to it 
- Basic Command Pattern App ->
    - transaction protocol 
    - classes implement that protocol (command class)
    - controller class to control the execution of those commands
    - implement undo/redo at transaction level
    - txn is a thing make it even more flexible - grp or batches of commands that seamingly integrate 
    - command is a thing - store / organize and structure
    - system - time/date batch execute can be scheduled 
- Used in non destructive editing programs like Video, audio editors
- Can store state and transaction history as well. 
- balance get on account and also recreate from transaction history ? Which one is true ? 
- In this example use state. 
