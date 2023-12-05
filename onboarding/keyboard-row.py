class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        arr = []

        for word in words:
            if any(letter in "qwertyuiop" for letter in word.lower()) and \
               not any(letter in "asdfghjkl" for letter in word.lower()) and \
               not any(letter in "zxcvbnm" for letter in word.lower()):
                arr.append(word)
            elif any(letter in "asdfghjkl" for letter in word.lower()) and \
                 not any(letter in "qwertyuiop" for letter in word.lower()) and \
                 not any(letter in "zxcvbnm" for letter in word.lower()):
                arr.append(word)
            elif any(letter in "zxcvbnm" for letter in word.lower()) and \
                 not any(letter in "qwertyuiop" for letter in word.lower()) and \
                 not any(letter in "asdfghjkl" for letter in word.lower()):
                arr.append(word)

        return arr
