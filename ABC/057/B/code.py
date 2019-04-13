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
    a = []
    b = []
    c = []
    d = []
    ans = []
    for i in range(N):
        t1, t2 = (int(_) for _ in input().split())  
        a.append(t1)
        b.append(t2)
    for i in range(M):
        t1, t2 = (int(_) for _ in input().split())  
        c.append(t1)
        d.append(t2)

    for i in range(N):
        min_dist = 1e10
        ans.append(0)
        for j in range(M):
            dist = abs(a[i]-c[j])+abs(b[i]-d[j])
            if min_dist > dist:
                ans[i] = str(j+1)
                min_dist = dist
    print('\n'.join(ans))
    
if __name__ == '__main__':
    main()
