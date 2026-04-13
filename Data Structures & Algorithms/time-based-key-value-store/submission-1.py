class TimeMap:
    from collections import defaultdict
    def __init__(self):
        self.dic = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((timestamp, value))
        
    def get(self, key: str, timestamp: int) -> str:
        print(self.dic)
        nums = self.dic[key]
        print(nums)
        if not nums:
            return ""
        n = len(nums)
        i = n - 1
        while i >= 0:
            if nums[i][0] == timestamp:
                return nums[i][1]
            elif nums[i][0] > timestamp:
                i -= 1
            else:
                return nums[i][1]
        return ""

        
