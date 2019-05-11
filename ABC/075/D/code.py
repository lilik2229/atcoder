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
    N, K = (int(_) for _ in input().split())
    p = []
    for i in range(N):
        x,y = (int(_) for _ in input().split())
        p.append((x,y))
        
    ans = INF
    for i in range(N):
        for j in range(i+1,N):
            for h in range(N):
                for g in range(h+1,N):
                    x_start = min(p[i][0],p[j][0])
                    y_start = min(p[h][1],p[g][1])
                    x_end = max(p[i][0],p[j][0])
                    y_end = max(p[h][1],p[g][1])
                    area = (x_end - x_start) * (y_end - y_start)
                    cnt = 0
                    for k in range(N):
                        if p[k][0] >= x_start and p[k][1] >= y_start and p[k][0] <= x_end and p[k][1] <= y_end:
                            cnt += 1
                            if cnt == K:
                                ans = min(ans,area)
                                break
    print(ans)
    
if __name__ == '__main__':
    main()
