"""
a child is running up a staircase with n steps adn hop either
1 step, 2 steps, or 3 steps at a time.  Implement a method
to count how many possible ways the child can run up the stairs.
"""

def method_helper(x):
    memo = [-1] * (x+1)
    return triple_hop(x, memo)


def triple_hop(x, memo):

    if x < 0: return 0

    memo[0] = 1

    if x >= 1:
        memo[1] = 1
    if x >= 2:
        memo[2] = memo[1] + memo[0]
    if x > 2:
        for i in range(3, x+1):
            memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    return memo[x]


if __name__ == "__main__":
    print method_helper(10)
