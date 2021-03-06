from functools import reduce
from collections import deque
import math

def bfs(i,E,N):
    q = deque()
    q.append(i)
    d = [-1]*N
    d[i] = 0
    while q:
        next_node = q.popleft()
        for e in E[next_node]:
            if d[e[0]] == -1:
                d[e[0]] = d[next_node] + e[1]                
                q.append(e[0])
    return d
def main():
    # 文字列の2進数を数値にする
    # '101' → '5'
    # 文字列の頭に'0b'をつけてint()にわたす
    # binary = int('0b'+'101',0)

    # 2進数で立っているbitを数える
    # 101(0x5) → 2
    # cnt_bit = bin(5).count('1')
    
    # N! を求める
    # f = math.factorial(N)

    # N の逆元
    # N_inv = pow(N,MOD-2,MOD)

    # nCr
    # Nの階乗 * rの階乗の逆元 * n-rの階乗の逆元
    
    # 切り捨て
    # 4 // 3
    # 切り上げ
    #-(-4 // 3)
    
    # 初期値用:十分大きい数(100億)
    INF = float("inf")

    # 大きな素数
    MOD = 10**9+7
    
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
    N = int(input())
    a = []
    b = []
    c = []
    for i in range(N-1):
        s1,s2,s3 = list(int(_) for _ in input().split())
        a.append(s1-1)
        b.append(s2-1)
        c.append(s3)
    Q,K = list(int(_) for _ in input().split())
    x = []
    y = []
    for i in range(Q):
        s1,s2 = list(int(_) for _ in input().split())
        x.append(s1-1)
        y.append(s2-1)
    
    e = [[] for i in range(N)]
    for i in range(N-1):
        e[a[i]].append((b[i],c[i]))
        e[b[i]].append((a[i],c[i]))

    d = bfs(K-1,e,N)

    for i in range(Q):        
        print(d[x[i]]+d[y[i]])
    
if __name__ == '__main__':
    main()
