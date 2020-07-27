'''Brute force solution to sort mixed-up plane tickets.'''

from itertools import permutations

class Ticket:
    def __init__(self, depart, arrive):
        self.depart = depart
        self.arrive = arrive

    def __repr__(self):
        return f'({self.depart}, {self.arrive})'

def sort_tickets(tickets):
    ticket_permutations = list(permutations(tickets, len(tickets)))
    for i in range(len(ticket_permutations)):
        tickets_in_order = 1
        tickets_to_check = ticket_permutations[i]
        for j in range(len(tickets) - 1):
            if tickets_to_check[j].arrive == tickets_to_check[j + 1].depart:
                tickets_in_order += 1

        if tickets_in_order == len(tickets):
            break

    return tickets_to_check

def format_itinerary(tickets):
    result_list = [x.depart for x in tickets]
    result_list.append(tickets[-1].arrive)
    return ' -> '.join(result_list)


# Test Data
ticket1 = Ticket('OAK', 'AUS')
ticket2 = Ticket('AUS', 'EWR')
ticket3 = Ticket('EWR', 'PHL')

# Solution string
solution = 'OAK -> AUS -> EWR -> PHL'

# Test code for all possible cases
assert solution == format_itinerary(sort_tickets([ticket1, ticket2, ticket3]))
assert solution == format_itinerary(sort_tickets([ticket1, ticket3, ticket2]))
assert solution == format_itinerary(sort_tickets([ticket2, ticket1, ticket3]))
assert solution == format_itinerary(sort_tickets([ticket2, ticket3, ticket1]))
assert solution == format_itinerary(sort_tickets([ticket3, ticket2, ticket1]))
assert solution == format_itinerary(sort_tickets([ticket3, ticket1, ticket2]))
