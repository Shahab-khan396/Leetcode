# boyermoore voting algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # count=0
        # candidate=None
        # for num in nums:
        #     if count==0:
        #         candidate=num
        #         count=1
        #     elif num==candidate:
        #         count +=1
        #     else:
        #         count-=1

        # return candidate

# collections approach
# from collections import Counter
        # counter = Counter(nums)
        # # most_common(1) returns the element with the highest frequency
        # return counter.most_common(1)[0][0]   

# BRute force approach
        for num in set(nums):
            if nums.count(num) > len(nums) // 2:
                return num   

        