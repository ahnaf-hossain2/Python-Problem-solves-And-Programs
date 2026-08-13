"""
You are given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

"""
# Not completed yet. There are errors. Will fix it later tomorrow. By writing down the problem in notebook.
nums = [2,7,11,15]
target = 9

for current in nums:
    new_current = abs(current - target)
    if new_current in nums:
        if (current + new_current) == target:
            output = [nums.index(current), nums.index(new_current)]
            print(output)
            break
