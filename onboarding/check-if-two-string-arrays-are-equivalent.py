class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word_one = "".join(word1)
        word_two = "".join(word2)

        return word_one == word_two
        