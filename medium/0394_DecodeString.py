class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """

        ## ]기준으로 문자열을 묶으므로 ']'나올때까지 stack에 쌓음
        ##
        stack=[]
        for ch in s:
            ## ']'가 아니면 stack에 쌓기
            if ch != ']':
                stack.append(ch)
            else: 
                ## ']'가 나오면 stack 안에 '[' 가 나올때까지 문자열 뽑아서 저장
                current_str=''
                while stack and stack[-1]!='[':
                    current_str = stack.pop()+current_str #pop으로 뽑으면 순서 뒤바껴서
                stack.pop() #'[' stack에서 뻄
                num_str=''
                while stack and stack[-1].isdigit():
                    num_str = stack.pop()+num_str
                stack.append(current_str*int(num_str))
        return ''.join(stack)
    

