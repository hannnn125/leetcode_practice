class Solution(object):
    def longestOnes(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        매 턴마다 max길이를 확인하고 업데이트 해줘야함
        K값을 건드리면안됨 0개수 세는걸로 k얼마나 사용했는지 확인
        nums[end]가 1이면? 변화 x 다음단계로 
        nums[end]가 0이면? 
            -zeroCount<k 라면 zeroCount 증가
            -zeroCount>=k 라면 zeroCount=k 가 될때까지 start 증가 
        """
        start=0 
        zeroCount=0
        max1=0
        
        for end in range(len(nums)):           
            if nums[end]==0:
                zeroCount+=1
            while zeroCount>k:
                if nums[start]==0:
                    zeroCount-=1
                start+=1
            max1=max(max1,end-start+1)
        return max1
                
