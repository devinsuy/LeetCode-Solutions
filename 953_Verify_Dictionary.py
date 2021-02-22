'''
Input: a list of words, a 26 long character sequence of the letter ordering
Ouput: boolean, whether or not the words are sorted lexical based on given order

In lexical sorting the first letter of both words are compared, if same then 2nd, if same then 3rd ...


- Map each letter to its position score -> order[0] : 0, ... , order[25] : 25

- Sliding window, left = 0, right = 1, both pointers increment by 1 each pass

- Compare word[left] and word[right]
    - Compare length = min(len(word[left]), len(word[right]))
    - We only need to compare as many characters as there are in the shorter of the two words
    - Start at the front of both words, score(word[left]) must be >= score(word[right]) for each letter
        - If at any point this is false, return false
        - If compare length finishes, they are sorted properly, advance pointers to next word, left = right, right = right+1
        
Edge cases:
    - Words not same length 
    - Single letter word
    - Words.length = 1 -> return true singleton is always sorted
    - Comparing two identical words, use score(left) less than OR EQUAL score(right)
        - The same word consecutively is still sorted lexically
    - Words have identical prefix but are not the same length, shorter word comes first lexically

'''

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        # Singleton is always sorted
        if(len(words) == 1):
            return True
        
        # Map letter to its position score
        letterScore = {}
        for i, letter in enumerate(order):
            letterScore[letter] = i
        
        # Begin checking words
        left = 0
        right = 1
        while(right < len(words)):
            leftWord = words[left]
            rightWord = words[right]
            checkLen = min(len(leftWord), len(rightWord))
            
            # The words have identical prefix, the shorter word must be to the left
            if(leftWord[:checkLen] == rightWord[:checkLen]):
                if(len(leftWord) > len(rightWord)):
                    return False
                
            # Compare the two words, return false if not in order
            for i in range(checkLen):
                # The right word is greater lexically than the left, no further check needed
                if(letterScore[rightWord[i]] > letterScore[leftWord[i]]):
                    break
                # The right word is not greater at this letter, the left must be <= the right at this letter
                if(letterScore[leftWord[i]] > letterScore[rightWord[i]]):
                    return False
            
            
            # Advance pointers to next words
            left += 1
            right += 1
        
        return True
        
        
        
        
        
        
        
        