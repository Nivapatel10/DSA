class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        ans = 0
        for (x1,y1),(x2,y2) in zip(points,points[1:]):
            ans+=max(abs(x2-x1),abs(y2-y1))
        return ans 
        