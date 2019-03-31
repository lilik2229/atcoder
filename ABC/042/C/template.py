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
    K = int(slist[1])
    D = input().rstrip().split(' ')

    for n in range(N,100000):
        # 各桁にDの配列にある数値がいるか
        d_flag = False
        tmp_n = list(str(n))
        # print(tmp_n)
        for tmp_char in tmp_n:
            if (str(tmp_char) in D):
                d_flag = True
                break
        if(d_flag == False):
            print(n)
            break
    
if __name__ == '__main__':
    main()
