import sys
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.count = 0
        self.dfs(s, [], self.count)
        return self.count

    def dfs(self, s, path, count):
        if len(s) > (4 - len(path)) * 3:
            return
        if not s and len(path) == 4:
            count  = count+1
            return count
        for i in range(min(3, len(s))):
            curr = s[:i+1]
            if (curr[0] == '0' and len(curr) >= 2) or int(curr) > 255:
                continue
            count = self.dfs(s[i+1:], path + [s[:i+1]], count)

if __name__ == '__main__':
    solu = Solution()
    str_ = sys.stdin.readline().strip()
    res = solu.restoreIpAddresses(str_)
    print(res)