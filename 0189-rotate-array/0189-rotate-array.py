class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        self.rev(nums, 0, n -1) 
        self.rev(nums, 0, k -1)
        self.rev(nums, k, n -1)
    
    def rev(self, nums, left, right):
        while left < right:
            nums[left], nums[right] =  nums[right], nums[left]
            left += 1
            right -= 1
