class Solution:
    def isPalindrome(self, x) :
        if (x >= 0) :
            x=str(x)
            num2 = x[::-1]
            if (x == num2) :
                return 1
            else :
                return 0

        else :
            return 0

a=Solution()

print(a.isPalindrome(0))