#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argsLst = sys.argv
    lenArgs = len(argsLst)
    idx = 1
    if lenArgs >= 2:
        if lenArgs == 2:
            print('{} argument:'.format(lenArgs - 1))
        else:
            print('{} arguments:'.format(lenArgs - 1))
        for args in range(lenArgs - 1):
            print('{}: {}'.format(idx, argLst[idx]))
        idx += 1
    else:
        print('0 arguments')
