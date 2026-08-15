class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        a = 0
        ans = []
        vowels = {"A", "E", "I", "O", "U"}

        words = sentence.split()

        for word in words:
            a += 1
            if word[0].upper() in vowels:
                ans.append(word + "ma" + "a" * a)
            else:
                ans.append(word[1:] + word[0] + "ma" + "a" * a)

        return " ".join(ans)
