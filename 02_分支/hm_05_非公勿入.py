# 定义一个布尔型变量，判断是不是本公司员工
is_emploee = False

# 如果不是提示不许入内
# 在开发中，通常希望某个条件不满足时可以使用 not
#另外，如果需要拼接复杂的逻辑计算条件，也可以使用not
if not is_emploee:
    print('非本公司员工')