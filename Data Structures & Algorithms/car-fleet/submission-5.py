class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        time: O(nlogn) sorting
        space: O(n) zip for sorting
        approach: (no stack) track last_time
        """
        # n = len(position)
        # # sort based on position with decreasing
        # cars = sorted(zip(position, speed), reverse=True)
        # ans = 0
        # last_ele = -1
        # for pos, spd in cars:
        #     dist = target - pos
        #     time = dist/spd
        #     if last_ele < time:
        #         ans += 1
        #         last_ele = time
        # return ans

        """
        time: O(nlogn)
        space: O(n)
        approach: last_time + (no stack) + (no zip)
        """
        n = len(position)
        indices = list(range(n))
        indices.sort(key=lambda i: position[i], reverse=True)
        ans = 0
        last_time = -1
        for idx in indices:
            dist = target - position[idx]
            time = dist / speed[idx]
            if last_time < time:
                ans += 1
                last_time = time
        return ans


        