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
    H,W = (int(_) for _ in input().split())

    ans = INF
    for h in range(1,H):
        if W%2 == 0:
            a= h*W//2
            b= h*W//2
        else:
            a= h*(W-1)//2
            b= h*(W+1)//2
        c= (H-h)*W
        s_max = max(a,b,c)
        s_min = min(a,b,c)
        ans = min(ans,s_max - s_min)

        a= h*W
        if (H-h)%2 == 0:
            b= (H-h)//2*W
            c= (H-h)//2*W
        else:
            b= (H-h-1)*W
            c= (H-h+1)*W
        s_max = max(a,b,c)
        s_min = min(a,b,c)
        ans = min(ans,s_max - s_min)
        
    for w in range(1,W):
        if H%2 == 0:
            a= w*H//2
            b= w*H//2
        else:
            a= w*(H-1)//2
            b= w*(H+1)//2
        c= (W-w)*H
        s_max = max(a,b,c)
        s_min = min(a,b,c)
        ans = min(ans,s_max - s_min)

        a= w*H
        if (W-w)%2 == 0:
            b= (W-w)//2*H
            c= (W-w)//2*H
        else:
            b= (W-w-1)//2*H
            c= (W-w+1)//2*H
        s_max = max(a,b,c)
        s_min = min(a,b,c)
        ans = min(ans,s_max - s_min)
        
    print(ans)
    
if __name__ == '__main__':
    main()
