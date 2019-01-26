def topKFrequent(self, nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: List[int]
    """
    freq = {}
    for x in set(nums):
        rep = nums.count(x)
        if rep in freq.keys():
            freq[rep].append(x)
        else:
            freq[rep] = [x]
    key_list = sorted(freq.keys(), reverse=True)
    result = []
    ctrl = 0
    for i in key_list:
        if ctrl < k:
            ctrl = ctrl + len(freq[i])
            result = result + freq[i]
        else:
            break
    return result
