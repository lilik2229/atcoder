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
    a = int(input().rstrip())
    b = int(input().rstrip())
    c = int(input().rstrip())
    d = int(input().rstrip())
    e = int(input().rstrip())
    k = int(input().rstrip())
    if abs(a - b) >k or abs(a - c) >k  or abs(a - d) >k or abs(a - e) >k or abs(b - c) >k or abs(b - d) >k  or abs(b - e) >k or abs(c - d) >k or abs(c - e) >k or abs(d - e) >k:
        print(':(')
    else:
        print('Yay!')
        
if __name__ == '__main__':
    main()
