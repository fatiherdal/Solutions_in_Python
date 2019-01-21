    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        a_list = list(A)
        b_list = list(B)
        diff = 0
        if len(a_list) == len (b_list):
            if a_list == b_list:
                if len(set(a_list)) == 1:
                    return True
                elif len(set(a_list)) > 1 and len(a_list) > len(set(a_list)):
                    return True
                else:
                    return False
            elif a_list != b_list and sorted(a_list) == sorted (b_list):

                for i in range (0 , len(a_list)):
                    if a_list[i] != b_list[i]:
                        diff = diff + 1                                          
                if diff == 2:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False