class Solution:
    def minPlatformsNeeded(self, arr, dep):
        schedule = list(zip(arr, dep))

        schedule.sort(key=lambda x: x[1])
        time = []
        n = len(schedule)
        platform_count = 0

        print(schedule)
        s = schedule[0][0]
        e = schedule[0][0]

        for i in range(1,n):
            start_time = schedule[i][0]
            end_time = schedule[i][1]



            

        return platform_count


sol = Solution()
arr = [900, 945, 955, 1100, 1500, 1800]
dep = [920, 1200, 1130, 1150, 1900, 2000]
print(sol.minPlatformsNeeded(arr, dep))