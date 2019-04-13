from functools import reduce
import math

def main():
    # N! を求める
    # f = math.factorial(N)
    
    # 切り捨て
    # 4 // 3
    # 切り上げ
    #-(-4 // 3)
    
    # 初期値用:十分大きい数(100億)
    # 1e10

    # 初期値用:十分小さい数(-100億)
    # -1e10
    
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
    N,M = (int(_) for _ in input().split())
    if(M<2):
        print(0)
        exit()
    if N>M//2:
        N = N-(N - M//2)
    ans = (N*2 + M)//4
    # while True:
    #     N = N -1
    #     M = M -2
    #     ans = ans + 1
    #     if(N<=0 or M<=0):
    #         break
    # if(N<=0 and M>0):
    #     ans = ans + M//4
             
    print(ans)
    
if __name__ == '__main__':
    main()
