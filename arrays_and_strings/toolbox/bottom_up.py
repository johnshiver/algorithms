"""
Going bottom-up is a way to avoid recursion, saving the memory cost
that recursion incurs when it builds up the call stack.

A bottom up algorithm 'starts from the beginning' while a recursive
algorithm starts from the end and works backwards.

!! SOMETHING TO WATCH OUT FOR WITH RECURSION !!

Some compilers and interpreters will do what is called
'tail call optimization (TCO)' where it can optimize
some recursive functions to avoid building up a tall call stack.
Python and Java DO NOT use TCO.  Some Ruby implementations do,
but most dont. Some C implementations do, and Javascript recently
allowed TCO.  Scheme is one of the few languages that guarantee TCO
in all implementations. In general, best not to assume your compiler / interpreter
will do this work for you.

Bottom-up is a common strategy for 'dynamic programming' which are problems
where the solution is composed of solutions to the same problem with
smaller inputs. The other common strategy for dynamic programming problems
is memoization.

Bottom up is a way to avoid recursion, saving the memory cost that recursion
incurs when it builds up the call stack.

"""

# Example: multiple all numbers in range 1..n


def product_1_to_n(n):
    # assume n >= 1
    return n * product_1_to_n(n-1) if n > 1 else 1

"""
The issue with the above example is that it builds a call stack of size O(n)
which makes our total memory cost O(n). This makes it vulnerable to
stack overflow error, where the call stack gets too big and runs out of space.

To avoid this, we can go bottom up!
"""


def product_1_to_n(n):
    # assume n >= 1
    result = 1
    for num in range(1, n+1):
        result *= num

    return result

"""
The below question is a a broad class called 'dynamic programming'.  Dynamic programming
is kind of like the next step up from greedy.  You're taking that idea of
'keeping track of what we need in order to update the best answer so far' and applying
it to situations where the new best answer so far might not just have to do with the
previous answer, but 'some other earlier' answer as well.

As you can see in the problem, we kept track of all of our previous answers to smaller
versions of the problem in a big array called ways_of_doing_n_cents

Again, same idea of keeping track of what we need in order to update the answer as we go,
like we did when storing max product of 2, min product of 2, etc. Except now we keep track
of ALL previous answers, which are kept in an array.

"""


# bottom_up solution to change problem
def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1

    for coin in denominations:
        for higher_amount in range(coin, amount + 1):
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += ways_of_doing_n_cents[higher_amount_remainder]

    return ways_of_doing_n_cents[amount]

"""
Here's how ways_of_doing_n_cents would look in successive iterations of our function for

amount=5 and denominations=[1,3,5]

  ===========
key:
a = higher_amount
r = higher_amount_remainder
===========

============
for coin = 1:
============
[1, 1, 0, 0, 0, 0]
 r  a

[1, 1, 1, 0, 0, 0]
    r  a

[1, 1, 1, 1, 0, 0]
       r  a

[1, 1, 1, 1, 1, 0]
          r  a

[1, 1, 1, 1, 1, 1]
             r  a

============
for coin = 3:
=============
[1, 1, 1, 2, 1, 1]
 r        a

[1, 1, 1, 2, 2, 1]
    r        a

[1, 1, 1, 2, 2, 2]
       r        a

============
for coin = 5:
=============
[1, 1, 1, 2, 2, 3]
 r              a


final answer: 3
"""