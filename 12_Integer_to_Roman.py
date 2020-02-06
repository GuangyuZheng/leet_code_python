class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''
        value2symbol = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
        }
        divide = [1000, 100, 10, 1]
        for i in range(len(divide)):
            val = num // divide[i]
            assert val <= 9
            if val == 0:
                continue
            else:
                if val < 4:
                    tmp_result = val * value2symbol[divide[i]]
                elif val == 4:
                    tmp_result = value2symbol[divide[i]] + value2symbol[5*divide[i]]
                elif val == 9:
                    tmp_result = value2symbol[divide[i]] + value2symbol[10*divide[i]]
                else:
                    tmp_result = value2symbol[5*divide[i]] + (val-5) * value2symbol[divide[i]]
                result += tmp_result
            num -= val * divide[i]
        return result
