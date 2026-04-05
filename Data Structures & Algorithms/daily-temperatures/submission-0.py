class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        i = 0
        result = []
        while i < n:
            j =  i + 1
            flag = False
            while j < n:
                if temperatures[j] > temperatures[i]:
                    result.append(j-i)
                    flag = True
                    break
                j += 1
            if flag == False:
                result.append(0)
            i += 1
        return result
            
        