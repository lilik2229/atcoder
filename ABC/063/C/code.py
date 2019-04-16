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
    s = []
    for i in range(N):
        s.append(int(input().rstrip()))
    s.sort()
    ans = 0
    
    if sum(s) % 10 != 0:
        ans = sum(s)
        print(ans)
        exit()
    for i in range(N):
        if(s[i]%10 !=0 ):
            ans = sum(s) - s[i]
            break
    # dp = []
    # for i in range(N):
    #     dp.append([-1]*(100*100))
    # dp[0][s[0]] = 1
    # for i in range(1,N):
    #     for j in range(100*100):
    #         if(j == s[i] or (j-s[i]>=0 and dp[i-1][j-s[i]]==1)):
    #             dp[i][j] = 1
    #         else:
    #             dp[i][j] = dp[i-1][j]
    # ans = 0
    # for i in range(100*100-1,0,-1):
    #     if(i%10 != 0 and dp[N-1][i]==1):
    #         ans = i
    #         break
    print(ans)
if __name__ == '__main__':
    main()
