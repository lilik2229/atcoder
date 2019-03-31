from functools import reduce

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    slist = input().rstrip().split(' ')
    N = int(slist[0])
    L = int(slist[1])
    S = []
    ans = ''
    for i in range(0,N):
        S.append(input().rstrip())
    S.sort()
    for i in range(0,N):
        ans = ans + S[i]
    print(ans)
   
if __name__ == '__main__':
    main()
