class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        # trick is to decide when to assign a new room vs using an avaibable room
        # we can use a min heap to keep track of end time of used rooms to determine if a new room is needed for next meeting
        if len(intervals) == 0: return 0
        free_rooms = []
        intervals = sorted(intervals, key = lambda x: x[0]) # sort by start time
        heapq.heappush(free_rooms, intervals[0][1]) # start with the first room
        
        for i in intervals[1:]:
            # if the room on top of the queue ends before the next start
            if free_rooms[0] <= i[0]:
                heapq.heappop(free_rooms)
            heapq.heappush(free_rooms, i[1])
        
        return len(free_rooms)
