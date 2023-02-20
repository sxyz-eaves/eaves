# -*- coding: utf-8 -*-

# 这个程序是一个基础模块，供各个脚本调用。

import sys
import os
import logging
import datetime
import __main__


def settingLog():
    log.setLevel(logging.DEBUG)
    # 设置 log 等级

    file_log = logging.FileHandler(filename='eaves.log', mode='a')
    file_log.setLevel(logging.INFO)
    file_log.setFormatter(logging.Formatter(
        '[%(levelname).1s]%(filename)s:%(funcName)s:%(lineno)d:%(message)s'))
    # file_log 将日志输出到文件中
    log.addHandler(file_log)

    bash_log = logging.StreamHandler()
    bash_log.setLevel(logging.DEBUG)
    bash_log.setFormatter(logging.Formatter(
        '[%(levelname).1s]%(message)s'))
    # bash_log 将日志输出到命令行
    log.addHandler(bash_log)


def init():
    settingLog()
    log.info(
        u'开始程序\n   脚本：%s\n   工作目录：%s\n   参数：[%s]\n   开始于 %s' % (
            __main__.__file__, os.getcwd(), str(
                sys.argv[1:]), str(datetime.datetime.now())
        )
    )


def unknownParameter(parameter):
    # 当发现未知参数时可调用此函数，并直接停止运行程序。
    log.error(u'发现未知参数 %s，程序停止运行。', parameter)
    exit()


def missingParameter():
    # 发现缺少必要参数，直接停止运行程序。
    log.error(
        u'缺少必要参数，使用 \'eaves.%s -h\' 查询使用方式。' % (
            os.splitext(os.path.split(__main__.__file__)[1])[0]
            # 把文件名切出来
        )
    )
    exit()


log = logging.getLogger()
# 使用 log 输出日志。
