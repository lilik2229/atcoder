import collections
from functools import reduce

def main():
    # 初期値用:十分大きい数(100億)
    # 1e10

    # 初期値用:十分小さい数(-100億)
    # -1e10

    # 1文字のみを読み込み
    # s = input().rstrip()
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 1文字ずつ標準入力を文字列として読み込み
    # s = list(input().rstrip())
    
    # 位置文字ずつ標準入力を数値配列として読み込み
    # X = [int(_) for _ in input().split()]
    X = [int(_) for _ in input().split()]
    if X[0] + X[1] == X[2] or X[0] + X[2] == X[1] or X[1] + X[2] == X[0]:
        print('Yes')
    else:
        print('No')

        
   
if __name__ == '__main__':
    main()
