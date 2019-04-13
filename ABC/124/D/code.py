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
    N,K = (int(_) for _ in input().split())
    S = list(int(_) for _ in input())
    now = 1
    cnt = 0
    Nums = []
    ans = 0
    left = 0
    right = 0
    tmp = 0
    for i in range(N):
        if(S[i]==now):
            cnt+=1
        else:
            Nums.append(cnt)
            now = 1 - now
            cnt=1
    if(cnt!=0):
        Nums.append(cnt)
    if(len(Nums)%2 == 0):
        Nums.append(0)
    Add = 2 * K +1
    sum = []
    sum.append(0)
    for i in range(0,len(Nums)):
        sum.append(sum[i] + Nums[i])
        
    for i in range(0,len(Nums),2):
        left = i
        right = min(i+Add,len(Nums))
        tmp = sum[right] - sum[left]
        # while(Nextleft>left):
        #     tmp -= Nums[left]
        #     left +=1
        # while(Nextright>right):
        #     tmp += Nums[right]
        #     right +=1        
        ans = max(tmp,ans)
    print(ans)
    
if __name__ == '__main__':
    main()
