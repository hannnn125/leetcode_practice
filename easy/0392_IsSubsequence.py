class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s)>len(t):
            return False
        i=0
        j=0 
        while i<len(s) and j<len(t):
            if s[i]==t[j]:
                i+=1
            j+=1
        if i < len(s): #j는 len(t)를 넘겼는데 다 못찾음=없음
            return False
        else: 
            return True
             

'''
1차 시도: 실패 
s안에 없는 ch를 다 지우고 s = t면 true 아니면 false 
중복...단어는 안지워짐 O(M+N)복잡도 
2차 시도: 
힌트 :Verify subsequence by matching characters in order using a linear scan without altering relative positions.
Use two pointers to traverse both strings once, avoiding list reconstruction and membership checks.

s, t에 대한 포인터를 각각 (i,j = 0 초기화) 두고, s[i] == t[j] 인 경우 s안 다음 값을 t에서 찾음
s[i]를 다 돌고 i가 s 인덱스를 넘기면 t에서 s값 다 찾았으니 True 넘김 아니면 False 
j 인덱스는 계속 넘겨야함
baab -> 중복이더라도 a 찾은 후에 다음s로 넘어가므로 상관 x  

'''
        

s = "acd"
t = "ahbgdc"
print(Solution().isSubsequence(s, t))