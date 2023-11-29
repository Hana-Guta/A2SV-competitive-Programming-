class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        x = 16 
        mn = 0

        while x >= 0:
            yehone = 3 ** x
            if yehone + mn < n:
                mn += yehone
            elif yehone + mn == n:
                return True
            x -= 1
            
        return False 
       

      
        


        