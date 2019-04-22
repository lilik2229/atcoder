from functools import reduce
import math
from collections import deque
from collections import defaultdict

def bfs(i,d,N):
    q = deque()
    q.append(i)
    d_from_1 = [-1]*(N+1)
    d_from_1[i] = 0
    i = 1
    while q:
        l = len(q)
        for j in range(l):
            next_node = q.popleft()
            for succ in d[next_node]:
                if d_from_1[succ] == -1:
                    d_from_1[succ] = i
                    q.append(succ)
        i += 1
    return d_from_1
    
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
    N = int(input().rstrip())
    a = []
    b = []
    d = defaultdict(list)
    
    for i in range(N-1):
        s1,s2 = list(int(_) for _ in input().split())
        d[s1].append(s2)
        d[s2].append(s1)       
    f= 0
    s= 0
    d_from_1 = bfs(1,d,N)
    d_from_N = bfs(N,d,N)
        
    # print(d_from_1)
    # print(d_from_N)
    for i in range(1,N+1):
        if(d_from_1[i] <= d_from_N[i]):
            f += 1
        else:
            s += 1
    if(f>s):
        print('Fennec')
    else:
        print('Snuke')
if __name__ == '__main__':
    main()
