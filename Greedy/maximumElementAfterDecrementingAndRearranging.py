from typing import List

"""
Given an array of integers arr, you are allowed to choose a set of 
integers and decrement each of them by 1. You can perform this 
operation any number of times (including zero). After performing the 
operations, you can rearrange the elements of the array in any order.
Return the maximum possible value of the maximum element in arr after 
performing the operations and rearranging.

Example 1:
Input: arr = [2,2,1,2,1]
Output: 2

Approach:
1. Sort the array in ascending order.
2. Set the first element to 1, as the minimum possible value for 
the maximum element
3. Iterate through the array starting from the second element, and 
for each element, set it to the minimum of its current value and one more than the previous element.


How to think about it:
Step 1: Read the operations carefully

You are allowed to:

Rearrange the array.
Decrease any element.

Ask yourself:

Since I can rearrange however I want, does the original order matter?

No.

Whenever a problem says "you may rearrange in any order", it is a strong hint that sorting might simplify the problem.

Step 2: Understand the constraints

The final array must satisfy

arr[0] = 1
|arr[i] - arr[i-1]| <= 1

Since all numbers are positive,

arr[i] >= 1

The condition

|arr[i]-arr[i-1]| <= 1

means consecutive numbers cannot jump too much.

Step 3: What are we maximizing?

We want

maximum last element

To make the last element as large as possible, every previous element should also be as large as possible.

Think of building the array from left to right.

Suppose we already fixed

1

What's the largest second element?

2

because

|2-1| = 1

Largest third?

3

Largest fourth?

4

Ideally we'd like

1 2 3 4 5 ...

But we're limited by the numbers we already have.

Step 4: Why sort?

Consider

[100,1,1000]

Without sorting, suppose we keep the order.

100 1 1000

Can you build a valid sequence?

Not easily.

Instead sort

1 100 1000

Now process from smallest to largest.

You immediately know

first = 1

Next number is 100.

Can it stay 100?

No.

Largest allowed is

2

So make it

2

Next

1000

Largest allowed is

3

Done.

Sorting makes the greedy decision obvious.
"""


class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for idx in range(1, len(arr)):
            arr[idx] = min(arr[idx], arr[idx - 1] + 1)
        return arr.pop()


"""
A pattern to remember
Whenever you see a problem with:
You may rearrange the array
You may decrease elements (or otherwise only make them smaller)
A condition involving adjacent values or maintaining an order

a good instinct is:
Sort the array to establish a natural processing order.
Build the answer greedily from left to right, making each element as large as possible while satisfying the constraints.

This pattern appears in many array greedy problems: sorting lets you make locally optimal choices that don't prevent an optimal global solution.

Developing this instinct comes from repeatedly asking:

"Does the original order matter?" If not, sorting is often worth considering.
"Can I build the answer incrementally?" If yes, a greedy approach may be possible.
"At each step, what's the largest valid choice?" That often leads directly to the update rule, like min(curr, previous + 1) here.
"""
