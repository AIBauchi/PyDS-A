"""
Author: Rathish Rajendran

knapsack.py - A Python implementation of the 0/1 knapsack algorithm.

This script provides a python function named "knapsack_zero_one" that takes in the
following parameters:
1. capacity of knapsack 
2. weight of each item
3. profit associated with each item
4. total number of items

and provides the maximum profit that can be achieved. 
"""

def knapsack_zero_one( capacity_of_knapsack, weight_of_items, profit_of_items, item_number ):
    """
    capacity_of_knapsack : A single value denoting the total capacity of the knapsack
    weight_of_items      : A list denoting the weight of each item
    profit_of_items      : A list denoting the profit of each item
    item_number          : This denotes the total number of items. 
                           It also denotes the current item being processed
    """

    if capacity_of_knapsack == 0 or item_number == 0:
        return 0
    
    # Check if the item cannot be incuded in the knapsack.
    # Do this by checking if the specific item's weight
    # exceeds the total capacity of the knapsack
    if weight_of_items[item_number - 1] > capacity_of_knapsack:
        return knapsack_zero_one( capacity_of_knapsack, weight_of_items, profit_of_items, item_number-1 )
    
    # If the item can be included in the knapsack, check whether including
    # the item or not including the item will give us maximum profit. 
    # Return the maximum profit that is produced by including/not including the item
    else:
        return max( 
            profit_of_items[ item_number - 1 ] + 
            knapsack_zero_one( 
                capacity_of_knapsack - weight_of_items[ item_number-1 ],
                weight_of_items, profit_of_items, item_number-1  
            ),
            knapsack_zero_one( capacity_of_knapsack, weight_of_items, profit_of_items, item_number-1 )
        )

