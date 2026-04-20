'''
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
'''
## 꽃 심으려는곳 포함 앞뒤로 0이어야 심을 수 있음. -> flowerbed 를 돌면서 인덱스 포함 앞뒤 합이 0인걸 확인하면 됨
##첫번째와 마지막 인덱스 확인 용이하게 하기 위해 패딩 넣어줌 
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        flowerbed = [0]+flowerbed+[0]

        for i in range(1, len(flowerbed)-1): 
            if sum(flowerbed[i-1:i+2])==0: 
                flowerbed[i]=1
                n-=1

        return n<= 0