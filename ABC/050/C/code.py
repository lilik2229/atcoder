from functools import reduce
import bisect

def main():
    # 切り捨て
    # 4 // 3
    # 切り上げ
    #-(-4 // 3)
    
    # 初期値用:十分大きい数(100億)
    # 1e10

    # 初期値用:十分小さい数(-100億)
    # -1e10

    # mod用
    p=10**9+7
    
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
    A = list(map(int, input().split()))
    # A = list(int(_) for _ in input().split())
    # A = list(input().split())
    A.sort()
    flag = False
    if A[0] == 0 and N%2 == 1:
        flag = True
        for i in range(N):
            if A[i] != (i + 1) // 2 * 2:
                flag = False
                break
    if A[0] == 1 and N%2 == 0:
        flag = True
        for i in range(N):
            if A[i] != i // 2 * 2 + 1:
                flag = False
                break
    if flag:
        print(2**(N//2) % p)
    else:
        print(0)
        
if __name__ == '__main__':
    main()
