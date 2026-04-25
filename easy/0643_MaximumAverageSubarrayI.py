class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        i = 0
        previous = sum(nums[:k])
        avg = previous/float(k)
        max_avg = avg
        i+=1

        while i <= len(nums)-k:
            current_sum = previous-(nums[i-1])+(nums[i+k-1])
            avg = current_sum/float(k)
            previous = current_sum
            if avg > max_avg:
                max_avg = avg
                i+=1
            else:
                i+=1
        return max_avg
            
'''
k가 엄청 큰 상황 고려 sum()으로 매번 값 찾는것보다 
슬라이딩하면서 앞뒤값만 각각 빼고 더하는식으로 

이때 그냥 나눠버리면 정수/정수 라 정수/실수 로 바꿔줌
'''
        