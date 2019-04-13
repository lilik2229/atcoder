from functools import reduce
import math

def main():
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
    S = list(_ for _ in input())
    S = S[::-1]    
    S_num = 0
    temp_ans_0 = '0b'
    temp_ans_1 = '0b'
    num_temp_ans_0 = 0
    num_temp_ans_1 = 0
    for i in range(len(S)):
        if(i%2 ==0):
            temp_ans_0 += '0'
            temp_ans_1 += '1'
        else:
            temp_ans_0 += '1'
            temp_ans_1 += '0'
    # i = 0
    # for s in S:
    #     S_num += int(s) * 2**i
    #     if(i%2 ==0):
    #         num_temp_ans_0 += 0 * 2**i
    #         num_temp_ans_1 += 1 * 2**i
    #     else:
    #         num_temp_ans_0 += 1 * 2**i
    #         num_temp_ans_1 += 0 * 2**i
    #     i +=1
    S_str ='0b'+''.join(S)
    S_num = int(S_str,0)
    num_temp_ans_0 = int(temp_ans_0,0)
    num_temp_ans_1 = int(temp_ans_1,0) 
    c0 = bin(S_num ^ num_temp_ans_0).count('1')
    c1 = bin(S_num ^ num_temp_ans_1).count('1')
    
    print(min(c0,c1))
    
if __name__ == '__main__':
    main()
