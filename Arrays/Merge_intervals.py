class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        a = intervals
        a.sort()
        result = []
        
        start = a[0][0]
        end = a[0][1]
        
        for item in a[1:]:
            if item[0] <= end:
                end = max(end,item[1])
            else:
                result.append([start, end])
                start = item[0]
                end = item[1]
        result.append([start, end])
                
        return result
    
#     Input - [[1,3],[2,6],[8,10],[15,18]]
#     Out - [[1,6],[8,10],[15,18]]
