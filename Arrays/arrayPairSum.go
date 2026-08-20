func arrayPairSum(nums []int) int {
    slices.SortFunc(nums, func(a, b int) int {
        return a - b
    })
    sum := 0
    n := len(nums)

    for i:=n-1; i > 0; i = i - 2{
        a, b := nums[i], nums[i - 1]
        sum += min(a, b)
    }
    return sum
}

func arrayPairSum(nums []int) int {
    slices.Sort(nums)

    sum := 0
    for i := 0; i < len(nums); i += 2 {
        sum += nums[i]
    }

    return sum
}