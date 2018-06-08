#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import datetime as dt

def printusage():
    print 'timedelta.py start end'
    print '    format : \'YYYY-MM-DD hh:mm:ss.SSS\' | \'[YYYY-MM-DD hh:mm:ss.SSS]\''

if __name__ == '__main__':
    argvs = sys.argv  # コマンドライン引数を格納したリストの取得
    argc = len(argvs) # 引数の個数

    if argc <> 3:
        printusage()
        exit(1)

    s_str = argvs[1].replace('[', '').replace(']', '')
    e_str = argvs[2].replace('[', '').replace(']', '')

    fmt = '%Y-%m-%d  %H:%M:%S.%f'

    s = dt.datetime.strptime(s_str, fmt)
    e = dt.datetime.strptime(e_str, fmt)
    d = e - s

    # print 'delta =', d
    print d.total_seconds(), 'sec'
    
    exit(0)
