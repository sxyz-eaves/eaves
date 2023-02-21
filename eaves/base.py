# -*- coding: utf-8 -*-

# 这个程序是一个基础模块，供各个脚本调用。

import sys
import os
import logging
import datetime
import __main__

log = logging.getLogger()
# 使用 log 输出日志。


def settingLog():
	log.setLevel(logging.DEBUG)
	# 设置 log 等级
	file_log = logging.FileHandler(filename='eaves.log', mode='a')
	file_log.setLevel(logging.INFO)
	file_log.setFormatter(
		logging.Formatter(
			'[%(levelname).1s]' +
			'%(filename)s:' +
			'%(funcName)s:' +
			'%(lineno)d:' +
			'%(message)s')
	)
	# file_log 将日志输出到文件中
	log.addHandler(file_log)

	bash_log = logging.StreamHandler()
	bash_log.setLevel(logging.DEBUG)
	bash_log.setFormatter(logging.Formatter('[%(levelname).1s]%(message)s'))
	# bash_log 将日志输出到命令行
	log.addHandler(bash_log)


def init():
	settingLog()
	log.info(
		u'开始程序\n   脚本：%s\n   工作目录：%s\n   参数：%s\n   开始于 %s' % (
			__main__.__file__, os.getcwd(), str(
				sys.argv[1:]), str(datetime.datetime.now())
		)
	)
	log.info(u'版权声明')
	log.info(u'  版权所有 (C) 2023 SXYZ-EAVES 团队 保留一切权利 ')
	log.info(u'  此程序遵循 GPL-3.0 许可协议 ')
	log.info(u'  您可以遵照自由软件基金会出版的 GNU通用公共许可证条款 来修改和重新发布这一程序 ')
	log.info(u'  发布这一程序的目的是希望它有用 但它没有任何担保 甚至没有适合特定目的的隐含的担保 ')
	log.info(u'  更详细的情况请参阅 GNU通用公共许可证条款 ')


def unknownParameter(parameter):
	# 当发现未知参数时可调用此函数，并直接停止运行程序。
	log.error(
		u'发现未知参数 %s，程序停止运行。请使用 \'eaves.%s help\' 查询使用方式。' % (
			parameter,
			os.splitext(os.path.split(__main__.__file__)[1])[0]
			# 把文件名切出来
		)
	)
	exit()


def missingParameter():
	# 发现缺少必要参数，直接停止运行程序。
	log.error(
		u'缺少必要参数，程序停止运行。请使用 \'eaves.%s help\' 查询使用方式。' % (
			os.splitext(os.path.split(__main__.__file__)[1])[0]
			# 把文件名切出来
		)
	)
	exit()


def extraParameter(parameter):
	log.warn(u'发现多余参数 %s。' % (parameter))
