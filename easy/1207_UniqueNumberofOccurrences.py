class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr_set = set(arr)
        arr_dict = {}
        for i in arr_set:
            arr_dict[i]= arr.count(i)
        print(arr_dict)
        return len(arr_dict) == len(set(arr_dict.values()))

arr = [1,2,2,1,1,1]
print(Solution().uniqueOccurrences(arr))
            


