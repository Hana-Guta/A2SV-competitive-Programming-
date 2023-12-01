class Solution:
    def isAlienSorted(self, words, order) -> bool:
        dic = {}
        for i, c in enumerate(order):
            dic[c] = i
        
        prev = []
        for char in words[0]:
            prev.append(dic[char])
        
        for i in range(1, len(words)):
            cur = []
            for ch in words[i]:
                cur.append(dic[ch])
            
            if cur < prev:
                return False
            prev = cur
        
        return True
