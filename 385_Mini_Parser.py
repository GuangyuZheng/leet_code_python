# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """


class NestedInteger:
    def __init__(self, value=None):
        """
       If value is not specified, initializes an empty list.
       Otherwise initializes a single integer equal to value.
       """

    def isInteger(self):
        """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

    def add(self, elem):
        """
       Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
       :rtype void
       """

    def setInteger(self, value):
        """
       Set this NestedInteger to hold a single integer equal to value.
       :rtype void
       """

    def getInteger(self):
        """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

    def getList(self):
        """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


# Recursion Version
class Solution:
    def deserialize(self, s: str) -> NestedInteger:

        def helper(s, start, end):
            if s[start:end + 1] == "":
                return NestedInteger(value=None)
            if s[start] != "[":
                return NestedInteger(value=int(s[start:end + 1]))
            else:
                elem = None
                nested = NestedInteger(value=None)
                i = start + 1
                while i <= end - 1:
                    if s[i] not in ',[]':
                        new_end = i + 1
                        while new_end <= end - 1 and s[new_end] != ",":
                            new_end += 1
                        elem = helper(s, i, new_end - 1)
                        i = new_end
                    else:
                        if s[i] == ",":
                            nested.add(elem)
                            elem = None
                            i += 1
                        elif s[i] == "[":
                            new_end = i + 1
                            left_count = 1
                            while left_count != 0:
                                if s[new_end] == '[':
                                    left_count += 1
                                if s[new_end] == ']':
                                    left_count -= 1
                                new_end += 1
                            elem = helper(s, i, new_end - 1)
                            i = new_end
                if elem is not None:
                    nested.add(elem)
                return nested

        return helper(s, 0, len(s) - 1)


# Stack Version
class SolutionV2:
    def deserialize(self, s: str) -> NestedInteger:
        if s[0] != "[":
            return NestedInteger(int(s))
        stack = []
        sign, number, is_num = 1, 0, False
        for ch in s:
            if ch == "-":
                sign = -1
            elif ch.isdigit():
                number = number * 10 + int(ch)
                is_num = True
            elif ch == "[":
                stack.append(NestedInteger())
            elif ch in ",]":
                if is_num:
                    curr = stack.pop()
                    curr.add(NestedInteger(sign * number))
                    stack.append(curr)
                sign, number, is_num = 1, 0, False

                if ch == "]" and len(stack) > 1:
                    curr = stack.pop()
                    stack[-1].add(curr)
        return stack[0]
