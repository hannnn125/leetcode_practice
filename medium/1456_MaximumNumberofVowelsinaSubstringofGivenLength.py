class Solution(object):
    def maxVowels(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        vowels={'a','e','i','o','u'}
        currentCount = len([s[x] for x in range(k) if s[x] in vowels])
        maxCount = currentCount
        for i in range(k, len(s)):
            if s[i-k] in vowels:
                currentCount-=1
            if s[i] in vowels:
                currentCount+=1
            maxCount = max(maxCount, currentCount)
        return maxCount


s = "abciiidef"
k = 3
print(Solution().maxVowels(s, k))

"""
처음에 문제를 잘못이해함 
k 길이의 슬라이딩 윈도우 안에 연속상관없이 최대 vowel개수를 찾아야함 
처음 슬라이드[:k]안의 vowel 개수를 찾고 
i를 k부터 len(s)-1까지 증가시키면서 슬라이드 앞뒤로 vowel이면 뺴고 더하는 방식으로 currentCount를 업데이트 후 maxCount를 업데이트 
마지막에 maxCount를 반환
"""