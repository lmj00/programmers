from collections import Counter
import copy

def solution(board):
    check = [[-1, -1], [-1, 0], [-1, 1], [0, 0], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]]
    copy_board = copy.deepcopy(board)
    result = 0
    
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 1:
                for k in check:
                    if -1 < i + k[0] < len(board) and -1 < j + k[1] < len(board):
                        copy_board[i + k[0]][j + k[1]] = 1
    
    
    for i in copy_board:
        c = Counter(i).most_common()

        if c[0][0] == 0:
            result += c[0][1] 
        elif len(c) > 1 and c[1][0] == 0:
            result += c[1][1]
    
    return result