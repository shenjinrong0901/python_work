fname = input("请输入要打开的文件名称：")
fo = open(fname, "r")
txt = fo.read()
# 对全文txt进行处理
fo.close()