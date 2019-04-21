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
    N = int(input().rstrip())
    S = list(_ for _ in input())
    
    # 基準点iより右にいる白石の数と基準点iより左にいる黒石の数の和が答え
    # i=0 のとき答えは文字列中の白石の数になる
    cnt_w = S.count('.') # iより右みいる白石の数
    cnt_b = 0 # iより左にいる文字列中の黒石の数
    ans = cnt_w 
    for i in range(N): # i番目の石を左に置くとき       
        if(S[i] == '#'): # 黒石を左に置く場合
            cnt_b +=1
        else: # 白石を左に置く場合
            cnt_w -=1
        ans = min(ans,cnt_b+cnt_w)
    print(ans)
    
if __name__ == '__main__':
    main()
