from functools import reduce

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    n = int(input().rstrip())
    slist = input().rstrip().split(' ')
    num_slist = []
    Alice = 0
    Bob = 0
    for i in range(0,n):
        num_slist.append(int(slist[i]))
    num_slist.sort(reverse = True)
    
    for i in range(0,n):
        if i % 2 == 0:
            Alice = Alice + int(num_slist[i])
        else:
            Bob = Bob + int(num_slist[i])
        
    print(Alice - Bob)    
   
if __name__ == '__main__':
    main()
