class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        while l < r:
            mid = (l + r) // 2
            # check if min is in left or right
            if nums[mid] <= nums[r]: # in left half
                r = mid
            
            else: # min is in right half
                l = mid + 1
        

        return nums[l]