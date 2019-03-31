from functools import reduce

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    slist = input().rstrip().split(' ')
    H = int(slist[0])
    W = int(slist[1])
    A = int(slist[2])
    B = int(slist[3])
    
    
if __name__ == '__main__':
    main()
