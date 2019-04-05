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
    
    # 1文字ずつ標準入力を数値配列として読み込み
    # X = [int(_) for _ in input().split()]
    s = input().rstrip().split(' ')
    W = int(s[0])
    W_S = 0
    H = int(s[1])
    H_S = 0
    N = int(s[2])
    x = []
    y = []
    a = []
    for i in range(N):
        s = input().rstrip().split(' ')
        x.append(int(s[0]))
        y.append(int(s[1]))
        a.append(int(s[2]))

    for i in range(N):
        if(a[i]==1 and x[i]>W_S ):
            W_S = x[i]
        elif(a[i]==2 and x[i]<W ):
            W = x[i]
        elif(a[i]==3 and y[i]>H_S ):
            H_S = y[i]
        elif(a[i]==4 and y[i]<H ):
            H = y[i]        
    if W-W_S <0 or H-H_S < 0:
        ans = 0
    else:
        ans = (W-W_S) * (H-H_S)
    print(ans)

if __name__ == '__main__':
    main()
