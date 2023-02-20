# -*- coding: utf-8 -*-

# 这个程序是一个基础模块，供各个脚本调用。

import sys
import os
import shutil
import logging
import datetime
import __main__

log = logging.getLogger()


def init():
    FORMAT = "%(asctime)s %(thread)d %(message)s"
    DATEFMT = "[%Y-%m-%d %H:%M:%S]"
    logging.basicConfig(level=logging.INFO,
                        format=FORMAT,
                        datefmt=DATEFMT,
                        filename='eaves.log')
    log.setLevel(logging.DEBUG)
    # 使用 log 输出日志。
    log.info(
        u'脚本：%s, 工作目录：%s, 参数：[%s]。开始与 %s' % (
            __main__.__file__, os.getcwd(), str(
                sys.argv[1:]), str(datetime.datetime.now())
        )
    )


def unknownParameter(parameter):
    # 当发现未知参数时可调用此函数，并直接停止运行程序。
    log.error(u'发现未知参数 %s，程序停止运行。', parameter)
    log.error(
        u'请使用 \'eaves.%s -h\' 查询使用方式。' % (
            os.splitext(os.path.split(__main__.__file__)[1])[0]
            # 把文件名切出来
        )
    )
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
