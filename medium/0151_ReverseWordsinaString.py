class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        #공백 만날때까지 word에 글자 더함
        #공백을 만나면 word를 ls에 append 하고 다시 비움 
        word = ""
        ls = []
        for i in range(len(s)):
            if s[i] != " ":
                word+=s[i] 
            else: 
                if word:
                    ls.append(word)
                    word=""
        if word: 
            ls.append(word)
        ls.reverse()
        return " ".join(ls)
    
s = "the sky is blue"
print(Solution().reverseWords(s))