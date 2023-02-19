# 这个脚本用于生成比赛文件/题目文件

import sys, os, shutil
from . import base
from .base import log

def genContest():
	if len(sys.argv) == 2:
		log.error(u'缺少必要参数')
		exit()
	shutil.copytree(os.path.split(__file__) + '/' + 'SampleContest', os.getcwd() + '/' + sys.argv[2])

def genProblem():
	log.error(u'还没开始写，咕咕咕～')

if __name__ == '__main__':
	base.init()
	if len(sys.argv) == 1:
		log.error(u'缺少必要参数')
		exit()
	if sys.argv[1] == 'contest':
		genContest()
	elif sys.argv[1] == 'problem':
		genProblem()
	else:
		base.unknownParameter(sys.argv[0])