from functools import reduce

def main():
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    s = list(input().rstrip())
    ans = []
    i = 0
    for char in s:
        if char=='0' or char=='1':
            ans.append(char)
        elif char=='B' and len(ans) > 0:
            ans.pop()
    
    print(''.join(ans))    
   
if __name__ == '__main__':
    main()
