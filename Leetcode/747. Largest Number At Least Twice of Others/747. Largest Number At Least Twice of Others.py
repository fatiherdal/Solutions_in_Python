    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        newnums = sorted(list(set(nums)))
        if len(newnums) == 1:
            return 0
        elif newnums[-1] >= newnums[-2]*2:
            large = newnums[-1]
            for i in range(0, len(nums)):
                if nums[i] == large:
                    return i
        else:
            return -1