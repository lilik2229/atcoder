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
    
    # 位置文字ずつ標準入力を数値配列として読み込み
    # X = [int(_) for _ in input().split()]
    
    SA = list(input().rstrip())
    SB = list(input().rstrip())
    SC = list(input().rstrip())
    SA.reverse()
    SB.reverse()
    SC.reverse()
    
    next = ''
    ans = ''
    for i in range(0,100+100+100+1):
        cur = next
        # print(cur)
        # print(SA)
        # print(SB)
        # print(SC)
        if i == 0:
            next = SA.pop()
        else :
            if next == 'a':
                if len(SA) > 0:
                    next = SA.pop()
                else:
                    ans = 'A'
                    break
            if next == 'b':
                if len(SB) > 0:
                    next = SB.pop()
                else:
                    ans = 'B'
                    break
            if next == 'c':
                if len(SC) > 0:
                    next = SC.pop()
                else:
                    ans = 'C'
                    break
    print(ans)
    
if __name__ == '__main__':
    main()
