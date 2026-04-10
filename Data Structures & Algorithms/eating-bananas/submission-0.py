class Solution:
    def get_hours(self, piles, rate):
        ans = 0
        for ele in piles:
            ans += math.ceil(ele/rate)
        return ans      
        

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        st, end = 1, max(piles)
        while st <= end:
            mid = st + (end-st)//2
            myHour = self.get_hours(piles, mid)
            if myHour <= h:
                # decrease the rate
                end = mid - 1
            else:
                # increase the rate 
                st = mid + 1 
        return st