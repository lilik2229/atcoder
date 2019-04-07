from functools import reduce
import copy

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
    N = int(input().rstrip())
    T = list(int(_) for _ in input().split())
    M = int(input().rstrip())
    A = []
    for i in range(M):
        tmp_T = copy.copy(T)
        sum = 0
        p, x = (int(_) for _ in input().split())
        tmp_T[p-1] = x
        for j in tmp_T:
            sum+= j
        A.append(str(sum))
    print('\n'.join(A))
    
if __name__ == '__main__':
    main()
