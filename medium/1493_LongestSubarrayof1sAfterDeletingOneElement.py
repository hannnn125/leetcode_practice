class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        start =0 
        maxLength=0
        delete=False
        if 0 not in nums:
            return len(nums)-1
        for end in range(len(nums)): 
            if nums[end]==0:
                if delete==True:
                    while delete==True:
                        if nums[start]==0:
                            delete=False
                        start+=1
                delete=True
            maxLength=max(maxLength,end-start)
        return maxLength

'''
문제는 값 1개를 지웠을때(필수 1개) 가장 긴 1의 배열을 찾는 것이므로 
모든 값이 1이면 가장 긴 배열은 len(nums)-1 로 해당 경우 제외하고 시작
delete=False로 초기화 
다이나믹 슬라이딩 윈도우 방식 -> 매 iter마다 maxLength Tracking
일단 0을 만날때까지 end 포인터를 늘림 (for loop로)
nums[end]==0이면 우선 delete 확인
    - delete==True이면 바로 이전 0 위치까지 start 포인터를 늘림
    - delete==False이면 delete=True로 변경하고 넘어감

1004번 문제 참고
'''

nums = [1,1,0,1]
print(Solution().longestSubarray(nums))
