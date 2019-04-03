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

    # dp[n][k][s] : n枚目までからk枚選んで合計をsにする場合の数
    dp = [[[0 for _ in range(2501)] for _ in range(N+1)] for _ in range(N+1)]
    dp[0][0][0] = 1
    
    for n in range(N+1):
        for k in range(n+1):
            for s in range(50*k+1):
                if(n>=1 and s<X[n-1]):
                    dp[n][k][s] = dp[n-1][k][s]
                if(n>=1 and s>=X[n-1]):
                    dp[n][k][s] = dp[n-1][k][s] + dp[n-1][k-1][s-X[n-1]]

    Ans = 0
    for i in range(1,N+1):
        Ans += dp[N][i][i*A]
 
    print(Ans)
    
if __name__ == '__main__':
    main()
