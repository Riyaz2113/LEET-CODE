class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        N = [intervals[0]]
        for i in intervals[1:]:
            last = N[-1]
            if i[0] <= last[1]:
                last[1] = max(last[1], i[1])
            else:
                N.append(i)
        return N