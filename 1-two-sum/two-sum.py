class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #deeksha
        dict={}
        for i in range(0, len(nums)):
            cur_sum= target - nums[i]
            if cur_sum in dict:
                return [dict[cur_sum], i]
            else:
                dict[nums[i]]=i


           # n=len(nums)
        # for i in range(0, n-1):
        #     for j in range(i+1,n):
        #         if nums[i]+nums[j]==target:
        #             return[i, j]       