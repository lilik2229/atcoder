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
            for s in range(2501):            
                if(n>=1 and X[n-1] > s):
                    dp[n][k][s] = dp[n-1][k][s]
                elif(n>=1 and X[n-1] <= s):
                    dp[n][k][s] = dp[n-1][k][s] + dp[n-1][k-1][s-X[n-1]]
                print(n,k,s,dp[n][k][s])
    ans = 0
    for k in range(1,N+1):
        ans = ans + dp[N][k][k*A]
    print(ans)
if __name__ == '__main__':
    main()
