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
    INF = float("inf")
    
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
    S = list(_ for _ in input())

    S_num = []
    index = 0 
    now = ''
    if(S[0]=='#'):
        S_num.append(1)
        now = '#'
    else:
        S_num.append(-1)
        now = '.'
        
    for i in range(1,N):
        if(S[i]=='#' and now =='#'):
            S_num[index] +=1
        elif(S[i]=='.' and now =='.'):
            S_num[index] +=-1
        elif(S[i]=='#' and now !='#'):
            S_num.append(1)
            now = '#'
            index +=1
        elif(S[i]=='.' and now !='.'):
            S_num.append(-1)
            now = '.'
            index +=1
    # print(S_num)
    ans = 0
    b = 0
    w = 0
    # ###.#.. → 3,-1,1,-2 → 5,-2
    # #...#.. → 1,-3,1,-2 → 1,-2
    for i in range(len(S_num)-1):
        if(S_num[i]>0 and S_num[i+1]<0):
            b += S_num[i]
            w += -S_num[i+1]
            # ans += min(S_num[i],-S_num[i+1])
            # if((S_num[i] > -S_num[i+1]) and i+2 < len(S_num)-1):
            #     S_num[i+2] += S_num[i] -S_num[i+1]
    ans = min(b,w)
    print(ans)
    
if __name__ == '__main__':
    main()
