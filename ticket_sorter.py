from itertools import permutations


class Ticket:
    def __init__(self, depart, arrive):
        self.depart = depart
        self.arrive = arrive
        
    def __repr__(self):
        return f'({self.depart}, {self.arrive})'
    
    @property
    def as_tuple(self):
        return self.depart, self.arrive


def sort_tickets_slow(tickets):
    '''Brute force method.
    Create all permutations of the tickets and
    find the one that is in order.'''
    
    ticket_permutations = list(permutations(tickets, len(tickets)))
    for i in range(len(ticket_permutations)):
        tickets_in_order = 1
        tickets_to_check = ticket_permutations[i]
        for j in range(len(tickets) - 1):
            if tickets_to_check[j].arrive == tickets_to_check[j + 1].depart:
                tickets_in_order += 1
            else:
                break

        if tickets_in_order == len(tickets):
            break

    return tickets_to_check


def sort_tickets_fast(tickets):
    '''The more elegant method.
    Find the start city using the difference of two sets.
    Append the tickets to the starting ticket.'''
    
    unique_cities = {item for sublist in (ticket.as_tuple for ticket in tickets) for item in sublist}
    arrival_cities = {ticket.arrive for ticket in tickets}
    start_city = unique_cities.difference(arrival_cities)
    start_ticket_num = [i for i, v in enumerate(tickets) if v.depart in start_city][0]
    sorted_tickets = [tickets.pop(start_ticket_num)]

    while len(tickets) >= 1:
        for i in range(len(tickets)):
            if sorted_tickets[-1].arrive == tickets[i].depart:
                break
                
        sorted_tickets.append(tickets.pop(i))
        
    return sorted_tickets


def format_itinerary(tickets):
    result_list = [ticket.depart for ticket in tickets]
    result_list.append(tickets[-1].arrive)
    return ' -> '.join(result_list)


# Test Data
ticket1 = Ticket('OAK', 'AUS')
ticket2 = Ticket('AUS', 'EWR')
ticket3 = Ticket('EWR', 'PHL')

# Solution string
solution = 'OAK -> AUS -> EWR -> PHL'

# Test code for all possible cases using slow method
assert solution == format_itinerary(sort_tickets_slow([ticket1, ticket2, ticket3]))
assert solution == format_itinerary(sort_tickets_slow([ticket1, ticket3, ticket2]))
assert solution == format_itinerary(sort_tickets_slow([ticket2, ticket1, ticket3]))
assert solution == format_itinerary(sort_tickets_slow([ticket2, ticket3, ticket1]))
assert solution == format_itinerary(sort_tickets_slow([ticket3, ticket2, ticket1]))
assert solution == format_itinerary(sort_tickets_slow([ticket3, ticket1, ticket2]))

# Test code for all possible cases using fast method
assert solution == format_itinerary(sort_tickets_fast([ticket1, ticket2, ticket3]))
assert solution == format_itinerary(sort_tickets_fast([ticket1, ticket3, ticket2]))
assert solution == format_itinerary(sort_tickets_fast([ticket2, ticket1, ticket3]))
assert solution == format_itinerary(sort_tickets_fast([ticket2, ticket3, ticket1]))
assert solution == format_itinerary(sort_tickets_fast([ticket3, ticket2, ticket1]))
assert solution == format_itinerary(sort_tickets_fast([ticket3, ticket1, ticket2]))
