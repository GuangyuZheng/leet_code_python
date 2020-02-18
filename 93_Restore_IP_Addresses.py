from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        results = []
        if s == "":
            return []

        def helper(rest_str, num, curr_str):
            if len(rest_str) > (4 - num) * 3:
                return
            if rest_str[0] != '0':
                if 0 < int(rest_str) <= 255 and num == 3:
                    curr_str = curr_str + rest_str
                    results.append(curr_str)
                    return
            else:
                if int(rest_str) == 0 and len(rest_str) == 1 and num == 3:
                    curr_str = curr_str + rest_str
                    results.append(curr_str)
                    return
            for i in range(1, min(4, len(rest_str))):
                digits = rest_str[:i]
                if digits[0] != '0':
                    if 0 < int(digits) <= 255:
                        helper(rest_str[i:], num + 1, curr_str + digits + '.')
                else:
                    if int(digits) == 0 and len(digits) == 1:
                        helper(rest_str[i:], num + 1, curr_str + digits + '.')

        helper(s, 0, '')

        return results
