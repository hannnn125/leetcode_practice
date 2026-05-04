class Solution(object):
    def closeStrings(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: bool
        """
        word1_set = set(word1)
        word2_set = set(word2)
        if len(word1)!=len(word2) or word1_set!=word2_set:
            return False 
        word1_ls = []
        word2_ls = []
        for i in word1_set: 
            word1_ls.append(word1.count(i))
        for j in word2_set: 
            word2_ls.append(word2.count(j))
        if sorted(word1_ls)!=sorted(word2_ls): 
            return False 
        else: 
            return True