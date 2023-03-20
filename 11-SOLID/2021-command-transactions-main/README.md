## Command pattern with transactions as the ground truth

This repository contains the example code of the Command pattern with transactions as the ground truth. 

- Command Pattern 
- Can store state and transaction history as well. 
- balance get on account and also recreate from transaction history ? Which one is true ? 
- In the example use state. 
- in today's example, we use history - Impact on how you design your application 
- Make commands on objects then do different things with them - undo, redo or schedule them 
- data stored -> bank and accounts with balance, undo and redo set of txns -> hard to get list of txns 
- 1. store array of history of txns - another thing track with unod/redo and redundancy -> acct balance or history - which use 
- 2. acct balance not ground truth but list of txns is -> change design pattern 
- txn based system - not execute commands immediately but at a later date & not worry about balance - simplify undo/redo as store txns 
- state based systen 
    - easier to view current balance (current state)
- txn based system 
    - easier to modify things ex. undo/redo 
    - clear cache of accts that are being affected
    - recompute cache every couple of mins 
    - once a year, recalculcate txn and store it and reuse from that pt. 
    - Ex. non destructive programs
    - final cut pro video editing programs -> not modify original video but applies effects and transformations on them and renders results into movie file
    - computer animation-base animation and apply tranformation / map to diff character or move in space - tranform animation data using command design pattern 
    - 3d modelling tools -> texture / model / animation - apply effects and render to movie file - render calculate balance cache
    - design softare - dont take state as default ground truth, take txn as ground truth - better fit