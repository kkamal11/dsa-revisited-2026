class BinaryUtil:
    def convert_decimal_to_binary(self, n: int) -> str:
        """
        Time complexity - O(log n)
        Space Complexity - O(log n) because numner of bits in n = log2 n
        """
        binary = []

        while n > 0:
            rem = n % 2
            binary.append(rem)
            n = n // 2

        return "".join(
            (str(x) for x in reversed(binary))
        )  # It will have complexity O(log n) as number of elements = log n

    def convert_binary_to_decimal(self, s: str) -> int:
        ans = 0
        p2 = 1

        for i, ch in enumerate(reversed(s)):
            # ans += int(ch) * (2**i)
            ans += int(ch) * p2
            p2 = 2 * p2

        return ans

    def get_ones_complement(self, n):
        binary = self.convert_decimal_to_binary(n)

        ans = ""

        for x in binary:
            if x == "1":
                ans += "0"
            else:
                ans += "1"

        return ans

    def get_twos_complement(self, n):
        ones = self.get_ones_complement(n)

        res = list(ones)
        carry = 1

        for i in range(len(res) - 1, -1, -1):
            if res[i] == "1" and carry == 1:
                res[i] = "0"
            else:
                res[i] = "1"
                carry = 0
                break

        if carry == 1:
            res.insert(0, "1")

        return "".join(res)


n = 13
s = "1101"
binary = BinaryUtil()
print(binary.convert_decimal_to_binary(n))
print(binary.convert_binary_to_decimal(s))
print(binary.get_ones_complement(n))
print(binary.get_twos_complement(n))
