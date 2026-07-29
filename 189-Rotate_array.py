class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        # Right rotation: move last k elements to the front
        nums[:] = nums[-k:] + nums[:-k]   