class HeapConverter:
    def __init__(self, arr):
        self.arr = arr
        self.n = len(arr)

    def left_child_idx(self, i):
        return 2*i + 1

    def right_child_idx(self, i):
        return 2*i + 2

    def max_heapify(self, i):
        largest = i
        l = self.left_child_idx(i)
        r = self.right_child_idx(i)

        if l < self.n and self.arr[l] > self.arr[largest]:
            largest = l

        if r < self.n and self.arr[r] > self.arr[largest]:
            largest = r

        if largest != i:
            self.arr[i], self.arr[largest] = self.arr[largest], self.arr[i]
            self.max_heapify(largest)
        
    def min_heapify(self, i):
        smallest = i
        l = self.left_child_idx(i)
        r = self.right_child_idx(i)

        if l < self.n and self.arr[l] < self.arr[smallest]:
            smallest = l

        if r < self.n and self.arr[r] < self.arr[smallest]:
            smallest = r

        if smallest != i:
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.min_heapify(smallest)

    def convert_to_max_heap(self):
        for i in range(self.n//2 - 1, -1, -1):
            self.max_heapify(i)

        return self.arr
    
    def convert_to_min_heap(self):
        for i in range(self.n//2 - 1, -1, -1):
            self.min_heapify(i)

        return self.arr