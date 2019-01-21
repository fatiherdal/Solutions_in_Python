    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        new_nums = [num for num in sorted(nums) if num > 0 ]
        if len(new_nums) > 0:
            for x in range(1, new_nums[-1]+2):
                if x not in new_nums:
                    return x
                    break
        else:
            return 1