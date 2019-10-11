class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if len(a) < len(b):
            tmp = a
            a = b
            b = tmp
        min_len = len(b)
        max_len = len(a)
        ra = [a[i] for i in range(len(a) - 1, -1, -1)]
        rb = [b[i] for i in range(len(b) - 1, -1, -1)]
        rr = ""
        d = 0
        for i in range(min_len):
            num = d + int(ra[i]) + int(rb[i])
            d = num // 2
            num = num % 2
            rr += str(num)
        for i in range(min_len, max_len):
            num = d + int(ra[i])
            d = num // 2
            num = num % 2
            rr += str(num)
        if d != 0:
            rr += str(d)
        result = ''.join([rr[i] for i in range(len(rr) - 1, -1, -1)])
        return result
