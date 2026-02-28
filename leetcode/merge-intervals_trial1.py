class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        n = len(intervals)
        new_intervals = []
        curr = []
        intervals.sort(key=lambda x: x[0])

        for i in range(n):
            if not curr:
                curr = intervals[i]
            elif curr[1] >= intervals[i][1]:
                continue
            elif curr[1] >= intervals[i][0]:
                curr[1] = intervals[i][1]
            else:
                new_intervals.append(curr)
                curr = intervals[i]
        new_intervals.append(curr)
        return new_intervals