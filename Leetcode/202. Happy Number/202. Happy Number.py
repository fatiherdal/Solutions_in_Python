def isHappy(self, n):
    """
    :type n: int
    :rtype: bool
    """
    happy = False
    cycle = []
    while happy == False:
        a = str(n)
        total = 0
        for i in a:
            x = int(i)
            total += x**2
        if total == 1:
            happy = True
        elif total in cycle:
            break
        else:
            n = total
            cycle.append(total)
    return happy