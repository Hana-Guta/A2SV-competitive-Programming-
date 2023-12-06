class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count = Counter(nums)
        k = len(nums)// 3
        arr = []
        for num, cnt in count.items():
            if cnt > k:
                arr.append(num)

        return arr
        