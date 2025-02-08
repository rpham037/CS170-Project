

class TreeNode:
    eight_goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]

    def __init__(self, parent, board, gCost, hCost=0): #Initialization of the TreeNode 
        self.parent = parent            #Points to parent node
        self.board = board              #The boards current state
        self.gCost = gCost            #Actual path cost from start node to current node
        self.hCost = hCost            #Heuristic cost exploring new paths
        self.fCost = gCost + hCost   #Total cost, A* algorithm
        

    def solvedBoard(self):
        return self.board == TreeNode.eight_goal_state

    def makeTuple(self):
        return tuple(map(tuple, self.board))

    
    #Function gets neighbors of the current board could be for 8 puzzle, 15 puzzle, or 25 puzzle
    #Function returns a list of new states of for the new board 
    def getNeighbors(self, pos):
        size = len(self.board)                           #Size of the board  
        x, y = pos                                  #Positions
        moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]  #Move about x and y axis
        
        for x1, y1 in moves:
            new_x = x + x1
            new_y = y + y1
            if 0 <= new_x < size and 0 <= new_y < size:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[new_x][new_y] = new_board[new_x][new_y], new_board[x][y]
                yield new_board, (new_x, new_y)


    #Function finds the blank space in the board indexing through the whole matrix
    def findBlank(self):
        size = len(self.board)
        for i in range(size):
            for j in range(size):
                if self.board[i][j] == 0:   
                    return i, j
        raise ValueError("Error! Blank space was not found in the board.")
