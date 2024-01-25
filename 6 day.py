class Solution(object):
    def majorityElement(self, nums):
        non_duplicate = list(set(nums))
        for i in non_duplicate:
            if nums.count(i) > (len(nums)/2):
                return i
