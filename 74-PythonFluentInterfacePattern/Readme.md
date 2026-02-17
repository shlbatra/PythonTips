# Fluent Interface

Method returns itself so you can chain methods.
Ex query(data).filter(x).order_by(...).limit() -> More readable / flow - sequence of things in order.
Ex pandas or sqlalchemy orl or pipeline tools

How things defined and used independent, 

- great fit for sequence of operations where order matters, data pipeline, config flows, query builders
- Not use if one off operation, if not naturally sequential, need strong immutability as each step modified, out of order steps
 
Instead of parallel lists, a fluent interface would chain:                                                                                                                                
                                                                                                                                                                                            
  Before (current):                                                                                                                                                                       
  Animation(steps=[Rotate(60), Move(200,0)], durations=[1.0, 1.0])                                                                                                                          
                                                                                                                                                                                            
  After (fluent):                                                                                                                                                                         
  Animation().rotate(60, duration=1.0).move(200, 0, duration=1.0)                                                                                                                           
                                                                                                                                                                                            
  Each method returns self, enabling chaining like a sentence.  