def titleToNumber(self, s):
    """
    :type s: str
    :rtype: int
    """
    alpha  = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    factor = len(s) - 1
    result = 0
    if len(s) > 1:
        for i in s[:-1]:
            self = alpha.index(i)+1
            result = result + ((26**factor) * self)
            factor -=1
        result = result + alpha.index(s[-1]) + 1
    else:
        result = result + alpha.index(s[-1]) + 1
    return result