from exam import *
import sys
if __name__ == '__main__':
    if len(sys.argv) >= 2:
        filename = sys.argv[1]
    else:
        print('请输入要处理的文件名：',end = ' ')
        filename = input()
    w = WordCount(readIn(filename))
    w.showTotal()
    w.showTop_low()
    w.showHistogram()
