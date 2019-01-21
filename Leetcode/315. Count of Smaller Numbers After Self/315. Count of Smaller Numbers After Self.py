    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = []
        for num_idx , num in enumerate(nums):
            check_list = list(sorted(nums[num_idx+1:]))
            try:
                if num > check_list[0]:
                    first = 0
                    if len(check_list) >= 1:     
                        last = len(check_list)
                        while first < last:
                            ctrl_idx = (first + last) // 2
                            if last - first == 1:
                                result.append(last)
                                break
                            elif check_list[ctrl_idx] == num:
                                result.append(ctrl_idx)
                                break
                            elif check_list[ctrl_idx] > num:
                                last = ctrl_idx
                            elif check_list[ctrl_idx] < num:
                                first = ctrl_idx
                    else:
                        result.append(0)
                else:
                    result.append(0)
            except:
                result.append(0)

        return result