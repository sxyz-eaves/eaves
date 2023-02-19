# 这个程序是一个基础模块，供各个脚本调用。

import sys, os, shutil
import logging
import datetime
import __main__

def init():
	log.info(
		u'脚本：%s, 工作目录：%s, 参数：[%s]。开始与 %s' % (
			__main__.__file__, os.getcwd(), str(sys.argv[1:]), str(datetime.datetime.now())
		)
	)

def unknownParameter(parameter):
	# 当发现未知参数时可调用此函数，并直接停止运行程序。
	log.error(u'发现未知参数 %s，程序停止运行。', parameter)
	exit()

log = logging.getLogger()
log.setLevel(logging.DEBUG)
# 使用 log 输出日志。