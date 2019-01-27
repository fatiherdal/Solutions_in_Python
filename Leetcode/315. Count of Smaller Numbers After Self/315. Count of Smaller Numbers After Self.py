def countSmaller(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    replica = nums
    result = []
    for x in range (len(nums)):
        check_num = replica.pop(0)
        ctrl = 0
        for n in replica:
            if n < check_num:
                ctrl += 1
        result.append(ctrl)
    return result
