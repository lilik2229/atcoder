from functools import reduce

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    slist = input().rstrip().split(' ')
    if slist[0] == '5' and slist [1] == '5' and slist[2] == '7':
        print('YES')
    elif slist[0] == '5' and slist [1] == '7' and slist[2] == '5':
        print('YES')
    elif slist[0] == '7' and slist [1] == '5' and slist[2] == '5':
        print('YES')
    else:
        print('NO')
        
if __name__ == '__main__':
    main()
