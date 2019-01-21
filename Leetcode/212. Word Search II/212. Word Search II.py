    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        word_dict = {}
        board_dict = {}
        result_list = []
        
        """
        # FUNCTIONS : 
            1-extract_letter : Creates a dictionary usings elements of 'word' list and 'board' list.
                                keys   : letters of the words
                                values : index numbers (from the board list) corresponding to these letters
            2- letter_check   : checks the neighborly relations of given numbers (index numbers corresponding to the letters)
            
            3- combination    : produces all the possible combinations of given lists (index lists) as long as the result of 'letter_check'is True'
            
            """
        
        def extract_letter(word):
            letter_dict = {}
            for character in set(word):
                letter_list = []
                if word.count(character) > list(board_dict.values()).count(character):
                    break
                else:
                    for key, value in board_dict.items():
                        if character == value:
                            letter_list.append(key)      
                            letter_dict[character] = letter_list
            return letter_dict

        def letter_check(x, y):
            return (y == (x[-1] -10) or y == (x[-1] +10) or y == (x[-1] -1) or y == (x[-1] +1)) and (y not in x)

        def combination(*args):
            result = [[]]
            try:
                pools = [tuple(pool) for pool in args]
                result = [x+[y] for x in result for y in pools[0]]
                for pool in pools[1:]:        
                    result = [x+[y] for x in result for y in pool if letter_check(x,y) == True]
                for prod in result:
                    yield tuple(prod)
            except:
                return result
            
            
        """ # Creates a dictionary from board list. Produces index numbers as keys and assigns characters as values. 
        
        """
        
        for out_idx, outer in enumerate(board):
            for inn_idx, inner in enumerate(outer):
                key = 10*out_idx + inn_idx
                board_dict[key] = inner

        word_dict = {word[::-1] : extract_letter(word) for word in words if len(extract_letter(word))>0}
        new_words = list(word_dict.keys())


        for word in new_words:
            word_list = []
            for i, letter in enumerate(word):
                letter_list = extract_letter(word).get(letter)
                word_list.append(letter_list)
            if tuple(combination(*word_list)) != ():
                result_list.append(word[::-1])
        return sorted(result_list)