class Solution:
    def simplifyPath(self, path: str) -> str:
        path_hierarchy = []
        folder_name = ''

        for ch in path:
            if ch == '/':
                if folder_name == '.':
                    folder_name = ''
                elif folder_name == '..':
                    path_hierarchy = path_hierarchy[:-1]
                    folder_name = ''
                else:
                    if folder_name != '':
                        path_hierarchy.append(folder_name)
                    folder_name = ''
            else:
                folder_name += ch
        if folder_name != '':
            if folder_name == '..':
                path_hierarchy = path_hierarchy[:-1]
            elif folder_name == '.':
                pass
            else:
                path_hierarchy.append(folder_name)

        result = ''
        for i in range(len(path_hierarchy)):
            if path_hierarchy[i] == '':
                continue
            else:
                result += '/' + path_hierarchy[i]
        if result == '':
            result = '/'
        return result
