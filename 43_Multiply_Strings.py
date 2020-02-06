class Solution:
    # 优化版竖式乘法
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'
        if len(num2) > len(num1):
            num1, num2 = num2, num1
        results = [0 for i in range(len(num1)+len(num2))]
        for i in range(len(num1)-1, -1, -1):
            for j in range(len(num2)-1, -1, -1):
                p = int(num1[i]) * int(num2[j]) + results[i+j+1]
                results[i+j+1] = p % 10
                results[i+j] += p // 10
        product = ""
        for i in range(len(results)):
            if i == 0 and results[i] == 0:
                continue
            product += str(results[i])
        return product
