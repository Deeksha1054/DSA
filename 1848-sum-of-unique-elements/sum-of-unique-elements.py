class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        dict={}
        uni_sum=0
        for i in range(0, len(nums)):
            if nums[i] in dict:
                dict[nums[i]]+=1
            else:
                dict[nums[i]]=1
        for key, val in dict.items():
            if val == 1:
                uni_sum+= key
        return uni_sum
        