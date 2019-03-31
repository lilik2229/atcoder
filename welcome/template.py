from functools import reduce

def main():
    s = input().rstrip().split(' ')
    if s[0] % 2 == 0 or s[1] % 2 == 0:
        print('Even')
    else:
        print('Odd')
    
if __name__ == '__main__':
    main()
                
