from functools import reduce

def main():
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')
    
    # 位置文字ずつ標準入力を配列として読み込み
    s = list(input().rstrip())
    
    print(int(s[0])+int(s[1])+int(s[2]))
   
if __name__ == '__main__':
    main()
