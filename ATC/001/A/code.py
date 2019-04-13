from functools import reduce
import math
from collections import deque

def dfs(H,W,a):
    visited = []
    for i in range(H):
        visited.append(list(0 for _ in range(W)))
        for j in range(W):
            if a[i][j] == 's':
                sx = i
                sy = j
                
    q = deque([[sx,sy]])
    visited[sx][sy] = 1
    while q:
        x,y = q.popleft()
        if(a[x][y] == 'g'):
            return 'Yes'
        for i,j in ([1,0],[-1,0],[0,1],[0,-1]):
            next_x,next_y = x+i,y+j
            if(next_x<0 or next_x>=H or next_y<0 or next_y>=W):
                continue
            elif(a[next_x][next_y] != '#' and visited[next_x][next_y] == 0):
                visited[next_x][next_y] = 1
                q.appendleft([next_x,next_y])
    return 'No'
def bfs(H,W,a):
    visited = []
    for i in range(H):
        visited.append(list(0 for _ in range(W)))
        for j in range(W):
            if a[i][j] == 's':
                sx = i
                sy = j
                
    q = deque([[sx,sy]])
    visited[sx][sy] = 1
    while q:
        x,y = q.popleft()
        if(a[x][y] == 'g'):
            return 'Yes'
        for i,j in ([1,0],[-1,0],[0,1],[0,-1]):
            next_x,next_y = x+i,y+j
            if(next_x<0 or next_x>=H or next_y<0 or next_y>=W):
                continue
            elif(a[next_x][next_y] != '#' and visited[next_x][next_y] == 0):
                visited[next_x][next_y] = 1
                q.append([next_x,next_y])
    return 'No'

def main():
    # N! を求める
    # f = math.factorial(N)
    
    # 切り捨て
    # 4 // 3
    # 切り上げ
    #-(-4 // 3)
    
    # 初期値用:十分大きい数(100億)
    # 1e10

    # 初期値用:十分小さい数(-100億)
    # -1e10
    
    # 1文字のみを読み込み
    # 入力:2
    # a = input().rstrip()
    # 変数:a='2'
    
    # スペース区切りで標準入力を配列として読み込み
    # 入力:2 4 5 7
    # a, b, c, d = (int(_) for _ in input().split())  
    # 変数:a=2 b=4 c=5 d =7
    
    # 1文字ずつ標準入力を配列として読み込み
    # 入力:2 4 5 7
    # a = list(int(_) for _ in input().split())
    # 変数:a = [2, 4, 5, 7]    

    # 1文字ずつ標準入力を配列として読み込み
    # 入力:2457
    # a = list(int(_) for _ in input())
    # 変数:a = [2, 4, 5, 7]    
    H,W = (int(_) for _ in input().split())
    a = []
    for i in range(H):
        a.append(list(_ for _ in input()))
    print(dfs(H,W,a))
if __name__ == '__main__':
    main()
