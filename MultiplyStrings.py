class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                product = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j, i + j + 1
                total = product + result[pos2]

                result[pos1] += total // 10
                result[pos2] = total % 10

        index = 0
        while index < len(result) and result[index] == 0:
            index += 1

        return ''.join(str(x) for x in result[index:])

    
  
