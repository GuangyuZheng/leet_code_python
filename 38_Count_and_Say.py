class Solution:
    def say(self, s: str) -> str:
        tmp_token = s[0]
        count = 1
        result = ""
        for i in range(1, len(s)):
            if s[i] != tmp_token:
                result += str(count) + tmp_token
                tmp_token = s[i]
                count = 1
            else:
                count += 1
        result += str(count) + tmp_token
        return result

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            return self.say(self.countAndSay(n - 1))