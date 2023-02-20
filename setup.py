from setuptools import setup, find_packages

setup(
    name = "eaves",
    version="0.0.2",
    authors = "Mine_King",
    author_email = "1395354790@qq.com",
    description = "一个基于 python 的轻量级比赛创建辅助工具。",
    url = "https://github.com/sxyz-eaves/eaves",
    packages = find_packages(),
    package_data = {
        'eaves': [
            'SampleContest/*.*'
        ]
    }
)