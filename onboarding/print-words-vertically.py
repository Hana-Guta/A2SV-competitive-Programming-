class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split(" ")
        height = max(len(word) for word in words)
        result = []

        for i in range(height):
            column = ""
            for j in range(len(words)):
                if i < len(words[j]):
                    column += words[j][i]
                else:
                    column += " "
            result.append(column.rstrip(" "))
                
        return result
