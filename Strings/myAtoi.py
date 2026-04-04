class Solution:
    def myAtoi(self, s: str) -> int:
        num = ""
        sign = "*"

        for ch in s:
            if num == "" and ch in ["+", "-"] and sign == "*":
                sign = ch
            elif (num != "" or ch != " " or sign != "*") and not ch.isdigit():
                break
            elif ch != " ":
                num += ch

        if num == "":
            return 0

        num = int(num) if sign in ["*", "+"] else int(num) * -1

        if num < -1 * (2**31):
            num = -1 * (2**31)

        if num > ((2**31) - 1):
            num = (2**31) - 1

        return num

    def myAtoi2(self, s: str) -> int:
        i = 0
        n = len(s)

        while i < n and s[i] == " ":
            i += 1

        sign = 1
        if i < n and (s[i] == "+" or s[i] == "-"):
            if s[i] == "-":
                sign = -1
            i += 1

        num = 0
        while i < n and s[i].isdigit():
            digit = int(s[i])

            if num > (2**31 - 1 - digit) // 10:
                return 2**31 - 1 if sign == 1 else -(2**31)

            num = num * 10 + digit
            i += 1

        return sign * num
