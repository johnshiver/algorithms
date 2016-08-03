"""
This example uses top down to solve the amount left problem

Answer is O(n*m) time and O(n*m) space, where n is the size of amount
and m is the number of items in denominations

Areas of concern:

Because this algorithm is recursive it will build up a 'large call stack'
of size O(m).  It is best to avoid a large stack like this, because it will
cause a stack overflow.

(this means recursion is usually better to avoid for functions that might have
arbitrarily large inputs)

A great way to avoid recursion is to go 'bottom up' which is defined in another module
yout
"""


class Change(object):
    def __init__(self):
        self.memo = {}

    def change_possibilities_top_down(self, amount_left, denominations_left):

        # check memo and short circuit if we've already solved this one
        memo_key = str((amount_left, denominations_left))
        if memo_key in self.memo:
            print('grabbing memo [%s]' % memo_key)
            return self.memo[memo_key]

        # base cases:
        # we hit the amount spot on. hurray!
        if amount_left == 0: return 1

        # overshot the amount left (used too many coins)
        if amount_left < 0: return 0

        # we're out of denominations
        if len(denominations_left) == 0: return 0

        print("check ways to make %i with %s" % amount_left, denominations_left)

        # choose a current coin
        current_coin, rest_of_coins = denominations_left[0], denominations_left[1:]

        # see how many possibilities we can get
        # for each number of times to use current coin
        num_possibilities = 0
        while amount_left >= 0:
            num_possibilities += self.change_possibilities_top_down(amount_left, rest_of_coins)
            amount_left -= current_coin

        # save answer in memo so we dont comput it again
        self.memo[memo_key] = num_possibilities
        return num_possibilities
