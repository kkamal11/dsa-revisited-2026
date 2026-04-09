from typing import List
import heapq
from collections import Counter

class KFrequentElemnts:
    def __init__(self, arr: List[int], k:int):
        self.arr = arr
        self.k = k

    def get_k_freq_elem(self):
        freq = {}
        for num in self.arr:
            freq[num] = freq.get(num, 0) + 1
        
        nums = self.arr.copy()

        nums.sort(key=lambda x: (freq[x], x), reverse=True)

        ans = []

        i = 0
        while len(ans) < self.k:
            if not ans:
                ans.append(nums[i])
            elif ans[-1] != nums[i]:
                ans.append(nums[i])
            i += 1

        return ans
    
    def get_k_freq_elem_optimized(self):
        freq = Counter(self.arr)
        heap = []

        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > self.k:
                heapq.heappop(heap)

        return [num for _, num in heap]
    

nums = [3,2,3,1,2,4,5,5,6,7,7,8,2,3,1,1,1,10,11,5,6,2,4,7,8,5,6]
k = 10
frequent = KFrequentElemnts(nums, k)
print(frequent.get_k_freq_elem())