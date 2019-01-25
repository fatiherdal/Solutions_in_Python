def sortedSquares(self, A):
    """
    :type A: List[int]
    :rtype: List[int]
    """
    result = []
    for i in A:
        result.append(abs(i)**2)
    return sorted(result)