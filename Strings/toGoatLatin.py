class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        a = 0
        ans = []
        vowels = set("aeiouAEIOU")

        words = sentence.split()

        for word in words:
            a += 1
            if word[0] in vowels:
                transformed_word = word + "ma" + "a" * a
            else:
                transformed_word = word[1:] + word[0] + "ma" + "a" * a

            ans.append(transformed_word)

        return " ".join(ans)
