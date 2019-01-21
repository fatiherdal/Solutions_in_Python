    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        total = 0
        for x in set(J):
            total += S.count(x)
        return total
        