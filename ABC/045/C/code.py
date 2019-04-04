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
    s = list(input().rstrip())
    # N, A = [int(_) for _ in input().split()]
    # X = [int(_) for _ in input().split()]
    sum = 0
    for i in range(1 << len(s)-1):
        e = s[0]
        for j in range(len(s)-1):
            # iのうち、jbit目が立っているか
            if(i & (1 << j)):
                e = e + '+' + s[j+1]
            else:
                e = e + s[j+1]
        sum += eval(e)
        
    print(sum)
if __name__ == '__main__':
    main()
