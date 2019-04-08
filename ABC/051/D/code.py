from functools import reduce

def main():
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
    N, M = (int(_) for _ in input().split())
    d = [[1e10 for _ in range(N)] for _ in range(N)]
    a = []
    b = []
    c = []
    for i in range(M):
        ai, bi, ci = (int(_) for _ in input().split())
        d[ai-1][bi-1] = ci
        d[bi-1][ai-1] = ci
        a.append(ai-1)
        b.append(bi-1)
        c.append(ci)
        
    for i in range(N):
        d[i][i] = 0       
        
    for i in range(N):
        for j in range(N):
            for k in range(N):
                d[j][k] = min(d[j][i]+d[i][k],d[j][k])

    ans = M
    for i in range(M):
        is_shortest = False
        for j in range(N):
            if(d[j][a[i]]+c[i] == d[j][b[i]]):
                is_shortest = True
        if is_shortest:
            ans -= 1
    print(ans)
    
if __name__ == '__main__':
    main()
