from functools import reduce

def main():
    # 初期値用:十分大きい数(100億)
    # 1e10

    # 初期値用:十分小さい数(-100億)
    # -1e10
    
    # 一文字のみを読み込み
    # s = input().rstrip().split(' ')
    
    # スペース区切りで標準入力を配列として読み込み
    # s = input().rstrip().split(' ')

    # 位置文字ずつ標準入力を配列として読み込み
    # s = list(input().rstrip())
    
    N = int(input().rstrip())
    a_list = input().rstrip().split(' ')
    cost = 0
    min_cost = 1e10
    for i in range(-100,101):
        cost = 0
        for a in a_list:
            a_num = int(a)
            cost = cost + (a_num - i) * (a_num-i)
            # print(i,a_num,cost)
        if(cost < min_cost):
            min_cost = cost
            # print('new ans',min_cost)
    print(min_cost)
    
if __name__ == '__main__':
    main()
