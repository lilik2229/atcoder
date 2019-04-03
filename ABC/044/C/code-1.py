from functools import reduce

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    N, A = [int(_) for _ in input().split()]
    X = [int(_) for _ in input().split()]

    # dp[n][s] : n枚目まで選んで合計をsにする場合の数
    dp = [[0 for _ in range(10000)] for _ in range(N+1)]
    dp[0][0] = 1
    
    for n in range(N+1):
        for s in range(A+1):
            if(n>=1 and s<X[n-1]):
                dp[n][s] = dp[n-1][s]
            if(n>=1 and s>=X[n-1]):
                dp[n][s] = dp[n-1][s] + dp[n-1][s-X[n-1]]

    # Ans = 0
    # for i in range(1,N+1):
    #     Ans += dp[N][i][i*A]
 
    print(dp[N][A])
    
if __name__ == '__main__':
    main()
