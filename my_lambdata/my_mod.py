# example from lecture video
def enlarge(n):
    '''
    param n is a int

    function will elarge n by 100
    '''
    return n * 100


if __name__ == '__main__':
    y = int(input("please choose a number: "))
    print(y, enlarge(y))