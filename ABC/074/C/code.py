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
    A,B,C,D,E,F = (int(_) for _ in input().split())
    memo = {}
    for a in range(31):
        for b in range(31):
            for c in range(101):
                for d in range(101):
                    w = (100*A)*a +(100*B)*b
                    s = c*C + d*D
                    if w ==0:
                        break
                    elif w + s > F:
                        break
                    else:
                        if w/100 * E >= s:
                            density = 100 * s/(w+s)
                            memo[a,b,c,d] = density
    max_density = max(memo.values())
    for k,v in memo.items():
        if v==max_density:
            print((100*A)*k[0] +(100*B)*k[1]+k[2]*C + k[3]*D,k[2]*C + k[3]*D)
            break
    
if __name__ == '__main__':
    main()
