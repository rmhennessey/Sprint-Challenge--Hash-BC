#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)

    """
    YOUR CODE HERE
    """
    # add first weight to ht
    hash_table_insert(ht, weights[0], 0)
    # initialize current index
    current_index = 1
    # loop through adding weights & checking
    while current_index < length:
        current_weight = weights[current_index]
        # insert weight to ht
        hash_table_insert(ht, current_weight, current_index)
        # find weight limit of pair
        limit_pair = limit - current_weight
        # see if pair exists
        exists = hash_table_retrieve(ht, limit_pair)
        if exists:
            if current_index == 1:
                return (current_index, 0)
            # order so larger number is first
            elif exists > current_index:
                return(exists, current_index)
            else:
                return (current_index, exists)
        #increment
        current_index +=1
    return None


def print_answer(answer):
    if answer is None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
