from functools import reduce

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')
    
    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())

    slist = input().rstrip().split(' ')
    N = int(slist[0])
    A = int(slist[1])
    B = int(slist[2])
    sum = 0
    
    for n in range(1,N+1):
        tmp_sum = 0
        i = n
        while(n>0):
            tmp_sum = tmp_sum + (n % 10)
            n = int(n/10)
        if tmp_sum >= A and tmp_sum <=B:
           sum = sum + i
    
        
    print(sum)    
   
if __name__ == '__main__':
    main()
