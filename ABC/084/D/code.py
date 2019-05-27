from functools import reduce
import math
import collections
## エラトステネスの篩
def eratosthenes(num):
    is_prime = [1]*num
    is_prime[0] = 0
    is_prime[1] = 0
    for i in range(2,num):
        if is_prime[i] == 1:
            for j in range(i*i,num,i):
                is_prime[j] = 0
    return is_prime
            
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

    # N の逆元
    # N_inv = pow(N,MOD-2,MOD)

    # nCr
    # Nの階乗 * rの階乗の逆元 * n-rの階乗の逆元
    
    # 切り捨て
    # 4 // 3
    # 切り上げ
    #-(-4 // 3)
    
    # 初期値用:十分大きい数(100億)
    INF = float("inf")

    # 大きな素数
    MOD = 10**9+7
    
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
    Q = int(input())
    l = []
    r = []
    for i in range(Q):
        s1, s2 = (int(_) for _ in input().split())
        l.append(s1)
        r.append(s2)
    cnt = 1
    is_prime = eratosthenes(100005)

    c = [0]*100005
    for i in range(3,100005,2):
        if is_prime[i] ==1 and is_prime[(i+1)//2] ==1:
            c[i] = 1

    for i in range(1,100004):
        c[i+1] += c[i]
    ans = []    
    for i in range(Q):
        ans.append(c[r[i]]-c[l[i]-1])
            
    print('\n'.join(str(_) for _ in ans))
    
if __name__ == '__main__':
    main()
