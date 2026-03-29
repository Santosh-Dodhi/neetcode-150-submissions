class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        from collections import Counter
        def check_rows():
            for row in board:
                counter = Counter(row) 
                del counter["."]
                if set(counter.values()) - set([1]) == set():
                    continue
                else:
                    return False
            return True

        def check_cols():
            n = 9
            for j in range(n):
                dic = defaultdict(int)
                for i in range(n):
                    if board[i][j] != '.':
                        dic[board[i][j]] += 1
                # print(j, set(dic.values()))
                if set(dic.values()) - set([1]) == set():
                    continue
                else:
                    return False
            return True

        def check_squares():
            stpoints = [(0, 0), (0, 3), (0, 6), (3, 0), (3, 3), (3, 6), (6, 0), (6, 3), (6, 6)]
            for x, y in stpoints:
                dic = defaultdict(int)
                for i in range(x, x+3):
                    for j in range(y, y+3):
                        if board[i][j] != '.':
                            dic[board[i][j]] += 1
                if set(dic.values()) - set([1]) == set():
                    continue
                else:
                    return False
            return True
                        

        print(check_rows())
        print(check_cols())
        print(check_squares())

        return check_rows() and check_cols() and check_squares()




        