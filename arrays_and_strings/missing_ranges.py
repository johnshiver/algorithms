"""
Given a sorted integer array nums, where the range of elements are in the
inclusive range [lower, upper], return its missing ranges.

Example:

Input: nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99,
Output: ["2", "4->49", "51->74", "76->99"]

"""


def findMissingRanges(nums, lower, upper):
	"""
	:type nums: List[int]
	:type lower: int
	:type upper: int
	:rtype: List[str]
	"""
	nums = [lower-1] + nums + [upper+1]
	final = []
	for i in range(len(nums)-1):
		if nums[i] == nums[i+1] or nums[i] + 1 == nums[i+1]:
			continue
		else:
			missing_lower = nums[i]+1
			missing_upper = nums[i+1]-1
			if missing_lower == missing_upper:
				final.append(str(missing_lower))
			else:
				final.append(str(missing_lower) + "->" + str(missing_upper))
	return final
