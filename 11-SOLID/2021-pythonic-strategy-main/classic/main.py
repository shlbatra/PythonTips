from support.app import (CustomerSupport, FILOOrderingStrategy,
                         TicketOrderingStrategy)
from support.ticket import SupportTicket


#create any custom stratergy here and use it without modifying any code
class BlackHoleStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets: list[SupportTicket]) -> list[SupportTicket]:
        return []


def main():
    # create the application
    app = CustomerSupport()

    # create a few tickets
    app.add_ticket(SupportTicket("John Smith", "My computer makes strange sounds!"))
    app.add_ticket(
        SupportTicket("Linus Sebastian", "I can't upload any videos, please help.")
    )
    app.add_ticket(
        SupportTicket("Arjan Codes", "VSCode doesn't automatically solve my bugs.")
    )

    # process the tickets
    #provide stratergy here
    app.process_tickets(FILOOrderingStrategy())


if __name__ == "__main__":
    main()
