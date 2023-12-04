class Solution:
    def largestGoodInteger(self, num: str) -> str:
        max_good = ""
        for i in range(len(num)-2):
            substring = num[i:i+3]
            if substring[0] == substring[1] == substring[2]:
                if max_good == "" or int(substring) > int(max_good):
                    max_good = substring
        
        return max_good

     



        