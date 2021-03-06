'''
完全AC
'''
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        stack = list()
        path = [p for p in path.split('/') if p]
        for f in path:
            if f == '.':
                continue
            elif f == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(f)

        return '/' + '/'.join(stack)
if __name__ == '__main__':
    a = '/a/././b//../../c/'
    print(Solution().Path(a))