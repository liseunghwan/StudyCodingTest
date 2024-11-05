#안전지대

def solution(board):
    n = len(board)
    
    directions = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1, -1), (-1,1), (-1,-1)]
    
    def is_valid(x,y):
        return 0 <= x < n and 0 <= y < n
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                for dx, dy in directions:
                    nx, ny = i + dx, j + dy
                    if is_valid(nx, ny) and board[nx][ny] == 0:
                        board[nx][ny] = 2
                            
    
    safe_area = sum(row.count(0) for row in board)
    
    
    return safe_area