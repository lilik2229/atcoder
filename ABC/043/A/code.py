from functools import reduce

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    n = int(input().rstrip())
    ans = 0
    for i in range(1,n+1):
        ans = ans + i
    print(ans)    
   
if __name__ == '__main__':
    main()
