def sum_number(num):

    print(num)
    # 递归的出口， 当参数满足某个条件时,函数不再实行
    # 也叫出口
    if num ==1 :
        return

    # 函数自己调用自己

    sum_number(num - 1)

sum_number(3)