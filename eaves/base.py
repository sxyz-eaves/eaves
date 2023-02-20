# -*- coding: utf-8 -*-

# 这个程序是一个基础模块，供各个脚本调用。

import sys
import os
import shutil
import logging
import datetime
import json
import __main__

log = logging.getLogger()
log.setLevel(logging.DEBUG)
# 使用 log 输出日志。


def get_tool_conf():
    def get_sys_env():
        return '$'.join([
            os.environ[key]
            for key in ['OS', 'SESSIONNAME', 'USERNAME', 'COMPUTERNAME', 'USERDOMAIN', 'USER', 'SHELL', 'SESSION']
            if key in os.environ
        ] + ['py%x' % sys.hexversion])
    global env_conf
    try:
        tool_conf = json.loads(
            open(os.path.join(__main__.__path__, 'conf.json'), 'rb').read().decode('utf-8'))
    except:
        tool_conf = {}
    sys_env = get_sys_env()
    if sys_env not in tool_conf:
        tool_conf[sys_env] = {}
    env_conf = tool_conf[sys_env]
    return tool_conf


def custom_conf():
    get_tool_conf()
    c = env_conf['file_log'] if 'file_log' in env_conf else {}
    file_log = logging.FileHandler(
        c['path'] if 'path' in c else 'tuack.log',
        mode=c['mode'] if 'mode' in c else 'a',
        encoding=c['encoding'] if 'encoding' in c else None
    )
    file_log.setLevel(c['level'] if 'level' in c else logging.INFO)
    file_log.setFormatter(logging.Formatter(
        c['format'] if 'format' in c else '[%(levelname).1s]%(filename)s:%(funcName)s:%(lineno)d:%(message)s'
    ))
    log.addHandler(file_log)

    c = env_conf['bash_log'] if 'bash_log' in env_conf else {}
    if 'encoding' in c:
        class MyStream(object):
            def __init__(self, stream):
                self.stream = stream

            def write(self, s):
                self.stream.buffer.write(s.encode(c['encoding']))
                self.stream.flush()

            def flush(self):
                self.stream.flush()
        bash_log = logging.StreamHandler(MyStream(sys.stdout))
    else:
        bash_log = logging.StreamHandler()
    bash_log.setLevel(c['level'] if 'level' in c else logging.DEBUG)
    bash_log.setFormatter(logging.Formatter(
        c['format'] if 'format' in c else '[%(levelname).1s]%(message)s'
    ))
    log.addHandler(bash_log)


def init():
    custom_conf()
    log.info(
        u'脚本：%s, 工作目录：%s, 参数：[%s]。开始与 %s' % (
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
