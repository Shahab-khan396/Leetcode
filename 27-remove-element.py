class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # for i in range(len(nums)):
        k = 0
        i = 0  # 1. Initialize i
        
        while i < len(nums): # 2. Use < instead of <= to avoid IndexError
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
            i += 1  # 3. Always increment i (moved outside the if block)
            
        return k
