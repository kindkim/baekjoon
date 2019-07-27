class Solution:
    def twoSum(self, nums, target) :
        ln=len(nums)
        print(ln)
        for i in range(ln) :
            for j in range(i+1, ln) :
                if ( nums[i]+nums[j] == target) :
                    # print([i, j])
                    return([i,j])


# a=Solution()
# a.twoSum([3,3], 6)
# a.twoSum([2, 7, 11, 15], 9)

# https://leetcode.com/problems/two-sum/