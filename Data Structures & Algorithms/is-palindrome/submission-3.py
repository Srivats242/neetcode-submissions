class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        # Whole base intial point of comparison to even begin the process of checking if its a palindrome or not
        # Is left < right or right > left to start comparison process
        while l < r:
            while l < r and not self.alphaNum(s[l]):
                # If left character is not an alphanumeric character and left < right counter, left counter increments
                l += 1
            while r > l and not self.alphaNum(s[r]):
                # If right character is not an alphanumeric character and right > left counter, right counter decrements
                r -= 1
            if s[l].lower() != s[r].lower():
                # Returns false indicating its not a palindrome as alphanumeric characters aren't equal to one another
                return False
            # Else keep incrementing left and decrementing right
            l, r = l + 1, r - 1
        # Entire loop finishes which means it is a palindrome and we can return true to indicate it is a palindrome
        return True
    def alphaNum(self, c): # Check to see if a character is alphanumeric or not
        # ord - Returns ASCII value of a character and if character ASCII value between ASCII value range
        # for uppercase, lowercase and numeric characters, then it is alphanumeric for sure
        return (ord('A') <= ord(c) <= ord('Z') or
        ord('a') <= ord(c) <= ord('z') or ord('0') <= ord(c) <= ord('9'))
                    

                
               
               

        
