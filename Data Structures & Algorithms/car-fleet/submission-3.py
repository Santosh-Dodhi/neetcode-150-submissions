class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        time: O(nlogn) sorting
        space: O(n) zip for sorting
        approach: stack
        """
        n = len(position)
        # sort based on position with decreasing
        cars = sorted(zip(position, speed), reverse=True)
        ans = 0
        last_ele = -1
        for pos, spd in cars:
            dist = target - pos
            time = dist/spd
            if last_ele < time:
                ans += 1
                last_ele = time
        return ans

        