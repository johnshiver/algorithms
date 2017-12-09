"""
You are a professional robber planning to rob houses along a street.
Each house has a certain amount of money stashed, the only constraint
stopping you from robbing each of them is that adjacent houses have security
systemi connected and it will automatically contact the police if two adjacent
houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without alerting the police.
"""


def rob(nums):
    import ipdb;ipdb.set_trace()
    f, s = 0, 0
    for n in nums:
	#f, s = s, max(f + n, s)
        f = s
        s = max(f+n, s)
    return s


if __name__ == "__main__":
    print(rob([2, 0, 0, 2]))
