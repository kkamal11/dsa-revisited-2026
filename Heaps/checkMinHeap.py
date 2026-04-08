class MinHeap:
    def __init__(self, arr):
        self.arr = arr
    
    def parent_idx(self, ind):
        return (ind - 1) // 2
    
    def left_child_idx(self, ind):
        return 2*ind + 1
    
    def right_child_idx(self, ind):
        return 2*ind + 2
    
    def check_valid_min_heap(self):
        i = 0
        n = len(self.arr)
        while i < n//2:
            node_value = self.arr[i]

            li = self.left_child_idx(i)
            ri = self.right_child_idx(i)

            if ri < n and node_value > self.arr[ri]:
                return False

            if li < n and node_value > self.arr[li]:
                return False
             
            i += 1

        return True
    
    def check_valid_max_heap(self):
        i = 0
        n = len(self.arr)
        for i in range(n//2):
            node_value = self.arr[i]

            li = self.left_child_idx(i)
            ri = self.right_child_idx(i)

            if ri < n and node_value < self.arr[ri]:
                return False

            if li < n and node_value < self.arr[li]:
                return False
             
        return True
    
    def __str__(self):
        return str(self.arr)


def main():
    L = [10, 20, 30, 25, 15]
    min_heap = MinHeap(L)
    print(min_heap.check_valid_min_heap())

    L2 = [10, 20, 30, 21, 23]
    min_heap = MinHeap(L2)
    print(min_heap.check_valid_min_heap())


if __name__ == "__main__":
    main()
    
