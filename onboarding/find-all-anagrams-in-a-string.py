class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_freq = Counter(p)
        window_freq = Counter(s[:len(p)])
        k = len(p)
        res = []

        if window_freq == p_freq:
            res.append(0)

        for i in range(k, len(s)):
            window_freq[s[i - k]] -= 1

            if window_freq[s[i - k]] == 0:
                del window_freq[s[i - k]]

            window_freq[s[i]] += 1

            if window_freq == p_freq:
                res.append(i - k + 1)

        return res






            

            