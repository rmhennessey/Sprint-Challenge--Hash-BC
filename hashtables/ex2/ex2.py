#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    #initialize ht
    hashtable = HashTable(length)
    #initialize route
    route = [None] * length

    """
    YOUR CODE HERE
    """
    # loop thru tix & insert to ht
    for ticket in tickets:
        hash_table_insert(hashtable, ticket.source, ticket.destination)
    # set the first trip
    first_trip = hash_table_retrieve(hashtable, "NONE")
    route[0] = first_trip

    # loop thru remaining trips

    for i in (num + 1 for num in range(len(route) - 1)):
        route[i] = hash_table_retrieve(hashtable, route[i-1])

    return route
