class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        opening= ["(","{","["]
        match = {")": "(", "}": "{", "]": "["}
        stack = []

#닫는 괄호가 처음에 나오면 False 
#여는괄호가 처음에 나오면 stack 에 추가 다음으로 진행 
    #다음에 나오는 괄호가 여는괄호일 시 stack 에 추가 
    #다음에 나오는 괄호가 닫는괄호일 시 false 
    #다음에 나오는 괄호가 일치하는 닫는괄호일 시 stack 에서 제거 
    #마지막에 stack 이 비어있으면 True 아니면 False 

        for i, char in enumerate(s):
            if i == 0 and char not in opening: #닫는 괄호로 시작하면 False
                return False
            
            if char in opening: #여는 괄호일 시 stack 에 추가 
                stack.append(char)
                continue
            elif char not in opening: #닫는 괄호 일 시 
                if not stack or stack[-1]!=match[char]: # stack 이 비어있거나 마지막 stack open이 Not match면 False
                    return False
                else: #stack open이 match면 stack 에서 제거
                    stack.pop()

        return not stack


                
# s = "()"
# s = "()[]{}"
# s = "(]"
# s = "([])"
s = "([)]"
print(Solution().isValid(s))