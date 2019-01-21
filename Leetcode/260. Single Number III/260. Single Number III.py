    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        once = []
        nums = sorted(nums)
        while i < len(nums):
            if i == len(nums)-1:
                once.append(nums[i])            
                break
            elif nums[i] != nums[i+1]:
                once.append(nums[i])
                i+=1                      
            else:                
                i+=2
        return once