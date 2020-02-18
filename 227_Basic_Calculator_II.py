class Solution:
    def calculate(self, s: str) -> int:
        num = 0
        stack = list()
        op = '+'
        for i, c in enumerate(s):
            if c.isnumeric():
                num = num*10+int(c)
            if c in '+-*/' or i == len(s)-1:
                if op == '+':
                    stack.append(num)
                if op == '-':
                    stack.append(-num)
                if op == '*':
                    stack.append(stack.pop()*num)
                if op == '/':
                    stack.append(int(stack.pop()/num))
                op = c
                num = 0
        return sum(stack)
