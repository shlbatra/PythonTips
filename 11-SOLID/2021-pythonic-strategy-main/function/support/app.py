import random
from typing import Callable

from support.ticket import SupportTicket

# change to functions -> define what function needs to look like 
#define type alias here 
#class, objects and functions are callables, use object of class with dundar method
# or create method or function
TicketOrderingStrategy = Callable[[list[SupportTicket]], list[SupportTicket]]


def fifo_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return tickets.copy()


def filo_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return list(reversed(tickets))


def random_strategy(tickets: list[SupportTicket]) -> list[SupportTicket]:
    return random.sample(tickets, len(tickets))

"""
if pass parameter - how to use method approach
- can add *args, **kwargs -> but then cust would need to know 

class RandomOrderingStratery:
    seed: Optional[int] = None
    
    def __call__(self, tickets: list[SupportTicket]]) -> list[SupportTicket]:
        random.seed(self.seelf)
        return random.sample(tickets, len(tickets))
        
Call -> app.process_tickets(RandomOrderingStratergy(seed=1))
"""

class CustomerSupport:
    def __init__(self):
        self.tickets: list[SupportTicket] = []

    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        # create the ordered list
        ticket_list = processing_strategy(self.tickets)

        # if it's empty, don't do anything
        if len(ticket_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        # go through the tickets in the list
        for ticket in ticket_list:
            ticket.process()
