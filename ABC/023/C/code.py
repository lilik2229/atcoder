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
    
    # 切り捨て
    # 4 // 3
    # 切り上げ
    #-(-4 // 3)
    
    # 初期値用:十分大きい数(100億)
    INF = float("inf")
    
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
    R,C,K = (int(_) for _ in input().split())
    N = int(input().rstrip())
    candy = []
    NR = [0]*R
    NC = [0]*C
    for i in range(N):
        r,c = (int(_) for _ in input().split())
        candy.append((r-1,c-1))
        NR[r-1] +=1
        NC[c-1] +=1

    CS = [0]*101000
    # index個のアメのある列の数
    for nc in NC:
        CS[nc] += 1
    ret = 0
    for nr in NR:
        left = K - nr
        if left >= 0:
            ret += CS[left]
    for (r,c) in candy:
        if NR[r] + NC[c] == K:
            ret -=1
        elif NR[r] + NC[c] == K+1:
            ret +=1
    print(ret)
    
if __name__ == '__main__':
    main()
