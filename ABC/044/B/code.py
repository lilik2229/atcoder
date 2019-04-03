from functools import reduce

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    s = list(input().rstrip())
    dict = {}
    b_flag = True
    for char in s:
        if(char in dict.keys()):
            dict[char] = dict[char] + 1
        else:
            dict[char] = 1
        
    for v in dict.values():
        if v % 2 == 1:
            b_flag = False
    if b_flag:
        print('Yes')
    else:
        print('No')
        
if __name__ == '__main__':
    main()
