class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        widest = 0
        points.sort(key=lambda x: x[0])

        for i in range(1, len(points)):
            prev_x, prev_y = points[i-1]
            curr_x, curr_y = points[i]
            diff = curr_x - prev_x

            if diff > widest:
                widest = diff
        
        return widest