class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        min_times = len(nums) // 2

        nums_set = set(nums)

        for num in nums_set:
            if nums.count(num) > min_times:
                return num