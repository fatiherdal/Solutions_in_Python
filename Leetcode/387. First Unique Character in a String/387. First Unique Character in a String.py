def firstUniqChar(self, s):
    """
    :type s: str
    :rtype: int
    """
    result = None
    if len(s) < 1:
        result = -1
    else:
        for x, i  in enumerate(s):
            if s.count(i) == 1:
                result = x
                break
            else:
                result = -1
    return result