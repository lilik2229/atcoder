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
    S = list(input().rstrip())
    tmp_color = S[0]
    ans=0 
    for i in range(len(S)):
        if(tmp_color != S[i]):
            tmp_color = S[i]
            ans += 1
    print(ans)
    
if __name__ == '__main__':
    main()
