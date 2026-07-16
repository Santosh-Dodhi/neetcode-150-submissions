class LRUCache:
    from collections import OrderedDict
    def __init__(self, capacity: int):
        self.dic = OrderedDict()
        self.n = capacity

    def get(self, key: int) -> int:
        # check present if yes; shuffle(move this to end) and return value
        # not present return -1;
        
        if key in self.dic:
            self.dic.move_to_end(key, last=True)
            return self.dic[key]
        return -1

    def put(self, key: int, value: int) -> None:
        # check present update value; and shuffle(move this to end)
        # not present and n > 0 ; add key-value at end
        # not present and n < 0; remove first then add key-value at end
        
        if key in self.dic:
            self.dic.move_to_end(key, last=True)
            self.dic[key] = value #Remember updating value will not change the order
            return
        
        if self.n > 0:
            self.dic[key] = value #Remember insertion is always at the end
            self.n -= 1
            return
        else:
            self.dic.popitem(last=False)
            self.dic[key] = value
            return


