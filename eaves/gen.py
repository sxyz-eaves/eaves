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
	log.info(u'  contest: 将当前文件夹设置为比赛文件夹并生成文件。')
	log.info(
		u'  problem <name1> <name2> ... : 创建若干题目文件夹，文件夹名和题目英文名称为 <name1>, <name2>, ...')


def genContest():
	if len(sys.argv) > 2:
		base.extraParameter(sys.argv[2:])
	shutil.copyfile(os.path.split(__file__)[0] + '/SampleContest/conf.yaml', os.getcwd() + '/conf.yaml')
	log.info(u'创建 /conf.yaml')
	shutil.copyfile(os.path.split(__file__)[0] + '/SampleContest/precautions.md', os.getcwd() + '/precautions.md')
	log.info(u'创建 /precautions.md')
	shutil.copyfile(os.path.split(__file__)[0] + '/SampleContest/.gitignore', os.getcwd() + '/.gitignore')
	log.info(u'创建 /.gitignore')
	# 将 SampleContest 中的文件全都迁移过来。


def genProblem():
	if len(sys.argv) == 2:
		base.missingParameter()

	sample = os.path.split(__file__)[0] + '/SampleProblem'
	# 获取 SampleProblem 路径
	for problem in sys.argv[2:]:
		dirPath = os.getcwd() + '/' + problem
		# 获取当前路径
		if os.path.exists(dirPath):
			ifDeleteFolder = input('文件夹' + problem + '已经存在，是否删除原文件夹[Y/n]？')
			if ifDeleteFolder != 'n' and ifDeleteFolder != 'n':
				shutil.rmtree(dirPath)
		try:
			# 创建文件夹
			shutil.copytree(sample, dirPath)
			log.info(u'创建题目文件夹 %s' % (problem))
			problemConf = open(dirPath + '/conf.yaml', 'w')
			problemConf.write('folder: problem\n')
			problemConf.write('title: 题目名称\n')
			problemConf.write('name: %s\n' % (problem))
			problemConf.write('data: {}\n')
			problemConf.write('memory limit: 512 MiB\n')
			problemConf.write('time limit: 1.0 s\n')
			problemConf.write('type: traditional\n')
			problemConf.write('checker: False\n')
			problemConf.close()
			# 写入 conf.yaml
			os.mkdir(dirPath + '/data')
			os.mkdir(dirPath + '/sample')
			os.mkdir(dirPath + '/tables')
			os.mkdir(dirPath + '/users')
		except FileExistsError:
			# 捕获 文件已经存在 错误
			log.error(u'文件夹 %s 创建失败。' % (problem))


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
