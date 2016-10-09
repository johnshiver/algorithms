

# solution found on leetcode forum: thanks simkieu!

#-----------------BACKTRACKING---------------------#
#  
#
#
#
#
#
#


class Solution(object):
    def canFindSum(self, nums, target, curSum, ind, n):
        if curSum == target: return True
        if curSum < target:
            for i in xrange(ind, n):
                if self.canFindSum(nums, target, curSum + nums[i], i+1, n):
                    return True
        return False

    def canPartition(self, nums):
        s = sum(nums)
        if s % 2 != 0: return False
        return self.canFindSum(nums, s/2, 0, 0, len(nums))
