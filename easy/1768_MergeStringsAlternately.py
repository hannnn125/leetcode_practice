class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
    # i - word1,2중 가장 긴 길이까지 반복하며 각 문자열의 문자를 차례대로 추가
        ls=[]
        max_length=max(len(word1), len(word2))
        for i in range(max_length):
            if i < len(word1):
                ls.append(word1[i])
            if i < len(word2):
                ls.append(word2[i])
        return ''.join(ls)


word1 = "abc"
word2 = "pqrs"

print(Solution().mergeAlternately(word1, word2))