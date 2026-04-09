import heapq

class KthElementInArr:
    def __init__(self, arr, k):
        self.arr = arr
        self.k = k
        self.n = len(self.arr)
    
    def kth_largest_element(self):
        heap = []
        for num in self.arr:
            heapq.heappush(heap, num)
            if len(heap) > self.k:
                heapq.heappop(heap)
        return heap

    def kth_smallest_element(self):
        heap = []
        for num in self.arr:
            heapq.heappush(heap, -num)
            if len(heap) > self.k:
                heapq.heappop(heap)
        return [-num for num in heap]

    def __str__(self):
        return str(self.arr)




nums = [-5, 4, 1, 2, -3]
k = 2
kth = KthElementInArr(nums, k) 
print(kth.kth_largest_element())
print(kth.kth_smallest_element())