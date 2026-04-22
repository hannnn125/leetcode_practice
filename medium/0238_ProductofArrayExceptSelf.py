class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [0]*n
        left = 1
        right = 1

        for i in range(n):
            result[i] = left
            left *= nums[i]
        for i in range(n-1, -1, -1):
            result[i] *= right 
            right *= nums[i]
        return result

nums = [-1,1,0,-3,3]
print(Solution().productExceptSelf(nums))

## note : 
'''
1차시도: (시간초과)
곱해야하는 값들을 i기준 왼쪽 슬라이싱 + 오른쪽 슬라이싱으로 리스트 만든 후 곱하는 방식을 생각
-> 이때 빈리스트에서 인덱스로 값 넣으려고함 (오류) -> .append로 변경 
but, 문제 의도는 division 없이 O(n)으로 풀어야함 해당방식 = O(n^2) : 리스트 만드는 과정 n X 내부에서 곱하는 과정 n-1

2차시도: (시간초과)
여전히 O(n^2) 시간복잡도  

3차 시도: 
일단 len(nums)길이의 result 리스트를 만듬
i 왼쪽에 있는 값을 먼저 리스트에 넣어줌, 오른쪽에 있는 값을 거기에 곱해줌
'''