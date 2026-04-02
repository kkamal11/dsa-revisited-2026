class SolutionNaive:
    def merge(self, nums1, nums2):
        result = []
        i = 0
        j = 0
        m = len(nums1)
        n = len(nums2)
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                result.append(nums1[i])
                i += 1
            else:
                result.append(nums2[j])
                j += 1
        while i < m:
            result.append(nums1[i])
            i += 1
        while j < n:
            result.append(nums2[j])
            j += 1
        return result

    def findMedianSortedArrays(self, nums1, nums2):
        result = self.merge(nums1, nums2)
        num_elem = len(result)

        if num_elem % 2 != 0:
            median = result[num_elem // 2]
        else:
            a = result[num_elem // 2]
            b = result[(num_elem // 2) - 1]
            median = (a + b) / 2
        return median


# There will n/2 elements on left of median and n/2 elements on right of median
# We cann use this
class SolutionBinarySearch:
    def findMedianSortedArrays(nums1, nums2):
        # always binary search on smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n1, n2 = len(nums1), len(nums2)
        low, high = 0, n1

        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1

            l1 = float("-inf") if cut1 == 0 else nums1[cut1 - 1]
            l2 = float("-inf") if cut2 == 0 else nums2[cut2 - 1]
            r1 = float("inf") if cut1 == n1 else nums1[cut1]
            r2 = float("inf") if cut2 == n2 else nums2[cut2]

            if l1 <= r2 and l2 <= r1:
                # correct partition
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2
                else:
                    return max(l1, l2)

            elif l1 > r2:
                high = cut1 - 1
            else:
                low = cut1 + 1
