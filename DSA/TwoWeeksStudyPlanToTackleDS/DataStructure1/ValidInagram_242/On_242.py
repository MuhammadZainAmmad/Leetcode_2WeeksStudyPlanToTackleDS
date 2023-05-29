# Time: O(n), Space: O(n)
class Solution(object):
    def isAnagram(self, s, t):
        dic = {}
        for char in s: # O(n)
            if char in dic:
                dic[char] += 1
            else: 
                dic[char] = 1

        for char in t: # O(n)
            if char not in dic:
                return False # b/c t has some extra character
            else:
                dic[char] -= 1

        for char_count in dic.values(): # O(n)
            if char_count != 0:
                return False # b/c both s and t should have same no of occurences of a character
        return True