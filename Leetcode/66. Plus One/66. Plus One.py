    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strnums = []
        final = []
        for x in digits:
            strnums.append(str(x))
        strnums = list (str(int (''.join(strnums)) + 1))
        for x in strnums:
            final.append(int(x))
        return final
        