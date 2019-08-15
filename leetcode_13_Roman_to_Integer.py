class Solution:
    def romanToInt(self, s) :
        nums = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        num = 0
        for i in range(len(s)):
            if i + 1 < len(s) and nums[s[i + 1]] > nums[s[i]]:
                num -= nums[s[i]]
            else:
                num = num + nums[s[i]]
        return num






a=Solution()
print(a.romanToInt("MCMXCIV"))