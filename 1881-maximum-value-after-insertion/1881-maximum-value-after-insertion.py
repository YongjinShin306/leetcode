class Solution(object):
    def maxValue(self, n, x):
        """
        :type n: str
        :type x: int
        :rtype: str
        """
        l = len(n)
        if n[0] == "-":
            if int(max(list(n))) <= x:
                pos = l
            else:
                i = 1
                while int(n[i]) <= x:
                    i += 1
                pos = i
        else:
            if int(min(list(n))) >= x:  # 가장 마지막 위치에 부여
                pos = l
            else:  # 앞에서부터 x보다 작은 최초의 위치에 앞에 부여
                i = 0
                while int(n[i]) >= x:
                    i += 1
                pos = i

        ans = n[0:pos] + str(x) + n[pos:l]
        return ans