from functools import reduce
import math

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
    H,W = (int(_) for _ in input().split())
    S = []
    V = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
    
    for i in range(H):
        S.append(list(_ for _ in input()))
        
    for h in range(H):
        for w in range(W):
            cnt = 0
            if(S[h][w] == '.'):                
                for v in V:
                    if(h+v[0]<H and h+v[0]>=0 and w+v[1]<W and w+v[1]>=0 and S[h+v[0]][w+v[1]]=='#'):
                        cnt += 1
                S[h][w] = cnt
                        
    for h in range(H):
        print(''.join(str(_) for _ in S[h]))
    
if __name__ == '__main__':
    main()
