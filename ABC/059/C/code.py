from functools import reduce
import math

def main():
    # 文字列の2進数を数値にする
    # '101' → '5'
    # 文字列の頭に'0b'をつけてint()にわたす
    # binary = int('0b'+'101',0)

    # 2進数で立っているbitを数える
    # 101(0x5) → 2
    # cnt_bit = bin(5).count('1')
    
    # N! を求める
    # f = math.factorial(N)
    
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
    N = int(input().rstrip())
    a = list(int(_) for _ in input().split())
    sum = a[0]
    sum2 = a[0]
    ans_o = 0
    ans_e = 0
    if a[0] <= 0:
        sum = 1
        ans_o = -a[0]+1
    if a[0] >= 0:
        sum2 = -1
        ans_e = a[0]+1
    
    for i in range(1,len(a)):
        sum +=a[i]
        if(i%2 ==1 and sum>=0):
            ans_o += sum+1
            sum = -1
        elif(i%2 ==0 and sum <= 0):
            ans_o += -sum+1
            sum = 1
            
        sum2 +=a[i]
        if(i%2 ==0 and sum2>=0):
            ans_e += sum2+1
            sum2 = -1
        elif(i%2 ==1 and sum2 <= 0):
            ans_e += -sum2+1
            sum2 = 1
            
    print(min(ans_o,ans_e))
    
if __name__ == '__main__':
    main()
