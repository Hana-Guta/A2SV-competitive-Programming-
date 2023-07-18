class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpn = ''.join(i.lower() for i in s if i.isalnum())
        reverse = alpn[::-1]
        
        if reverse == alpn:
            return True 
        return False
      
            
       
