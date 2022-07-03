import bisect


class Solution:

    def platesBetweenCandles(self, s, queries):
        A = [i for i, c in enumerate(s) if c == '|']
        print(f'A={A}')
        res = []
        for a, b in queries:
            # Locate the insertion point for x in a to maintain sorted order.
            # If x is already present in a, the insertion point will
            # be before (to the left of) any existing entries.
            i = bisect.bisect_left(A, a)

            # Similar to bisect_left(), but returns an insertion point which
            # comes after (to the right of) any existing entries of x in a.
            j = bisect.bisect(A, b) - 1

            res.append((A[j] - A[i]) - (j - i) if i < j else 0)
            print(f'i={i} j={j} res={res}')
        return res


s1 = '**|**|***|'
s2 = "***|**|*****|**||**|*"
queries1 = [[2, 5], [5, 9]]
queries2 = [[1, 17], [4, 5], [14, 17], [5, 11], [15, 16]]
pbc = Solution()

print(pbc.platesBetweenCandles(s2, queries2))
