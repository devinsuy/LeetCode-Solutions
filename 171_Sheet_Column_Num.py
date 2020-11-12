class Solution:
    letter_values = {"A" : 1}   # Cache values
    A_ASCII = ord("A")

    def get_value(self, letter):
        if letter in letter_values:
            return letter_values[letter]

        else: # Calculate value and cache it for later use
            dist_from_a = ord(letter) - A_ASCII
            numerical_value = 1 + dist_from_a           # We know "A" holds the value 1
            letter_values[letter] = numerical_value     # Cache the letter

            return numerical_value 


    def titleToNumber(self, s: str) -> int:
        start_pos = len(s) - 1
        col_value = 0
        index = 0
        
        # current_value : 26^position * letter_value
        # Position is descending where rightmost letter is positon 0
        # Index is ascending where leftmost letter is index 0
        for position in range(start_pos,-1,-1):
            current_letter = s[index]
            index += 1

            current_value = (26**position) * self.get_value(current_letter)
            col_value += current_value
        
        return col_value

