# coding:utf-8
'''
description:配置全局参数
'''
import time,os

# 获取项目路径
project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.split(os.path.realpath(__file__))[0]), '.'))
# 测试用例代码存放路径（用于构建suite,注意该文件夹下的文件都应该以test开头命名）
test_case_path = project_path+"\\src\\test_case"