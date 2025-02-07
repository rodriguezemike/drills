#https://leetcode.com/problems/two-sum/submissions/1534122856/

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in lookup:
                return [lookup[complement], i]
            lookup[nums[i]] = i
