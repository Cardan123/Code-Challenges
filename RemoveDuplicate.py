from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
      k = 0

      for i in range(len(nums) - 1):
        if(nums[i] != nums[i+1]):
          nums[k] = nums[i+1]
          k+=1

      return k, nums 

nums = [0,0,1,1,1,2,2,3,3,4,4,5,5,7]
obj = Solution()
ans = obj.removeDuplicates(nums)

print(ans)