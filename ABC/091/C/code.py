from functools import reduce
import math
from operator import itemgetter

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
    ab = []
    cd = []
    for i in range(N):
        s1, s2 = (int(_) for _ in input().split())
        ab.append((s1,s2))
    for i in range(N):
        s1, s2 = (int(_) for _ in input().split())
        cd.append((s1,s2))
    cnt = 0
    ab = sorted(ab, key = itemgetter(0))
    cd = sorted(cd, key = itemgetter(0))
    for i in range(N):
        rp = -1
        tmp = -1
        for j in range(len(ab)):
            # print(ab[j],cd[i])
            if ab[j][0]<cd[i][0] and ab[j][1]<cd[i][1]:
                if ab[j][1] > tmp:                    
                    tmp = ab[j][1]
                    rp = j
        if rp >=0:
            # print(ab[rp])
            ab.pop(rp)
            cnt +=1
    print(cnt)
    
if __name__ == '__main__':
    main()
