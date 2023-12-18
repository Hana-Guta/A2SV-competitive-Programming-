class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s_list = list(s)
        n = len(s)

        for i in range(0, n, 2 * k):
            start, end = i, min(i + k - 1, n - 1)
            
            while start < end:
                s_list[start], s_list[end] = s_list[end], s_list[start]
                start += 1
                end -= 1

        return ''.join(s_list)