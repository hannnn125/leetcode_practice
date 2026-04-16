
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        rom = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500, 'M':1000}
        result = 0 
        for i in range(len(s)):
            if i < len(s)-1 and rom[s[i]]<rom[s[i+1]]:
                result -= rom[s[i]]
            else:
                result += rom[s[i]]

        return result
