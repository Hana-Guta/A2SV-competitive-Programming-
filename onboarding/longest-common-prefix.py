class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        first = strs[0]

        def same(prev, curr):
            longest_pre = []
            for i in range(min(len(prev), len(curr))):
                if prev[i] != curr[i]:
                    break
                else:
                    longest_pre.append(prev[i])
            return "".join(longest_pre)

        for i in range(1, len(strs)):
            first = same(first, strs[i])

        return first
