from collections import Counter
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        # subList=[[row[i] for row in grid] for i in range(len(grid))]
        # totalCount = sum([grid.count(sub) for sub in subList])
        # return totalCount
        
        totalCount=0
        rowCount = Counter(tuple(row) for row in grid) 
        # row 개수 e.g.,{(): ,(): ,():} 
        for i in range(len(grid)):
            column = tuple(grid[row][i] for row in range(len(grid)))
            totalCount+=rowCount[column]
        return totalCount

"""
1차 시도 성공/복잡도 O(n^3)
List comprehension 으로 일일히 행과 열을 비교-느림
->
2차 시도 해시맵 사용 복잡도 O(n^2)
"""
