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
    N = int(input().rstrip())
    factor = []
    f = math.factorial(N)
    dict = {}
    ans = 1
    for num in range(2,1000):
        while f % num == 0:
            f //= num
            factor.append(num)
            if num in dict:
                dict[num] += 1
            else:
                dict[num] = 1
    for v in dict.values():
        ans *= v + 1

    print(ans % (10**9 + 7))
    
if __name__ == '__main__':
    main()
