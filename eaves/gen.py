# -*- coding: utf-8 -*-

# 这个脚本用于生成比赛文件/题目文件

import sys
import os
import shutil
from . import base
from .base import log


def help():
    log.info(u'Usage')
    log.info(u'  help: 查询使用方法')
    log.info(u'  contest <name>: 创建一个比赛文件夹，文件夹名为 <name>')
    log.info(
        u'  problem <name1> <name2> ... : 创建一个若干题目文件夹，文件夹名和题目英文名称为 <name1>, <name2>, ...')


def genContest():
    if len(sys.argv) == 2:
        base.missingParameter()
    try:
        # 尝试创建文件
        shutil.copytree(os.path.split(__file__)[0] + '/' + 'SampleContest',
                        os.getcwd() + '/' + sys.argv[2])
    except FileExistsError:
        # 捕获 文件已经存在 错误
        log.error(u"该文件夹已经存在")
        # 这里会把子文件复制进去吗?


def genProblem():
    if len(sys.argv) == 2:
        base.missingParameter()
    for i in range(2, len(sys.argv)):
        dirPath = os.getcwd() + '\\' + sys.argv[i]
        try:
            # 尝试创建文件
            log.info(u"正在创建文件夹 " + dirPath)
            os.makedirs(dirPath)
            log.warn(u"未完成!将不会创建子文件")
        except FileExistsError:
            # 捕获 文件已经存在 错误
            log.error(u"该文件夹已经存在")


if __name__ == '__main__':
    base.init()
    if len(sys.argv) == 1:
        base.missingParameter()
    if sys.argv[1] == 'help':
        help()
    elif sys.argv[1] == 'contest':
        genContest()
    elif sys.argv[1] == 'problem':
        genProblem()
    else:
        base.unknownParameter(sys.argv[1])
