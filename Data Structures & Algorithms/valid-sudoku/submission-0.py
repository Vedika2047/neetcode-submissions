class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = [set() for _ in range(9)]
        col = [set() for _ in range(9)]
        box = [set() for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                else: 
                    num = board[r][c]
                    if num in row[r]:
                        return  False
                    else:
                        row[r].add(num)    
                    if num in col[c]:
                        return False 
                    else:
                        col[c].add(num)
                    box_index = (r//3)*3+(c//3)
                    if num in box[box_index]:
                        return False
                    else:
                        box[box_index].add(num)     

        return True                            

        