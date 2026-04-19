class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        
    #Greatest common divisor of two strings
    #최대공약수         
        if str1+str2 == str2+str1:
            idx = self.gcd(len(str1), len(str2))
            return str1[:idx]
        else:
            return ""

    def gcd(self, a,b):
        while b: 
            a,b = b, a%b 
        return a 

str1 = "ABCABC"
str2 = "ABC"

print(Solution().gcdOfStrings(str1, str2))