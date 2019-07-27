class Solution:
    def reverse(self, x) :
        if (x==0) :
            return 0
        while ( x%10 == 0) :
            x = x//10

        result = ""
        x=str(x)
        ln=len(x)

        for i in range(0, ln):
            result = str(x[i]) + result
        if (result[ln-1]=="-") :
            result = result[ln-1]+result[0:ln-1]
        if (int(result) < -2**31 or int(result) > (2**31)-1) :
            print(result)
            return 0

        print(result)
a=Solution()
a.reverse(1534236469)