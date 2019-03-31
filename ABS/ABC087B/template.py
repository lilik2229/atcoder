from functools import reduce

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')
    
    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())

    A = int(input().rstrip())
    B = int(input().rstrip())
    C = int(input().rstrip())
    X = int(input().rstrip())
    ans = 0
    for A_i in range(0,A+1):
        for B_i in range(0,B+1):
            for C_i in range(0,C+1):
                if X == 500*A_i+100*B_i+50*C_i:
                    ans = ans+1
    print(ans)
   
if __name__ == '__main__':
    main()
