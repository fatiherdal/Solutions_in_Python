def missingNumber(self, nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    exp_sum = 0
    for x in range(len(nums)+1):
        exp_sum += x

    missing = exp_sum - sum(nums)
    return missing