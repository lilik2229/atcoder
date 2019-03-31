from functools import reduce

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')
    
    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())

    n = input().rstrip()
    slist = input().rstrip().split(' ')
    c = 0
    exist_odd = False
    while(exist_odd == False):
        i = 0
        for s in slist:
            if int(s)%2 == 1:
                exist_odd = True
                continue            
            slist[i] = int(int(s)/2)
            i = i+1
        if exist_odd == False:
            c = c +1
    print(c)    
   
if __name__ == '__main__':
    main()
