class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        pointer = 0

        for idx, char in enumerate(s):
            if pointer < len(spaces) and spaces[pointer] == idx:
                res.append(" ")
                pointer += 1

            res.append(char)

        return "".join(res)