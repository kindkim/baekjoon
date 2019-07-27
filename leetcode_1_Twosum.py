class Solution:
    def twoSum(self, nums, target) :
        ln=len(nums)
        for i in range(ln) :
            for j in range(1, ln-1) :
                if ( nums[i]+nums[j] == target) :
                    return([i,j])
                    # print([i, j])

a=Solution()
a.twoSum([2, 7, 11, 15], 9)

# https://leetcode.com/problems/two-sum/