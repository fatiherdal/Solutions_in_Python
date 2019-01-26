def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    result = 0
    jump = False
    for i in range(len(s)):
        if jump == False:
            if i < len(s)-1:
                if s[i] == 'M':
                    result = result + 1000
                elif s[i] == 'D':
                    result = result + 500
                elif s[i] == 'C':
                    if s[i+1] == 'D':
                        result = result + 400
                        jump = True
                    elif s[i+1] == 'M':
                        result = result + 900
                        jump = True
                    else:
                        result = result + 100
                elif s[i] == 'L':
                    result = result + 50    
                elif s[i] == 'X':
                    if s[i+1] == 'L':
                        result = result + 40
                        jump = True
                    elif s[i+1] == 'C':
                        result = result + 90
                        jump = True                
                    else:
                        result = result + 10
                elif s[i] == 'V':
                    result = result + 5
                elif s[i] == 'I':
                    if s[i+1] == 'V':
                        result = result + 4
                        jump = True
                    elif s[i+1] == 'X':
                        result = result + 9        
                        jump = True
                    else:
                        result = result + 1
            else:
                if s[i] == 'M':
                    result = result + 1000
                elif s[i] == 'D':
                    result = result + 500
                elif s[i] == 'C':
                     result = result + 100
                elif s[i] == 'L':
                    result = result + 50    
                elif s[i] == 'X':
                    result = result + 10
                elif s[i] == 'V':
                    result = result + 5
                elif s[i] == 'I':
                    result = result + 1
        else:
            jump = False
    return result