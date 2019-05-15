# 解决IDE不能识别自己写的module:
# 1.打开File--> Setting—> 打开 Console下的Python Console，把选项（Add source roots to PYTHONPAT）点击勾选上
# 2.右键点击自己的工作空间文件夹，找到Mark Directory as 选择Source Root

from module1 import self_intro

self_intro("Nick")
