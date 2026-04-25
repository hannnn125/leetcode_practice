class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        ## 출발점(0,1)
        current = 0
        highest = 0
        
        for al in gain:
            current += al
            if current > highest:
                highest = current 
        return highest

'''
높이 0에서 출발하므로 현재 위치 current = 0, highest = 0으로 잡음
어짜피 최대 고도 구하는거니 Point 신경 안씀 
gain에 있는 거리들을 이동하면서 current 에 더해줌 
이때 current 가 현재까지 highest 를 넘으면 highest 덮어씀 
gain 끝나고 highest 출력
'''


        