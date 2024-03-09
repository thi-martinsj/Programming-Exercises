class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def invert(array, i, j):
            while i < j:
                array[i], array[j] = array[j], array[i]
                i += 1
                j -= 1
        
        n = len(nums)
        k = k % n
        
        invert(nums, 0, n - 1)
        invert(nums, 0, k - 1)
        invert(nums, k, n - 1)
