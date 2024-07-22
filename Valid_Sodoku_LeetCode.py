class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        # Validate Rows
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[i][j]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
        
        # Validate Cols
        for i in range(9):
            s = set()
            for j in range(9):
                item = board[j][i]
                if item in s:
                    return False
                elif item != '.':
                    s.add(item)
            
        # Validate Boxes
        starts = [(0, 0), (0, 3), (0, 6),
                  (3, 0), (3, 3), (3, 6),
                  (6, 0), (6, 3), (6, 6)]
        
        for i, j in starts:
            s = set()
            for row in range(i, i+3):
                for col in range(j, j+3):
                    item = board[row][col]
                    if item in s:
                        return False
                    elif item != '.':
                        s.add(item)
        return True

#my original code which somehow didn't run on leet code
#class Solution:
#	def isValidSukoku(self, board:list[list[str]]) -> bool:
#
##			seen = set()
#			for j in range(9):
#				item = board[i][j]
#				if item in seen:
#					return False
#				elif item != ".":
#					seen.add(item)
#
#3#			for i in range(9):
	#			if board[i][j] in seen:
	#				return False
	#				seen.add(board[j][i])
#
#
#		boxes = [(0,0),(0,3),(0,6),(3,0),(3,3),(3,6),(6,0),(6,3),(6,6)]
#
#		for i,j in boxes:
#			seen = set()
#
#
#			for row in range(i,i+3):
#				for column in range(j,j+3):
#					if board[row][column] in seen:
#						return False
#					elif board[row][column] !='.':
#						seen.add(board[row][column])
#
#		return True
#








					
