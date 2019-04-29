from functools import reduce
import math
import itertools

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
    N,M,R = (int(_) for _ in input().split())
    r = list(int(_)-1 for _ in input().split())
    a = []
    b = []
    c = []
    for i in range(M):
        s1,s2,s3 = (int(_) for _ in input().split())
        a.append(s1-1)
        b.append(s2-1)
        c.append(s3)
    d = []
    for i in range(N):
        d.append(list(INF for _ in range(N)))
        
    for i in range(N):
        for j in range(N):
            if i == j:
                d[i][j] = 0
    for i in range(M):
        if d[a[i]][b[i]] > c[i]:
            d[a[i]][b[i]] = c[i]
            d[b[i]][a[i]] = c[i]
    for k in range(N):
        for i in range(N):
            for j in range(N):
                if d[i][j] > d[i][k] + d[k][j]:
                    d[i][j] = d[i][k] + d[k][j]
    ans = INF
    for nodes in list(itertools.permutations(r)):
        cost = 0
        for i in range(len(nodes)-1):
            cost += d[nodes[i]][nodes[i+1]]
        ans = min(ans,cost)
    print(ans)
if __name__ == '__main__':
    main()
