from functools import reduce

def main():
    # 切り捨て
    # 4 // 3
    # 切り上げ
    #-(-4 // 3)
    
    # 初期値用:十分大きい数(100億)
    # 1e10

    # 初期値用:十分小さい数(-100億)
    # -1e10
    
    # 1文字のみを読み込み
    # 入力:2
    # a = input().rstrip()
    # 変数:a='2'
    
    # スペース区切りで標準入力を配列として読み込み
    # 入力:2 4 5 7
    # a, b, c, d = (int(_) for _ in input().split())  
    # 変数:a=2 b=4 c=5 d =7
    
    # 1文字ずつ標準入力を配列として読み込み
    # 入力:2 4 5 7
    # a = list(int(_) for _ in input().split())
    # 変数:a = [2, 4, 5, 7]    

    # 1文字ずつ標準入力を配列として読み込み
    # 入力:2457
    # a = list(int(_) for _ in input())
    # 変数:a = [2, 4, 5, 7]
    T = [
        ['d','r','e','a','m'],
        ['d','r','e','a','m','e','r'],
        ['e','r','a','s','e'],
        ['e','r','a','s','e','r']
    ]
    # S = list(_ for _ in input())
    S = input()
    S = S[::-1]
    # S.reverse()
    # S.sort(reversed=True)

    for i in range(4):
        T[i].reverse()
    while len(S)>0:
        if(''.join(S[0:len(T[0])]) == ''.join(T[0])):
            S = S[len(T[0]):]
            # for i in range(len(T[0])):
            #     S.pop(0)
        elif(''.join(S[0:len(T[1])]) == ''.join(T[1])):
            S = S[len(T[1]):]
            # for i in range(len(T[1])):
            #     S.pop(0)
        elif(''.join(S[0:len(T[2])]) == ''.join(T[2])):
            S = S[len(T[2]):]
            # for i in range(len(T[2])):
            #     S.pop(0)
        elif(''.join(S[0:len(T[3])]) == ''.join(T[3])):
            S = S[len(T[3]):]
            # for i in range(len(T[3])):
            #     S.pop(0)
        else:
            print('NO')
            break
        
    if(len(S) ==0):
        print('YES')

    
if __name__ == '__main__':
    main()
