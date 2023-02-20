import setuptools
setuptools.setup(
    name = "eaves",
    version = "0.0.1",
    author = "sxyz-eaves",
    author_email = "xxx@xxx.com",
    description = "一个基于 python 的轻量级比赛创建辅助工具。",
    long_description = "一个基于 python 的轻量级比赛创建辅助工具。",
    long_description_content_type="text/markdown",  # 模块详细介绍格式
    # url="https://github.com/sxyz-eaves/eaves",  # 模块github地址
    packages=setuptools.find_packages(),  # 自动找到项目中导入的模块
    package_data=[
        "eaves/SampleContest/**"
    ],
    # 模块相关的元数据
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GPL-3.0 License",
        "Operating System :: OS Independent",
    ],
    # 依赖模块
    install_requires=[
    ],
    python_requires='>=3',
)