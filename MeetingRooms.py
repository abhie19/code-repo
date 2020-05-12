class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        # sort and compare subsequent meetings for overlap
        if len(intervals) <= 1: return True
        # sort
        intervals = sorted(intervals)
        # compare each subsequent for overlap
        for i in range(len(intervals)-1):
            if intervals[i][0] < intervals[i+1][1] and intervals[i+1][0] < intervals[i][1]:
                return False
        return True
