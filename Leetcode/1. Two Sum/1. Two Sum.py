def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    for  idx, value in enumerate(nums):

        result = target - value
        diff = len(nums) - len(nums[idx+1:])
        if result in nums[idx+1:]:

            final_list = [idx, (nums[idx+1:].index(result)+diff)]
            break

    return final_list
