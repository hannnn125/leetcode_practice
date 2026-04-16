class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ""
        prefix = strs[0] #첫번째 문자 전체를 prefix로 설정
        for s in strs[1:]: 
            while not s.startswith(prefix): #s가 prefix로 시작하지 않으면 
                prefix = prefix[:-1] #prefix 한문자씩 줄이기
                if not prefix: #prefix가 비어있으면 빈문자열 반환
                    return "" #빈문자열 반환
        return prefix #prefix 반환

#가장 긴 prefix를 찾아야하므로 긴->짧 순으로 탐색.
strs = ["flower","flow","flight"]
# strs = ["dog","racecar","car"]
# strs = ["a"]
# strs = ["",""]
# strs = ["",""]
print(Solution().longestCommonPrefix(strs))