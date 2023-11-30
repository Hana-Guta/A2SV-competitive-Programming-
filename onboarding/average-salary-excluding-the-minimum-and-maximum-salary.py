class Solution:
    def average(self, salary: List[int]) -> float:
        salary.sort()
        left = 0
        right = len(salary) - 1

        Sum = sum(salary) - (salary[left] + salary[right])
        if right - 1 == 0:
            return 0
        average = Sum /(right - 1)

        return average
        