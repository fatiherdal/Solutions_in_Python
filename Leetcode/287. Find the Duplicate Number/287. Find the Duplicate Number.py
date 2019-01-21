    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from numpy import array 
        np_nums = array(sorted(nums))
        np_dummy =array(range(1,len(nums)+1))
        print(np_nums)
        print(np_dummy)
        merge = list(array(np_nums - np_dummy))
        
        return merge.index(-1)