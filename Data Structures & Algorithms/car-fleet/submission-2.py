class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        time: O(nlogn) sorting
        space: O(n)
        approach: stack
        """
        n = len(position)
        # sort based on position with decreasing
        cars = sorted(zip(position, speed), reverse=True)
        time = [0] * n
        # stack = []
        ans = 0
        last_ele = -1
        for pos, spd in cars:
            dist = target - pos
            time = dist/spd
            # if stack and stack[-1] < time:
            #     stack.append(time)
            # elif not stack:
            #     stack.append(time)
            if last_ele < time:
                ans += 1
                last_ele = time
        return ans

        