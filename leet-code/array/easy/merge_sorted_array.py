class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        ind_num1 = 0
        ind_num2 = 0

        temp_array = nums1[:m]
    
        for i in range(m + n):
            if ind_num1 < m and (n == 0 or ind_num2 > (n - 1) or temp_array[ind_num1] <= nums2[ind_num2]):
                nums1[i] = temp_array[ind_num1]
                ind_num1 += 1
            else:
                nums1[i] = nums2[ind_num2]
                ind_num2 += 1
        