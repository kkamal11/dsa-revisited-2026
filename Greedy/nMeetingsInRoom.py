class Solution:
    """
    Schedule the meeting that ends earliest
    """
    def num_meetings(self,start, end):
        count = 0
        last_meet_end = None

        meetings = [(start[i], end[i], i+1) for i in range(len(start))]
        meetings.sort(key=lambda x: x[1])

        n = len(meetings)

        result = []

        for i in range(n):
            st = meetings[i][0]
            en = meetings[i][1]

            if last_meet_end is None or last_meet_end < st:
                count += 1
                result.append(meetings[i][-1])
                last_meet_end = en
        
        return count, result


sol = Solution()
start = [1,3,0,5,8,5]
end = [2,4,5,7,9,9]

print(sol.num_meetings(start, end))

start = [9,5]
end = [9,8]
print(sol.num_meetings(start, end))