class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = list(bin(n)[2:])

        for i in range(1, len(bits)):
            if bits[i] == bits[i - 1]:
                return False

        return True