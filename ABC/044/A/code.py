from functools import reduce

def main():
    # 初期値用:十分大きい数(100億)
    # 1e10

    # 初期値用:十分小さい数(-100億)
    # -1e10

    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    N = int(input().rstrip())
    K = int(input().rstrip())
    X = int(input().rstrip())
    Y = int(input().rstrip())
    ans = 0
    if(N>K):
        ans = K*X + (N-K)*Y
    else:
        ans = N*X
    print(ans)   
   
if __name__ == '__main__':
    main()
