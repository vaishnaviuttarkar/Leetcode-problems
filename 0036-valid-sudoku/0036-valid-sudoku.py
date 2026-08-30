class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        p = True
        
        # 1. Check Rows
        for row in board:
            a = [item for item in row if item != '.']
            p = p * (len(a) == len(set(a)))
            
        # 2. Check Columns
        for col in zip(*board):
            b = [item for item in col if item != '.']
            p = p * (len(b) == len(set(b)))
            
        # 3. Check 3x3 Sub-boxes
        for r in range(0, 9, 3):       # Jump to the start of each box row (0, 3, 6)
            for c in range(0, 9, 3):   # Jump to the start of each box column (0, 3, 6)
                
                # Extract and flatten the 3x3 grid into a single list
                box = []
                for i in range(3):
                    for j in range(3):
                        box.append(board[r + i][c + j])
                
                # Apply your exact duplicate checking logic
                box_filtered = [item for item in box if item != '.']
                p = p * (len(box_filtered) == len(set(box_filtered)))
                
        return bool(p)
