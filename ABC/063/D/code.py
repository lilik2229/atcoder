from functools import reduce
import math

def is_ok(t,h,A,B):
    cnt = 0 # 必要な攻撃回数
    for hp in h:
        cnt += max(0,math.ceil((hp-B*t)/(A-B)))
    if t >= cnt:
        return True
    else:
        return False

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
    N,A,B = (int(_) for _ in input().split())
    h = []
    max_h = 0
    for i in range(N):
        h.append(int(input()))
        max_h = max(h[i],max_h)        
    ng = -1
    ok = math.ceil(max_h/B) # 考えうる最大の攻撃回数

    # 二分探索
    while (abs(ok-ng)>1):
        mid = (ok + ng) //2
        if is_ok(mid,h,A,B):
            ok = mid
        else:
            ng = mid
    print(ok)
    
if __name__ == '__main__':
    main()

