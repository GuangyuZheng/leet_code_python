class Solution:
    def romanToInt(self, s: str) -> int:
        symbol2value = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
            '': 999999,
        }
        ERROR = -1
        result = 0
        pre_ch = ""
        for ch in s:
            pre_value = symbol2value[pre_ch]
            value = symbol2value[ch]
            if pre_value < value:
                result -= pre_value
                if pre_ch == 'I':
                    if ch == 'V':
                        result += 4
                    elif ch == 'X':
                        result += 9
                    else:
                        return ERROR
                elif pre_ch == 'X':
                    if ch == 'L':
                        result += 40
                    elif ch == 'C':
                        result += 90
                    else:
                        return ERROR
                elif pre_ch == 'C':
                    if ch == 'D':
                        result += 400
                    elif ch == 'M':
                        result += 900
                    else:
                        return ERROR
                else:
                    return ERROR
            else:
                result += value
            pre_ch = ch
        return result