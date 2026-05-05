class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        ## + - 순서는 colide , - 뒤에 + 는 변경 x 
        ## 따라서 - 만날때까지 abs 값이 더 작은 양수들 다 삭제 
        
        stack=[]
        for ast in asteroids:
            while stack and ast<0<stack[-1]:
                if stack[-1]<abs(ast):
                    stack.pop()
                    continue
                elif stack[-1]==abs(ast):
                    stack.pop()
                    break
                else:
                    break
            else: 
               stack.append(ast)
        return stack


asteroids = [5,10,-5]
solution = Solution()
print(solution.asteroidCollision(asteroids))