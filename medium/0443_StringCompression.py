"""
Given an array of characters chars, compress it
char1 charcount1 char2 charcount2 ... 
return the new length.
"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        s = ""
        right = 0
        count = 0  
        while right < len(chars)-1:
            right +=1
            count +=1
            if chars[right-1]!=chars[right]: 
                s+=chars[right-1]
                if count > 1:
                    s+=str(count)
                count = 0    
        count +=1    
        s+=chars[right]
        if count >1: 
            s+=str(count)

        chars[:]=list(s)
        return list(s)

chars = ["a","b","b","b","b","b","b","b","b","b","b","b","b"]
print(Solution().compress(chars))

f"""
ls[set(ls)]으로 중복제거
chars.count(ls[i])

        s = ""
        ch_ls = list(set(chars))
        for ch in sorted(ch_ls):
            count = chars.count(ch)
            if count>1:
                s+=ch+str(count)
            else:
                s+=ch
        chars[:]=list(s)
        return len(chars)

1차시도 실패: 같은 ch가 다른 위치에 연속 할수있음 

현재(right) 값이 왼쪽 값과 달라질때까지 카운트해서 count가 1을 넘기면 숫자를 더해주는 방식으로 수정
이때 마지막 값이 안잡혀서 while문 종료 후 count에 1을 더해줘서 마지막 값을 처리 
    - 마지막으로 잡은 현재 값이 왼쪽과 달랐다면 count 가 0이므로 마지막으로 기록된 right의 개수는 1로 s+=chars[right]만추가됨
    - 마지막으로 잡은 현재 값이 왼쪽과 같다면 count가 1 이상으로 s+=chars[right]+str(count)로 추가됨
2차시도 성공 

"""