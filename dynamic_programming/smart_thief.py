"""
Each type of cake has a weight and a value, stored in a tuple with two indices:

An integer representing the weight of the cake in kilograms
An integer representing the monetary value of the cake in British pounds

You brought a duffel bag that can hold limited weight, and you want to make off with the most valuable haul possible.

Write a function max_duffel_bag_value() that takes a list of cake type tuples and a weight capacity, and returns the maximum monetary value the duffel bag can hold.
"""


def max_duffel_bag_value(capacity, cakes):
    max_value_capacity = [0] * (capacity+1)

    for current_cap in range(1, capacity+1)::
        max_value = 0
        for weight, value in cakes:
            if weight <= current_cap:
                max_value_using_cake = cake_value + max_value_capacity[current_cap-weight]
                max_value = max(max_value, max_value_using_cake)
	max_value_capacity[current_cap] = max_value
    return max_value_capacity[capacity]

