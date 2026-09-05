func firstStableIndex(nums []int, k int) int {
    n := len(nums)
    prefix_min := make([]int, n, n)
    prefix_min[n - 1] = nums[n - 1]
    max := nums[0]

    for i:= n-2; i >= 0; i--{
        if nums[i] < prefix_min[i+1]{
            prefix_min[i] = nums[i]
        } else {
            prefix_min[i] = prefix_min[i + 1]
        }
    }
    
    for i, v := range nums{
        if v > max{
            max = v
        }
        if (max - prefix_min[i]) <= k{
            return i
        }
    }
    return -1
}