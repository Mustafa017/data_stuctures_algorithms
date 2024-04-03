class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        res = []
        savedResults = {}
        for i in range(lo, hi+1):
            power = self.numSteps(i, savedResults)
            res.append((power, i))
        res = sorted(res, key=lambda pair: pair[0])
        # print(savedResults)
        print(res)
        return res[k-1][1]

    def numSteps(self, n, savedResults):
        steps = 0
        # init = n
        while n != 1:
            if n in savedResults:
                print(f'n={n} steps={savedResults[n]} cache={savedResults}')
                return savedResults[n] + steps
            else:
                n = 3*n + 1 if n % 2 else n//2
                steps += 1

                savedResults[init] = steps

        return steps
# [(3, 8), (6, 10), (14, 11), (16, 7), (19, 9)]
# [(4, 16), (6, 10), (7, 20), (9, 12), (9, 13), (12, 17), (14, 11), (17, 14), (17, 15), (20, 18), (20, 19)]
if __name__ == "__main__":
    s = Solution()
    # expected answer 13
    # print(s.getKth(12, 15, 2)) 
    print(s.getKth(7, 11, 4))
    # expected answer 13
    # print(s.getKth(10, 20, 5))
