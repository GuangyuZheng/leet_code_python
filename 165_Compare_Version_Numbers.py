class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1_list = version1.split('.')
        v2_list = version2.split('.')

        flag = 1
        if len(v1_list) < len(v2_list):
            v1_list, v2_list = v2_list, v1_list
            flag = -1

        for i in range(len(v2_list)):
            if int(v1_list[i]) > int(v2_list[i]):
                return flag * 1
            if int(v1_list[i]) < int(v2_list[i]):
                return flag * -1

        for k in range(len(v2_list), len(v1_list)):
            if int(v1_list[k]) > 0:
                return flag * 1

        return 0
