
def make_change(amount, coins):
    """
    given an amount and coin denominations,
    return number of ways in which to make amount
    """

    possibles = [0] * (amount+1)
    possibles[0] = 1

    for coin in coins:
        for higher_amount in range(coin, amount+1):
            diff = higher_amount - coin
            possibles[higher_amount] += possibles[diff]
    return possibles[amount]

if __name__ == "__main__":
    print(make_change(122, [1, 3, 5, 22, 25]))
