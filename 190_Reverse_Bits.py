class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        binary = str(bin(n))[2:].zfill(32)
        reverse = binary[::-1]
        reverse = '0b' + reverse
        result = int(reverse, 2)
        return result

    # bit operation version
    def reverseBitsV2(self, n):
        result = 0
        mask = 1
        for i in range(32):
            if n & mask != 0:
                result = result | (1 << (31 - i))
            mask = mask << 1
        return result
