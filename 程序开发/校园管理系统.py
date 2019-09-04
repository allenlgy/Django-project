import time

class School(object):

    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.branches = {} # 下属分级
        self.__stuff_list = [] # 员工人数
        self.__bank_account_balance = 0 # 财务账号
        print('初始化校区[%s],地址:%s...'%(self.name,self.address))

        # print('%s 在 %s成立了!'%(self.name,self.address))

    def count_stuff_num(self):
        '''统计公司各分校园的员工人数'''
        total_stuff_num = len(self.__stuff_list)
        for i in self.branches:
            total_stuff_num += self.branches[i].count_stuff_num() # 统计分校人数

        print("[%s]总员工数量：%s"%(self.name,total_stuff_num))

        return total_stuff_num


    def pay_roll(self, salary):
        '''发工资'''
        pass

    def new_stuff_enrollment(self,stuff_obj):
        self.__stuff_list.append(stuff_obj)

    def count_total_branches(self):
        balance = self.__bank_account_balance
        for branch_name, branch_obj in self.branches.items():
            balance += branch_obj.__bank_account_balance

            print('Total balance:',balance)

    def open_course(self):
        pass

    def open_class(self):
        pass

    def show_balance(self):
        print("[%s]账户余额:%s"%(self.name,self.__bank_account_balance))

    def money_transfer_in(self,amount,from_obj,purpose):
        '''收钱'''
        self.__bank_account_balance += amount
        print("%s,校区【%s】收到【%s】转账【%s】，缴费原因【%s】..."%(
            time.strftime("%Y-%m-%d %H:%M:%S"),self.name,from_obj.name,amount,purpose
        ))


class BranchSchool(School):
    '''分学校'''
    def __init__(self, name, address, headquater_obj):
        super().__init__(name,address)
        self.headquater_obj = headquater_obj  # 总部对象

        self.headquater_obj.branches[name] = self # 把自己添加到总部的分学校列表

class Course():
    '''课程类'''
    def __init__(self, name, fee ,degree_requirement,):
        self.name = name
        self.fee = fee # 学费
        self.degree_requirement = degree_requirement  # 学历要求

class Class():
    '''课程类'''
    def __init__(self, course_obj,school_obj,class_num,start_date):
        self.class_num = class_num  # 班级编号
        self.start_date = start_date  # 开班日期
        self.course_obj = course_obj  # 开设课程
        self.school_obj = school_obj  # 所在校区
        self.stu_list = []  # 学员列表
        print("校区[%s]开设了【%s】课程第【%s】班，开班日期【%s】..."%(
            school_obj.name,course_obj.name,class_num,start_date
        ))

    def get_class_name(self):
        return "%s-%s-%s期"%(self.school_obj.name,self.course_obj.name,self.class_num)

    def create_teaching_record(self):
        pass

    def drop_out(self,stu_obj):
        '''退学'''
        self.stu_list.remove(stu_obj)
        print("学员[%s]从[%s]退学了"%(stu_obj.name, self.get_class_name()))


class Stuff(object):
    '''员工'''
    def __init__(self,name,age,position,salary,dept,school_obj,on_board_date):
        self.name = name
        self.age = age
        self.position = position  # 职位
        self.salary = salary
        self.dept = dept  # 部门
        self.school_obj = school_obj  # 所属校区
        self.on_board_date = on_board_date  # 入职日期
        print("校区[%s]的【%s】部门在【%s】入职一名新同事[%s]，职位是【%s】"%(
            school_obj.name, dept,on_board_date,name, position
        ))



class Student(object):

    def __init__(self, name, age, degree, class_obj, balance):
        self.name = name
        self.age= age
        self.degree = degree
        self.class_obj = class_obj  # 报名班级的对象
        self.balance = balance  # 这个学生有的钱

        self.class_obj.stu_list.append(self)  # 添加学生到这个班级

    def pay_tuition(self):
        '''交学费'''

        self.balance -= self.class_obj.course_obj.fee  # 交学费
        self.class_obj.school_obj.money_transfer_in(self.class_obj.course_obj.fee,self,"交[%s】学费"%self.class_obj.get_class_name())

    def __repr__(self):
        return "学生：%s，班级：%s"%(self.name, self.class_obj.get_class_name())
class Teacher(Stuff):
    '''讲师'''
    def teaching(self,class_obj,class_title):
        '''上课'''


# newschool = School('广州动画学院','随风村')
headquater = School("小猿圈北京总部","北京长安街1号")
bj1 = BranchSchool("小猿圈北京分校","北京昌平流沙河汇德商厦401",headquater)
sh1 = BranchSchool("小猿圈上海1分校","上海张江科技园",headquater)
sh2 = BranchSchool("小猿圈上海2分校","上海虹桥火车站",headquater)
sz1 = BranchSchool("深圳南山大学城分校","深圳南山大学城桃李创业园",headquater)

# 初始化员工
staff1 = Stuff("Alex",26,"CEO",60000,"总经办",headquater,"2015-05-22")
staff2 = Stuff("周小月",23,"HR",6000,"HR",headquater,"2017-03-12")
t1 = Teacher("Mjj",27,"前端开发讲师",30000,"教研部",bj1,"2018-02-26")
t2 = Teacher("银角大王",27,"Python讲师",45000,"教研部",sz1,"2016-07-14")
t3 = Teacher("苑日天",23,"Java讲师",40000,"教研部",sh1,"2018-07-14")

# 初始化课程
py_course = Course("Python开发",21800,"本科")
linux_course = Course("Linux云计算运维",19800,"专科")
go_course = Course("GO开发",9800,"本科")

# 初始化班级
class1 = Class(py_course,bj1,21,"2019-05-06")
class2 = Class(linux_course,sz1,4,"2019-04-16")
class3 = Class(go_course,sh1,11,"2019-06-21")
# 初始化学员
stu1 = Student("blackgirl",22,"本科",class1,30000)
stu2 = Student("李晓虎",23,"专科",class2,25000)
stu3 = Student("林爱根",26,"本科",class3,13000)
stu4 = Student("刘清蒸",21,"本科",class3,10000)
stu5 = Student("海底捞哥",21,"专科",class1,20000)
for i in (stu1,stu2,stu3,stu4):
    i.pay_tuition()
print(class3.stu_list)
bj1.show_balance()
sh1.show_balance()
sh2.show_balance()
sz1.show_balance()
headquater.count_total_branches()
headquater.count_stuff_num()
#print(headquater.branches)
# 退学
stu5.class_obj.drop_out(stu5)

