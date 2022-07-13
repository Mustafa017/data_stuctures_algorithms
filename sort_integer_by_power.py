class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        for i in range(lo, hi+1):
            power = self.numSteps(i)
            res.append((power, i))
        res = sorted(res, key=lambda pair: pair[0])
        return res[k-1][1]

    def numSteps(self, n):
        steps = 0
        init = n
        cache = {}
        while n != 1:
            if n in cache:
                steps += cache[n]
            else:
                n = 3*n + 1 if n % 2 else n//2
                steps += 1

        cache[init] = steps

        return steps


if __name__ == "__main__":
    s = Solution()
    # print(s.getKth(12, 15, 2))
    print(s.getKth(7, 11, 4))
