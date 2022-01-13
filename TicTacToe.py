class TicTacToe(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.board = [[0]* n for i in range(n)]
        self.n = n

'''
        After Player1 has made his move, you need to mark the visited box in the board.
        '''
    def move(self, row, col, player):
        """
        :type row: int
        :type col: int
        :type player: int
        :rtype: int
        """
        self.board[row][col] = player
        n = self.n
        matrix = self.board

    def checkRow():
        for c in range(n):
            if matrix[r][c]!=player: return False
        return True

    def checkCol():
        for r in range(n):
            if matrix[r][c]!=player: return False
        return True

    def checkDiagonal():
        for d in range(n):
            if matrix[d][d]!=player: return False
        return True

    def checkAntiDiagonal():
        for r in range(n):
            if matrix[r][n-r-1]!=player:   # |Col index =x n-row-1|
                return False
            return True

    for r in range(n):
        if checkRow(r): return player

    for c in range(n):
        if checkCol(c): return player

    if checkDiagonal(): return player
    if checkAntiDiagonal(): return player

    return 0
        
        


# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)f