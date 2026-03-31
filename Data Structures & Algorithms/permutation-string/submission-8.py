class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m, n = len(s1), len(s2)
        count1 = [0]*26
        count2 = [0]*26
        for ch in s1:
            count1[ord(ch)-ord('a')] += 1

        i = 0
        for j, ch in enumerate(s2):
            count2[ord(ch)-ord('a')] += 1
            
            if j >= m:
                count2[ord(s2[i])-ord('a')] -= 1
                i += 1
            
            if count2 == count1:
                return True

        return False

            


        