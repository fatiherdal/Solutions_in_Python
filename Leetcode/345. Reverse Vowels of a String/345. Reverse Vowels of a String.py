    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels= ['a','A','e','E','i','I','o','O','u','U']
        word = list(s)
        indx = []
        revindx =[]
        newword = tuple(word)
        for i in range (0,len(word)):
            if word[i] in vowels:
                indx.append(i)
        if len(indx) > 1:
            revindx = indx[::-1]
            print(len(indx))
            for i in range (len(indx)):
                print(newword[indx[i]])
                word[revindx[i]] = newword[indx[i]]
        return ''.join(word)
        