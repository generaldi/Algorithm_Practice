class Solution:
    def binary_search(self,nums:list[int],target:int):
        left,right=0,len(nums)
        while left<right:
            middle=(left+right)//2
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right=middle
            else:
                left=middle+1
        return -1
# Testing the code
nums=[-1,0]
target_exist=0
target_not_exist=2
print('Searching ',target_exist,' in ',nums,',returning :',Solution().binary_search(nums,target_exist))
print('Searching ',target_not_exist,' in ',nums,',returning :',Solution().binary_search(nums,target_not_exist))
            