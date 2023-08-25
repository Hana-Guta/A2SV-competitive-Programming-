class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum=[]
        t=0
        for i in nums:
            t+=i
            sum.append(t)
        return sum

