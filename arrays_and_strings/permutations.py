
def permute(word):
    if len(word) == 1:
        return [word]

    result = []
    for i, v in enumerate(word):
        result += [v+p for p in permute(word[:i] + word[i+1:])]
    return result


def permuteUnique(nums):
    """
    Given collection of numbers that might contain duplicates,
    return all possible unique permutations.

    solution found in user forum on leetcode
    thanks StefanPochmann!
    """

    ans = [[]]
    for n in nums:
        ans = [l[:i]+[n]+l[i:]
               for l in ans
               for i in xrange((l+[n]).index(n)+1)]
    return ans


if __name__ == '__main__':
    print("Permutations")
    print(permute('abc'))
    print('\n')

    print("Unique Permutations")
    print(permuteUnique([1,1,2]))

