class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        ## start/end pointer 설정, 반대편으로 이동하면서 vowel 만나면 교환 
        vowels = "aeiouAEIOU"
        ls = list(s)
        start = 0 
        end = len(ls)-1

        while start < end:
            # vowel 만날때까지 start 이동 
            while start < end and vowels.find(ls[start])==-1: 
                start+=1
            # vowel 만날때까지 end 이동
            while start < end and vowels.find(ls[end])==-1: 
                end-=1
            ls[start], ls[end] = ls[end], ls[start]
            start+=1
            end-=1
        return "".join(ls)

s = "leetcode"
print(Solution().reverseVowels(s))