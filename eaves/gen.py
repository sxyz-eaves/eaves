# -*- coding: utf-8 -*-

# 这个脚本用于生成比赛文件/题目文件

import sys
import os
import shutil
import regex
from . import base
from .base import log


def help():
    license()
    log.info("Usage")
    log.info("  help: 显示版权声明及本帮助列表")
    log.info("  contest: 将当前文件夹设置为比赛文件夹并生成文件。")
    log.info(
        "  problem <name1> <name2> ... : 创建若干题目文件夹，文件夹名和题目英文名称为 <name1>, <name2>, ..."
    )
    log.info(
        "  translate <fileName> [outputName] : 转换md格式的题目为LaTeX格式，输入文件名为 <fileName>, 输出文件名为 [outputName], 不指定则默认为 <fileName>(去除后缀).tex"
    )


def genContest():
    if len(sys.argv) > 2:
        base.extraParameter(sys.argv[2:])
    shutil.copyfile(
        os.path.split(__file__)[0] + "/SampleContest/conf.yaml",
        os.getcwd() + "/conf.yaml",
    )
    log.info("创建 /conf.yaml")
    shutil.copyfile(
        os.path.split(__file__)[0] + "/SampleContest/precautions.md",
        os.getcwd() + "/precautions.md",
    )
    log.info("创建 /precautions.md")
    shutil.copyfile(
        os.path.split(__file__)[0] + "/SampleContest/.gitignore",
        os.getcwd() + "/.gitignore",
    )
    log.info("创建 /.gitignore")
    # 将 SampleContest 中的文件全都迁移过来。


def genProblem():
    if len(sys.argv) == 2:
        base.missingParameter()
    sample = os.path.split(__file__)[0] + "/SampleProblem"
    # 获取 SampleProblem 路径
    for problem in sys.argv[2:]:
        dirPath = os.getcwd() + "/" + problem
        # 获取当前路径
        if os.path.exists(dirPath):
            ifDeleteFolder = input("文件夹 %s 已经存在，你确定要继续并覆盖原文件吗[Y/n]？" % (problem))
            if ifDeleteFolder != "n" and ifDeleteFolder != "N":
                shutil.rmtree(dirPath)
        try:
            # 创建文件夹
            shutil.copytree(sample, dirPath)
            log.info("创建题目文件夹 %s" % (problem))
            problemConf = open(dirPath + "/conf.yaml", "w")
            problemConf.write("folder: problem\n")
            problemConf.write("title: 题目名称\n")
            problemConf.write("name: %s\n" % (problem))
            problemConf.write("data: {}\n")
            problemConf.write("memory limit: 512 MiB\n")
            problemConf.write("time limit: 1.0 s\n")
            problemConf.write("type: traditional\n")
            problemConf.write("checker: False\n")
            problemConf.close()
            # 写入 conf.yaml
            os.mkdir(dirPath + "/data")
            os.mkdir(dirPath + "/sample")
            os.mkdir(dirPath + "/tables")
            os.mkdir(dirPath + "/users")
        except FileExistsError:
            # 捕获 文件已经存在 错误
            log.error("文件夹 %s 创建失败。" % (problem))


def md2latex():
    if len(sys.argv) == 2:
        base.missingParameter()
    fileName = sys.argv[2]
    if len(sys.argv) == 3:
        outputName = fileName
        if outputName.rfind(".") != -1:
            suffix = outputName[outputName.rfind("."), len(outputName)]
            outputName.removesuffix(suffix)
        outputName = outputName + ".tex"
    else:
        outputName = sys.argv[3]
    log.info("读取输入文件 %s" % (fileName))
    filePath = os.getcwd() + "/" + fileName
    if os.path.exists(filePath) == False:
        log.error("文件 %s 不存在。" % (filePath))
    mdFile = open(filePath, "r")
    mdContent = mdFile.readlines()
    mdFile.close()
    log.info("文件读取完毕，开始转换。")
    texContent = []
    tabs = 0
    unorderedListCnt = [0]
    unorderedListTab = [0]
    orderedListCnt = [0]
    orderedListTab = [0]
    for mdLine, i in mdContent, range(len(mdContent)):
        if (int)((float)(i) / len(mdContent) * 100) % 10 == 0:
            log.info("正在处理第 %d / %d 行 " % (i) % len(mdContent))
        texLine = ""
        # 处理缩进
        # 匹配前缀空格
        prefixSpaceRegex = regex.compile("^( )*")
        prefixSpaceMatch = prefixSpaceRegex.match(mdLine)
        prefixSpaceResult = prefixSpaceMatch.capturesdict()
        # 转换为缩进值
        tabs = len(prefixSpaceResult[1])
        # 向该行添加空格
        for i in range(tabs):
            texLine = texLine + "\\ "
        # 处理列表
        # 处理无序列表
        # 匹配前缀列表符号
        prefixUnorderedListRegex = regex.compile("[-, \*, \+]")
        prefixUnorderedListMatch = prefixSpaceRegex.finditer(mdLine)
        for prefixUnorderedListMatchItem in prefixUnorderedListMatch:
            pos = prefixUnorderedListMatchItem.start()
            log.debug("Found Unordered List Item on Position %d" % pos)
            try:
                log.debug("Add ListCnt")
                find = unorderedListTab.index(pos)
                unorderedListTab = unorderedListTab[0, find]
                unorderedListCnt = unorderedListCnt[0, find]
                unorderedListCnt[find] = unorderedListCnt[find] + 1
            except ValueError:
                log.debug("New List")
                unorderedListTab.append(pos)
                unorderedListCnt.append(1)
        # 将该行附加到结果
        texContent.append(texLine)


if __name__ == "__main__":
    base.init()
    if len(sys.argv) == 1:
        base.missingParameter()
    if sys.argv[1] == "help":
        help()
    elif sys.argv[1] == "contest":
        genContest()
    elif sys.argv[1] == "problem":
        genProblem()
    elif sys.argv[1] == "translate":
        md2latex()
    else:
        base.unknownParameter(sys.argv[1])
