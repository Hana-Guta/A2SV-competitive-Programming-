class Solution:
    def interpret(self, command: str) -> str:
       intd = command.replace("()" , "o")
       intd = intd.replace("(al)" , "al")
       return intd

        
        