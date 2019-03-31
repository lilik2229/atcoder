from functools import reduce

def main():
    s = input().rstrip().split(' ')
    if int(s[0]) % 2 == 0 or int(s[1]) % 2 == 0:
        print('Even')
    else:
        print('Odd')
    
if __name__ == '__main__':
    main()
