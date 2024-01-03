class Solution:
    def minProcessingTime(self, processorTime: List[int], tasks: List[int]) -> int:
        processorTime.sort()
        tasks.sort(reverse = True)

        res = float("-inf")

        for i in range(0 , len(tasks) , 4):
            res = max(res , processorTime[i//4] + tasks[i])

        return res

