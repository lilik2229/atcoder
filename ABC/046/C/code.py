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

    # 1文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    # N, A = [int(_) for _ in input().split()]
    # X = [int(_) for _ in input().split()]
    N = int(input().rstrip())
    T=[]
    A=[]
    x=[]
    ans = 0
    for i in range(N):
        t, a = [int(_) for _ in input().rstrip().split(' ')]
        T.append(t)
        A.append(a)
    x.append(1)
    for i in range(1,N):
        x.append(max(-1*(-1*(T[i-1] *  x[i-1])//T[i]),-1*(-1*(A[i-1] *  x[i-1])//A[i])))
        t = x[i] * T[i]
        a = x[i] * A[i]
    print(t+a)
if __name__ == '__main__':
    main()
