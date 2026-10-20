func targetIndices(nums []int, target int) []int {
    target_indices := make([]int, 0)

    smallers, equals := 0, 0

    for _, num := range nums{
        if num == target{
            equals += 1
        } else if (num < target){
            smallers += 1
        }
    }
    for i := range equals{
        target_indices = append(target_indices, smallers + i)
    }
    return target_indices
}


// Example usage
nums := []int{1, 2, 5, 2, 3}
target := 2
result := targetIndices(nums, target)
fmt.Println(result) // Output: [1, 2]

nums = []int{1, 2, 5, 2, 3}
target = 3
result = targetIndices(nums, target)
fmt.Println(result) // Output: [3]


nums = []int{1, 2, 5, 2, 3}
target = 5
result = targetIndices(nums, target)
fmt.Println(result) // Output: [4]