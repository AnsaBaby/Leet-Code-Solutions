class Solution:
    def twoSum(self, nums, target):
        output = [0, 1]
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    output[0] = i
                    output[1] = j
                    break
        return output
    
# Time Complexity: O(n^2)
# Space Complexity: O(1)