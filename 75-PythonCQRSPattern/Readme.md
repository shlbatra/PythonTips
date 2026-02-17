# Command Query Responsibility Segregation

Commands - change state - Write state
Query - read state 

These 2 things can be different and optimized different. 
Works well with event sourcing.

1 fast api app
1 mongo db with 2 collections - 1 for reading tickets and other for modifying tickets.

Read and write models can evolve independently; Read is eventually consistent by design; Read lags behind Write, Also handle failure by retry / replay.
Same id across collections to keep projections simple and traceful.
Create seperate databses for read / write based on requirements - Read and write requirement diverges.


  What is CQRS?                                                                                                                                                                                        
                                                                                                                                                                                                       
  ┌─────────────────────────────────────────────────────────────────────┐                                                                                                                              
  │                        Traditional Approach                         │                                                                                                                              
  │                                                                     │                                                                                                                              
  │    ┌─────────┐                      ┌────────────────┐              │                                                                                                                              
  │    │  API    │ ──── Read/Write ──── │  One Database  │              │                                                                                                                              
  │    └─────────┘                      │   (tickets)    │              │                                                                                                                              
  │                                     └────────────────┘              │                                                                                                                              
  └─────────────────────────────────────────────────────────────────────┘                                                                                                                              
                                                                                                                                                                                                       
  ┌─────────────────────────────────────────────────────────────────────┐                                                                                                                              
  │                          CQRS Approach                              │                                                                                                                              
  │                                                                     │                                                                                                                              
  │    ┌─────────┐                                                      │                                                                                                                              
  │    │Commands │ ──── Write ───→ ┌──────────────────┐                 │                                                                                                                              
  │    │(Create, │                 │ ticket_commands  │ (Source of      │                                                                                                                              
  │    │ Update) │                 │ (full data)      │  Truth)         │                                                                                                                              
  │    └─────────┘                 └────────┬─────────┘                 │                                                                                                                              
  │                                         │                           │                                                                                                                              
  │                                    Projector                        │                                                                                                                              
  │                                         │                           │                                                                                                                              
  │    ┌─────────┐                 ┌────────▼─────────┐                 │                                                                                                                              
  │    │ Queries │ ◀─── Read ───── │  ticket_reads    │ (Optimized      │                                                                                                                              
  │    │ (List,  │                 │ (preview, flags) │  for queries)   │                                                                                                                              
  │    │Dashboard│                 └──────────────────┘                 │                                                                                                                              
  │    └─────────┘                                                      │                                                                                                                              
  └─────────────────────────────────────────────────────────────────────┘                                                                                                                              
                                                                                                                                                                                                       
  ---                                                                                                                                                                                                  
  Simple Example: Creating a Ticket                                                                                                                                                                    
                                                                                                                                                                                                       
  Before (No CQRS) - before.py:                                                                                                                                                                        
  User creates ticket                                                                                                                                                                                  
          │                                                                                                                                                                                            
          ▼                                                                                                                                                                                            
  ┌───────────────────┐                                                                                                                                                                                
  │   tickets coll    │  ← One collection for everything                                                                                                                                               
  │  - customer_id    │                                                                                                                                                                                
  │  - subject        │                                                                                                                                                                                
  │  - message        │  ← Full message stored                                                                                                                                                         
  │  - status         │                                                                                                                                                                                
  │  - agent_note     │                                                                                                                                                                                
  │  - created_at     │                                                                                                                                                                                
  └───────────────────┘                                                                                                                                                                                
          │                                                                                                                                                                                            
          ▼                                                                                                                                                                                            
  List query must:                                                                                                                                                                                     
    1. Fetch message field                                                                                                                                                                             
    2. Compute preview every time  ← Expensive!                                                                                                                                                        
    3. Check if agent_note exists  ← Every request!                                                                                                                                                    
                                                                                                                                                                                                       
  After (With CQRS) - after.py:                                                                                                                                                                        
  User creates ticket                                                                                                                                                                                  
          │                                                                                                                                                                                            
          ▼                                                                                                                                                                                            
  ┌────────────────────┐                                                                                                                                                                               
  │ ticket_commands    │ ← Source of truth (write model)                                                                                                                                               
  │  - customer_id     │                                                                                                                                                                               
  │  - subject         │                                                                                                                                                                               
  │  - message         │                                                                                                                                                                               
  │  - status          │                                                                                                                                                                               
  │  - agent_note      │                                                                                                                                                                               
  └─────────┬──────────┘                                                                                                                                                                               
            │                                                                                                                                                                                          
      project_ticket()  ← Projector transforms data ONCE                                                                                                                                               
            │                                                                                                                                                                                          
            ▼                                                                                                                                                                                          
  ┌────────────────────┐                                                                                                                                                                               
  │ ticket_reads       │ ← Read model (optimized)                                                                                                                                                      
  │  - subject         │                                                                                                                                                                               
  │  - status          │                                                                                                                                                                               
  │  - preview         │ ← Pre-computed! No recalculation                                                                                                                                              
  │  - has_note        │ ← Pre-computed boolean!                                                                                                                                                       
  └────────────────────┘                                                                                                                                                                               
            │                                                                                                                                                                                          
            ▼                                                                                                                                                                                          
  List query is now:                                                                                                                                                                                   
    - Just fetch ready-to-use fields                                                                                                                                                                   
    - No computation needed!                                                                                                                                                                           
                                                                                                                                                                                                       
  ---  