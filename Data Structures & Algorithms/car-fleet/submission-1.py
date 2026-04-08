class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        # sort based on position with decreasing
        cars = sorted(zip(position, speed), reverse=True)
        time = [0] * n
        stack = []
        for pos, spd in cars:
            dist = target - pos
            time = dist/spd
            if stack and stack[-1] < time:
                stack.append(time)
            elif not stack:
                stack.append(time)
        return len(stack)

        