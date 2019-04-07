from functools import reduce
import math

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
    S = []
    S.append(int(input().rstrip()))
    S.append(int(input().rstrip()))
    S.append(int(input().rstrip()))
    S.append(int(input().rstrip()))
    S.append(int(input().rstrip()))
    ans = 0
    min = S[0]
    min_i = 0
    sum = 0
    for i in range(len(S)):
        if min%10 > S[i]%10 and S[i]%10 != 0:
            min = S[i]%10
            min_i = i
    for i in range(len(S)):
        if i != min_i:
            sum += math.ceil(S[i]/10) * 10
        else:
            sum += S[i]
    print(sum)
if __name__ == '__main__':
    main()
