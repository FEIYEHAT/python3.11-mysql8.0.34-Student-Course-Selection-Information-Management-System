import datetime
import ttkbootstrap as ttk

import pymysql

def mysql_connect_csdb():
    global db2
    db2 = pymysql.connect(
        host="localhost",
        user="root",
        password="1234567",
        database="scdb",
    )
    return db2
    pass

# <个人信息>
# ① 更新数据函数
# 座右铭，姓名，学号||密码，密钥
def student_info_update_mysql2(mottor, user):
    global db2
    cursors = db2.cursor()

    value = (mottor, user)
    sql ="UPDATE student SET mottor=%s WHERE sno like %s"
    cursors.execute(sql, value)
    db2.commit()
    cursors.close()
    pass

# ② 获取个人数据函数
# 座右铭，姓名，学号||密码，密钥
def student_info_get_mysql2(user):
    global db2
    cursors = db2.cursor()

    value = (user,)
    sql = "SELECT s.sname, s.mottor, s.class, d.dname, s.ssex, s.sage FROM student s LEFT JOIN department d ON s.sdnoid = d.dno WHERE s.sno = %s;"
    cursors.execute(sql, value)
    data = cursors.fetchone()
    print(data)
    db2.commit()
    cursors.close()
    return data

    pass

# <班级信息>
# 更新数据函数
# 学号，姓名，班级
def class_info_data_get(sno):
    global db2
    cursors = db2.cursor()
    sql = "SELECT s.sno,s.sname,s.class FROM student s WHERE s.class like (SELECT s.class FROM student s WHERE s.sno like %s)"
    cursors.execute(sql, sno)
    data = cursors.fetchall()

    db2.commit()
    cursors.close()
    return data
    pass

# <课程信息>
# 显示个人选课信息
# 课程类型，课程名，上课时间，上课地点，授课教师
def course_info_show(sno, cset = True):
    global db2
    cursors = db2.cursor()
    value = (sno,)
    sql = "SELECT c.ctpye AS 课程类型, c.cname AS 课程名称, c.ctime AS 上课时间, c.caddress AS 上课地点, t.tname AS 授课教师 FROM course c INNER JOIN sct st ON c.cno = st.cno INNER JOIN teacher t ON t.tno = st.tno WHERE st.sno = %s"
    cursors.execute(sql, value)
    data = cursors.fetchall()
    c_low = cursors.description
    db2.commit()
    cursors.close()
    if cset:
        return data
    else:
        return c_low
    pass

# <课程成绩>
# 显示成绩信息
# 课程类型，课程名，学分，成绩
def course_grade_show(sno, g_set= True):
    global db2
    cursors = db2.cursor()
    sql = ("SELECT c.ctpye AS 课程类型,c.cname AS 课程,c.ccredit AS 学分,CASE WHEN sct.grade IS NULL THEN '' ELSE sct.grade END AS 成绩 FROM course c INNER JOIN sct ON c.cno = sct.cno WHERE sct.sno like %s")
    cursors.execute(sql, sno)
    data = cursors.fetchall()
    g_low = cursors.description
    db2.commit()
    cursors.close()
    if g_set:
        return data
    else:
        return g_low
    pass

# <选课信息>
# @课程类型
# @上课时间
def get_time():
    clock_var = ttk.StringVar()  # 创建一个StringVar对象来存储时间
    cdt = datetime.datetime.now()  # 获取当前日期和时间
    clock_var.set(cdt.strftime("%Y/%m/%d %H:%M"))  # 格式化日期和时间为年-月-日 时:分:秒
    sdt = clock_var.get()
    return sdt

def course_up_time_gets(ctpye):
    cursors = db2.cursor()
    datatt = None
    select = None
    if ctpye != "请选择":
        sql = "SELECT time_start, time_end FROM course_release_time WHERE ctpye = %s"
        cursors.execute(sql, ctpye)
        datatt = cursors.fetchone()
    if datatt:
        select = datatt[0] <= get_time() and get_time() <= datatt[1]
    if select is None:
        sql = "SELECT cselt_flag FROM course_release_time WHERE ctpye = %s"
        cursors.execute(sql, ctpye)
    else:
        sql = "UPDATE course_release_time SET cselt_flag ='0' WHERE ctpye = %s"
        cursors.execute(sql, ctpye)

    db2.commit()
    cursors.close()
    pass

def couse_data_info(ctpye, cday):
    cursors = db2.cursor()

    sql = "SELECT cselt_flag FROM course_release_time WHERE ctpye = %s"
    cursors.execute(sql, ctpye)
    result = cursors.fetchone()
    if result:
        # 查找发布
        if ctpye == "请选择":
            print("选择中")
            cursors.close()
            return None
        else:
            # sql
            if cday == "全部":
                # 参数：@<类型>
                sql = "SELECT c.ctpye,c.cno,c.cname,c.ctime,c.caddress,t.tname,c.ctonum,c.climnum FROM course c INNER JOIN teachercourse tc ON c.cno = tc.tecno INNER JOIN teacher t ON t.tno = tc.tno WHERE c.ctpye like %s"
                cursors.execute(sql, ctpye)
                pass
            else:
                # 参数：@<类型><星期>
                cday += "%"
                value = (ctpye, cday)
                sql = "SELECT c.ctpye,c.cno,c.cname,c.ctime,c.caddress,t.tname,c.ctonum,c.climnum FROM course c INNER JOIN teachercourse tc ON c.cno = tc.tecno INNER JOIN teacher t ON t.tno = tc.tno where (c.ctpye = %s && c.ctime like %s)"
                cursors.execute(sql, value)
        pass
    else:
        db2.commit()
        cursors.close()
    data = cursors.fetchall()
    db2.commit()
    cursors.close()
    return data
    pass

# <选课去重>
# 形参：@学号，@目标课程号
# 返回值：@课程号
def course_judgment(sno,cno):
    global db2
    value = (sno, cno)
    cursors = db2.cursor()
    sql = ("SELECT cno FROM sct WHERE sct.sno like %s and sct.cno like %s")
    cursors.execute(sql, value)
    data = cursors.fetchone()

    db2.commit()
    cursors.close()

    if data is not None:
        return False
    else:
        return True
    pass

# <课程的选择人数查询>
# 形参：@课程号
# 返回值：Ture False
def course_total_number(cno):
    global db2
    cursors = db2.cursor()

    value = (cno,)
    sql = "SELECT c.ctonum,c.climnum FROM course c WHERE c.cno like %s"
    cursors.execute(sql, value)
    data = cursors.fetchone()
    if data[0] > data[1]:
        return True
    else:
        return False
    pass

# <选课确认，更新课程表的选课人数信息>
# 学号，课程编号，教师工号，（成绩）defult
def couse_enter(sno, cno):
    global db2
    cursors = db2.cursor()
    value = (sno, cno)

    # 查找课程的授课教师工号
    sql = "SELECT tc.tno FROM teachercourse tc WHERE tc.tecno = %s"
    cursors.execute(sql, value[1])
    data = cursors.fetchone()
    print(data)

    value += data
    print(value)
    # 写入新数据行-->sct表
    sql = "INSERT INTO sct (sno, cno, tno) VALUES (%s, %s, %s)"
    cursors.execute(sql, value)

    # 更新选课人数字段course.climnum
    sql = "UPDATE course SET climnum=climnum+1 WHERE cno like %s"
    cursors.execute(sql, value[1])

    db2.commit()
    cursors.close()
    pass

# ①获取院系信息
# 返回data
def dept_data_get():
    global db2
    cursors = db2.cursor()
    sql = "SELECT d.dname AS 院系名称 FROM department d"
    cursors.execute(sql)
    data = cursors.fetchall()

    db2.commit()
    cursors.close()
    return data
    pass

# <管理端：T 学生修改>
# 查询学生，信息表
def st_find():
    global db2
    cursors = db2.cursor()
    sql = "SELECT s.sno AS 学号,s.sname AS 姓名,s.ssex AS 性别,s.sage AS 年龄,s.class AS 班级,d.dname AS 所属院系 FROM student s LEFT JOIN department d ON d.dno = s.sdnoid ORDER BY d.dname"
    cursors.execute(sql)
    data = cursors.fetchall()

    db2.commit()
    cursors.close()
    return data
    pass

# <管理端：T ①学生添加>
# 形参: 学号sno，姓名sname，性别ssex，年龄sage，班级sclass，所属院系sdept
def student_add(sno, sname, ssex, sage, sclass, sdept):
    global db2
    cursors = db2.cursor()
    if sage >=14 and sage<=24:
        # 查重
        sql = "SELECT sno FROM student WHERE sno like %s"
        cursors.execute(sql, sno)
        data = cursors.fetchone()
        print(data)
        if data:
            cursors.close()
            return False
        else:
            sql = "SELECT dno FROM department WHERE dname like %s"
            cursors.execute(sql, sdept)
            data = cursors.fetchone()

            if data:
                print(data[0])
                value = (sno, sname, ssex, sage, sclass, data[0])
                sql = "INSERT INTO student VALUES (%s, %s, %s, %s, %s, %s, NULL)"
                cursors.execute(sql, value)
            else:
                cursors.close()
                return False
    else:
        cursors.close()
        return False
    db2.commit()
    cursors.close()
    print("添加成功")
    return True
    pass

def student_info_add_low(select = False):
    global db2
    cursors = db2.cursor()
    sql = "SELECT s.sno AS 学号,s.sname AS 姓名,s.ssex AS 性别,s.sage AS 年龄,s.class AS 班级,d.dname AS 所属院系 FROM student s LEFT JOIN department d ON d.dno = s.sdnoid ORDER BY d.dname"
    cursors.execute(sql)
    slow = cursors.description
    data = cursors.fetchall()
    db2.commit()
    cursors.close()
    if select:
        return data
    else:
        return slow
    pass

# <管理端：T 学生管理>
# 修改学生信息
# 形参: sno, sname, ssex, sage, sclass, stdpt
def student_update(sno, sname, ssex, sage, sclass, stdpt):
    global db2
    cursors = db2.cursor()
    sql = "SELECT dno FROM department WHERE dname like %s"
    cursors.execute(sql, stdpt)
    data = cursors.fetchone()
    sdno = data[0]
    value = (sno, sname, ssex, sage, sclass, sdno, sno)
    sql = "UPDATE student SET sno = %s , sname = %s , ssex = %s , sage = %s , class = %s , sdnoid = %s WHERE sno like %s"
    cursors.execute(sql, value)
    db2.commit()
    cursors.close()
    print("修改成功！")
    pass

# <管理端：T 学生管理>
# 删除学生信息
# 形参: 学号sno
def student_info_del(sno):
    global db2
    cursors = db2.cursor()
    sql = "DELETE FROM student WHERE sno like %s"
    cursors.execute(sql, sno)
    db2.commit()
    cursors.close()
    pass

# <管理端：T 学生管理>
# 查询学生信息是否存在
# 形参: 学号sno
def student_find_sno(sno):
    global db2
    cursors = db2.cursor()
    sql = "SELECT s.sno AS 学号,s.sname AS 姓名,s.ssex AS 性别,s.sage AS 年龄,s.class AS 班级,d.dname AS 所属院系 FROM student s LEFT JOIN department d ON d.dno = s.sdnoid WHERE s.sno like %s ORDER BY d.dname"
    cursors.execute(sql, sno)
    data = cursors.fetchone()
    db2.commit()
    cursors.close()
    return data
    pass

# <管理端：T 学生管理>
# 查询学生信息是否存在
# 形参: 学生姓名sname
def student_find_name(sname):
    global db2
    cursors = db2.cursor()
    sql = "SELECT s.sno AS 学号,s.sname AS 姓名,s.ssex AS 性别,s.sage AS 年龄,s.class AS 班级,d.dname AS 所属院系 FROM student s LEFT JOIN department d ON d.dno = s.sdnoid WHERE s.sname like %s ORDER BY d.dname"
    cursors.execute(sql, sname)
    data = cursors.fetchall()
    db2.commit()
    cursors.close()
    if data:
        return data
    else:
        return False
    pass

# <管理端：T1 教工添加>
# 形参: 教工编号tno，教工名称tname，性别tsex，年龄tage，学历teb，职称tpt，所属院系名称dname
def teacher_add(tno, tname, tsex, tage, teb, tpt, dname):
    global db2
    cursors = db2.cursor()
    if 24 <= tage and tage <= 60 and (tsex == "男" or tsex == "女"):
        sql = "SELECT tno FROM teacher WHERE tno like %s"
        cursors.execute(sql, tno)
        data = cursors.fetchone()
        # 查重
        if data:
            cursors.close()
            return False
        else:
            sql = "SELECT dno FROM department WHERE dname like %s"
            cursors.execute(sql, dname)
            data = cursors.fetchone()
            if data:
                print(data)
                tdno = data[0]
                value = (tno, tname, tsex, tage, teb, tpt, tdno)
                sql = "INSERT INTO teacher VALUES (%s, %s, %s, %s, %s, %s, %s);"
                cursors.execute(sql, value)
            else:
                cursors.close()
                return False
    else:
        cursors.close()
        return False

    db2.commit()
    cursors.close()
    print("添加成功")
    return True
    pass

# <管理端：T2 教工修改>
# ②删除
# 形参: 教工编号tno
def teacher_info_del(tno):
    global db2
    cursors = db2.cursor()
    sql = "	DELETE FROM teacher WHERE tno like %s"
    cursors.execute(sql, tno)
    db2.commit()
    cursors.close()
    pass

# <管理端：T2 教工修改>
# ②-①删除-查询是否授课
# 形参: 教工编号tno
def teacher_course_find(tno):
    global db2
    cursors = db2.cursor()
    sql = "SELECT tc.tno,t.tname,c.cname FROM teachercourse tc LEFT JOIN course c ON tc.tecno = c.cno LEFT JOIN teacher t ON tc.tno = t.tno WHERE tc.tno = %s;"
    cursors.execute(sql, tno)
    data = cursors.fetchall()
    db2.commit()
    cursors.close()
    return data
    pass

# 更改课程的授课教师
def teacher_course_update(tno, course):
    global db2
    cursors = db2.cursor()
    print(course)
    sql = "SELECT tc.tecno FROM teachercourse tc WHERE tc.tecno = %s"
    cursors.execute(sql, course)
    data = cursors.fetchone()

    value = (tno, course)
    if data:
        sql = "UPDATE teachercourse tc SET tc.tno = %s WHERE tecno = %s"
        cursors.execute(sql, value)
    else:
        sql = "INSERT INTO teachercourse VALUES(%s,%s)"
        cursors.execute(sql, value)

    db2.commit()
    cursors.close()
    pass

def course_find(course):
    global db2
    cursors = db2.cursor()
    # 根据课程名查找课程ID
    sql = "SELECT cno FROM course WHERE cname = %s"
    cursors.execute(sql, course)
    tecno = cursors.fetchone()
    db2.commit()
    cursors.close()
    return tecno
    pass

# 查找课程的授课教师
def teacher_find_course(ctno):
    global db2
    cursors = db2.cursor()
    # 根据教工号查找课程ID
    sql = "SELECT tecno FROM teachercourse WHERE tno = %s"
    cursors.execute(sql, ctno)
    data = cursors.fetchall()
    db2.commit()
    cursors.close()
    return data
    pass
# <管理端：T2 教工修改>
# 查询教师信息是否存在
# 形参: 教工姓名tname

def teacher_find_name(tname):
    global db2
    cursors = db2.cursor()
    sql = "select t.tno AS 教工号,t.tname AS 姓名,t.tsex AS 性别,t.tage AS 年龄,t.teb AS 学历,t.tpt AS 职称,d.dname AS 所属院系 from teacher t INNER JOIN department d ON d.dno = t.tdno WHERE t.tname = %s"
    cursors.execute(sql, tname)
    data = cursors.fetchall()
    db2.commit()
    cursors.close()
    return data
    pass

# <管理端：T2 教工修改>
# 查询教师信息是否存在
# 形参: 教工编号tno
def teacher_find_one(tno):
    global db2
    cursors = db2.cursor()
    sql = "select t.tno AS 教工号,t.tname AS 姓名,t.tsex AS 性别,t.tage AS 年龄,t.teb AS 学历,t.tpt AS 职称,d.dname AS 所属院系 from teacher t INNER JOIN department d ON d.dno = t.tdno WHERE t.tno = %s"
    cursors.execute(sql, tno)
    data = cursors.fetchone()
    db2.commit()
    cursors.close()
    return data
    pass

# <管理端：T2 教工修改>
# 形参: 教工编号tno，教工名称tname，性别tsex，年龄tage，学历teb，职称tpt，所属院系名称tdname
def teacher_update(tno, tname, tsex, tage, teb, tpt, tdname):
    global db2
    cursors = db2.cursor()
    sql = "SELECT dno FROM department WHERE dname like %s"
    cursors.execute(sql, tdname)
    data = cursors.fetchone()
    tdno = data[0]
    value = (tno, tname, tsex, tage, teb, tpt, tdno, tno)
    sql = "UPDATE teacher SET tno = %s , tname = %s , tsex = %s , tage = %s , teb = %s , tpt = %s , tdno = %s WHERE tno like %s;"
    cursors.execute(sql, value)
    print("修改成功！")
    pass

# <管理端：T3 教工信息>
# 形参: 教工编号tno，教工名称tname，性别tsex，年龄tage，学历teb，职称tpt，所属院系名称tdname
def teacher_info_showall():
    global db2
    cursors = db2.cursor()
    sql = "SELECT t.tno AS 教工号,t.tname AS 姓名,t.tsex AS 性别,t.tage AS 年龄,t.teb AS 学历,t.tpt AS 职称,d.dname AS 所属院系 FROM teacher t LEFT JOIN department d ON d.dno = t.tdno ORDER BY d.dname"
    cursors.execute(sql)
    data = cursors.fetchall()

    db2.commit()
    cursors.close()
    return data
    pass

def teacher_info_add_low():
    global db2
    cursors = db2.cursor()
    sql = "SELECT t.tno AS 教工号,t.tname AS 姓名,t.tsex AS 性别,t.tage AS 年龄,t.teb AS 学历,t.tpt AS 职称,d.dname AS 所属院系 FROM teacher t LEFT JOIN department d ON d.dno = t.tdno ORDER BY d.dname"
    cursors.execute(sql)
    tlow = cursors.description
    db2.commit()
    cursors.close()
    return tlow
    pass

# <管理端：D，院系添加>
# 形参: 院系编号dno，院系名称dname，院系主任dmanager
def dept_add(dno, dname, dmanager):
    global db2
    cursors = db2.cursor()
    sql = "SELECT dno FROM department WHERE dno like %s"
    cursors.execute(sql, dno)
    data = cursors.fetchone()
    # 查重
    if data:
        cursors.close()
        return False
    else:
        dmanager = str(dmanager)
        if dmanager != 'nan' and len(dmanager):
            value = (dno, dname, dmanager)
            sql = "INSERT INTO department values(%s,%s,%s)"
            cursors.execute(sql, value)
        else:
            value = (dno, dname)
            sql = "INSERT INTO department(dno,dname) values(%s,%s)"
            cursors.execute(sql, value)

    db2.commit()
    cursors.close()
    print("添加成功")
    return True
    pass

def adept_info_add_low():
    global db2
    cursors = db2.cursor()
    sql = "SELECT dno AS 院系编号,dname AS 院系名称,dmanager AS 院系主任 FROM department"
    cursors.execute(sql)
    dlow = cursors.description
    db2.commit()
    cursors.close()
    return dlow
    pass

# <管理端：D2，院系修改>
# 形参: 院系编号dno，院系名称dname，院系主任dmanager
def adept_info_update(dname, dmanager, dno):
    global db2
    cursors = db2.cursor()
    value = (dname, dmanager, dno)
    sql = "UPDATE department SET dname=%s,dmanager=%s WHERE dno like %s"
    cursors.execute(sql, value)
    db2.commit()
    cursors.close()
    pass

def adept_info_del(dno):
    global db2
    cursors = db2.cursor()
    sql = "	DELETE FROM department WHERE dno like %s"
    cursors.execute(sql, dno)
    db2.commit()
    cursors.close()
    pass

# <管理端：D3，院系信息表>
# 返回值:@data : 院系编号dno，院系名称dname，院系主任dmanager，院系教工数dnum
def dept_info():
    global db2
    cursors = db2.cursor()
    sql = "SELECT d.dno AS 院系编号 ,d.dname AS 院系名称,d.dmanager AS 院系主任,COUNT(t.tdno) AS 院系教工总数 FROM department d LEFT JOIN teacher t ON t.tdno = d.dno GROUP BY d.dno"
    cursors.execute(sql)
    data = cursors.fetchall()
    # 获取file字段名
    file_low_set(cursors.description)
    db2.commit()
    cursors.close()
    return data
    pass

def file_low_set(lowr):
    global low
    low = lowr
    pass
def file_low_get():
    global low
    return low
    pass

# 课程添加
# c_type,c_id,name,credit,time,address
def mysql_course_add(c_type, c_id, name, credit, time, address, tonum = 0, limnum = 0, c_set = None):
    global db2
    cursors = db2.cursor()
    # 查重
    sql = "SELECT cno FROM course WHERE cno like %s"
    cursors.execute(sql, c_id)
    data = cursors.fetchone()
    print(data)
    if data:
        cursors.close()
        return False
    else:
        value = (c_type, c_id, name, credit, time, address, tonum, limnum)
        sql = "INSERT INTO course VALUES (%s, %s, %s, %s, %s, %s, %s, %s);"
        cursors.execute(sql, value)
        db2.commit()
        cursors.close()
        print("添加成功")
        return True
    pass

# 课程信息显示&获取列名
def course_info_low(select = False):
    global db2
    cursors = db2.cursor()
    sql = "SELECT c.ctpye AS 课程类型,c.cno AS 课程编号,c.cname AS 课程名,c.ccredit AS 学分,c.ctime AS 上课时间,c.caddress AS 上课地点,c.ctonum AS 限选人数,c.climnum AS 已选人数 FROM course c ORDER BY c.ctpye"
    cursors.execute(sql)
    slow = cursors.description
    data = cursors.fetchall()
    db2.commit()
    cursors.close()
    if select:
        return data
    else:
        return slow
    pass

def couse_info_select(ctype, cname = None):
    global db2
    cursors = db2.cursor()
    if ctype == "全部":
        if cname is not None:
            value = (cname,)
            sql = "SELECT c.ctpye AS 课程类型,c.cno AS 课程编号,c.cname AS 课程名,c.ccredit AS 学分,c.ctime AS 上课时间,c.caddress AS 上课地点,c.ctonum AS 限选人数,c.climnum AS 已选人数 FROM course c WHERE c.cname like %s ORDER BY c.ctpye"
            cursors.execute(sql, value)
        else:
            sql = "SELECT c.ctpye AS 课程类型,c.cno AS 课程编号,c.cname AS 课程名,c.ccredit AS 学分,c.ctime AS 上课时间,c.caddress AS 上课地点,c.ctonum AS 限选人数,c.climnum AS 已选人数 FROM course c ORDER BY c.ctpye"
            cursors.execute(sql)
    else:
        if cname is not None:
            value = (ctype, cname)
            sql = "SELECT c.ctpye AS 课程类型,c.cno AS 课程编号,c.cname AS 课程名,c.ccredit AS 学分,c.ctime AS 上课时间,c.caddress AS 上课地点,c.ctonum AS 限选人数,c.climnum AS 已选人数 FROM course c WHERE c.ctpye like %s AND c.cname like %s ORDER BY c.ctpye"
            cursors.execute(sql, value)
        else:
            value = (ctype,)
            sql = "SELECT c.ctpye AS 课程类型,c.cno AS 课程编号,c.cname AS 课程名,c.ccredit AS 学分,c.ctime AS 上课时间,c.caddress AS 上课地点,c.ctonum AS 限选人数,c.climnum AS 已选人数 FROM course c WHERE c.ctpye like %s ORDER BY c.ctpye"
            cursors.execute(sql, value)
        pass
    data = cursors.fetchall()
    db2.commit()
    cursors.close()
    return data
    pass

# 课程修改，更新
def course_update(c_type, c_id, name, credit, time, address, tonum = 0, limnum = 0):
    global db2
    cursors = db2.cursor()
    value = (c_type, name, credit, time, address, tonum, limnum, c_id)
    sql = "UPDATE course SET ctpye=%s,cname=%s,ccredit=%s,ctime=%s,caddress=%s,ctonum=%s,climnum=%s WHERE cno like %s;"
    cursors.execute(sql, value)
    db2.commit()
    cursors.close()
    print("修改成功")
    return True
    pass

# 课程删除
def course_del(c_id):
    global db2
    cursors = db2.cursor()
    value = (c_id,)
    sql = "DELETE FROM course WHERE cno like %s;"
    cursors.execute(sql, value)
    db2.commit()
    cursors.close()
    print("修改成功")
    return True
    pass

# 显示课程的授课教师情况
# 课程类型、课程名称、授课教师、教工编号
def teachercourse_info(select = False):
    global db2
    cursors = db2.cursor()
    sql = "SELECT c.ctpye AS 课程类型,c.cname AS 课程名称,CASE WHEN t.tname IS NULL THEN '无' ELSE t.tname END AS 授课教师,CASE WHEN tc.tno IS NULL THEN '无' ELSE tc.tno END AS 教工编号 FROM course c LEFT JOIN teachercourse tc ON c.cno = tc.tecno LEFT JOIN teacher t ON t.tno = tc.tno ORDER BY c.ctpye"
    cursors.execute(sql)
    sclow = cursors.description
    data = cursors.fetchall()
    db2.commit()
    cursors.close()
    if select:
        return data
    else:
        return sclow
    pass

def tc_info_select(ctype, cname=None):
    global db2
    cursors = db2.cursor()
    if ctype == "全部":
        if cname is not None:
            value = (cname,)
            sql = "SELECT c.ctpye AS 课程类型,c.cname AS 课程名称,CASE WHEN t.tname IS NULL THEN '无' ELSE t.tname END AS 授课教师,CASE WHEN tc.tno IS NULL THEN '无' ELSE tc.tno END AS 教工编号 FROM course c LEFT JOIN teachercourse tc ON c.cno = tc.tecno LEFT JOIN teacher t ON t.tno = tc.tno WHERE c.cname like %s ORDER BY c.ctpye"
            cursors.execute(sql, value)
        else:
            sql = "SELECT c.ctpye AS 课程类型,c.cname AS 课程名称,CASE WHEN t.tname IS NULL THEN '无' ELSE t.tname END AS 授课教师,CASE WHEN tc.tno IS NULL THEN '无' ELSE tc.tno END AS 教工编号 FROM course c LEFT JOIN teachercourse tc ON c.cno = tc.tecno LEFT JOIN teacher t ON t.tno = tc.tno ORDER BY c.ctpye"
            cursors.execute(sql)
    else:
        if cname is not None:
            value = (ctype, cname)
            sql = "SELECT c.ctpye AS 课程类型,c.cname AS 课程名称,CASE WHEN t.tname IS NULL THEN '无' ELSE t.tname END AS 授课教师,CASE WHEN tc.tno IS NULL THEN '无' ELSE tc.tno END AS 教工编号 FROM course c LEFT JOIN teachercourse tc ON c.cno = tc.tecno LEFT JOIN teacher t ON t.tno = tc.tno WHERE c.ctpye like %s AND c.cname like %s ORDER BY c.ctpye"
            cursors.execute(sql, value)
        else:
            value = (ctype,)
            sql = "SELECT c.ctpye AS 课程类型,c.cname AS 课程名称,CASE WHEN t.tname IS NULL THEN '无' ELSE t.tname END AS 授课教师,CASE WHEN tc.tno IS NULL THEN '无' ELSE tc.tno END AS 教工编号 FROM course c LEFT JOIN teachercourse tc ON c.cno = tc.tecno LEFT JOIN teacher t ON t.tno = tc.tno WHERE c.ctpye like %s ORDER BY c.ctpye"
            cursors.execute(sql, value)
        pass
    data = cursors.fetchall()
    db2.commit()
    cursors.close()
    return data
    pass

# 同类型课程的选课时间表
def course_start_info(select = True):
    global db2
    cursors = db2.cursor()
    sql = "SELECT crt.ctpye AS 课程类型,crt.time_start AS 选课时间,crt.time_end AS 选课结束,CASE WHEN crt.cselt_flag = '0' THEN '待发布' ELSE '已发布!' END AS 选课状态 FROM course_release_time crt ORDER BY crt.cselt_flag DESC"
    cursors.execute(sql)
    slow = cursors.description
    data = cursors.fetchall()
    db2.commit()
    cursors.close()
    if select:
        return data
    else:
        return slow
    pass

# 设置：选课时间的开始和结束
def course_time_set(start, end, tpye):
    global db2
    cursors = db2.cursor()
    value = (start, end, tpye)
    sql = "UPDATE course_release_time crt SET crt.time_start = %s, crt.time_end = %s WHERE crt.ctpye = %s"
    cursors.execute(sql, value)

    db2.commit()
    cursors.close()
    pass

# 发布课程
def course_flag_start(tpye):
    global db2
    cursors = db2.cursor()
    value = (tpye,)
    sql = "UPDATE course_release_time crt SET crt.cselt_flag = '1' WHERE crt.ctpye = %s"
    cursors.execute(sql, value)
    db2.commit()
    cursors.close()
    pass

# 选课时间结束
def course_flag_end(tpye):
    global db2
    cursors = db2.cursor()
    value = (tpye,)
    sql = "UPDATE course_release_time crt SET crt.cselt_flag = '0' WHERE crt.ctpye = %s"
    cursors.execute(sql, value)
    db2.commit()
    cursors.close()
    pass

def teacher_info_get_mysql2(tno):
    global db2
    cursors = db2.cursor()
    value = (tno,)
    sql = "SELECT t.tname, t.tno, t.tsex, t.tage, t.teb, t.tpt, d.dname FROM teacher t LEFT JOIN department d ON t.tdno = d.dno WHERE t.tno = %s"
    cursors.execute(sql, value)
    data = cursors.fetchone()
    print(data)
    db2.commit()
    cursors.close()
    return data
    pass

def Tc_info_data_mysql2(tpye, tno, tselect= True):
    global db2
    cursors = db2.cursor()

    if tpye == "全部":
        value = (tno,)
        sql = "SELECT c.ctpye AS 课程类型, c.cname AS 课程名称, c.ccredit AS 学分, c.ctime AS 上课时间, c.caddress AS 上课地点 FROM course c INNER JOIN sct st ON c.cno = st.cno INNER JOIN teacher t ON t.tno = st.tno WHERE t.tno = %s GROUP BY c.ctpye, c.cname, c.ccredit, c.ctime, c.caddress "
        cursors.execute(sql, value)
    else:
        value = (tpye, tno)
        sql = "SELECT c.ctpye AS 课程类型, c.cname AS 课程名称, c.ccredit AS 学分, c.ctime AS 上课时间, c.caddress AS 上课地点 FROM course c INNER JOIN sct st ON c.cno = st.cno INNER JOIN teacher t ON t.tno = st.tno WHERE c.ctpye = %s and t.tno = %s GROUP BY c.ctpye, c.cname, c.ccredit, c.ctime, c.caddress"
        cursors.execute(sql, value)

    data = cursors.fetchall()
    tlow = cursors.description

    print(data)
    db2.commit()
    cursors.close()
    if tselect is True:
        return data
    else:
        return tlow
    pass

def Tac_info_data_mysql2(tpye, tno):
    global db2
    cursors = db2.cursor()

    if tpye == "全部":
        value = (tno,)
        sql = "SELECT c.ctpye AS 课程类型, c.cname AS 课程名称 FROM course c INNER JOIN sct st ON c.cno = st.cno INNER JOIN teacher t ON t.tno = st.tno WHERE t.tno = %s GROUP BY c.ctpye, c.cname"
        cursors.execute(sql, value)
    else:
        value = (tpye, tno)
        sql = "SELECT c.ctpye AS 课程类型, c.cname AS 课程名称 FROM course c INNER JOIN sct st ON c.cno = st.cno INNER JOIN teacher t ON t.tno = st.tno WHERE c.ctpye = %s and t.tno = %s GROUP BY c.ctpye, c.cname"
        cursors.execute(sql, value)
    data = cursors.fetchall()

    print(data)
    db2.commit()
    cursors.close()
    return data
    pass

def Tac_info_grade_mysql2(cno, tno):
    global db2
    cursors = db2.cursor()
    if cno and tno:
        value = (cno, tno)
        sql = "SELECT sct.sno AS 学号,s.sname AS 姓名,s.class AS 班级,CASE WHEN sct.grade IS NULL THEN '' ELSE sct.grade END AS 成绩 FROM sct INNER JOIN student s ON s.sno = sct.sno WHERE sct.cno = %s and sct.tno =%s ORDER BY sct.sno"
        cursors.execute(sql, value)
        data = cursors.fetchall()
        print(data)
    else:
        return None
    db2.commit()
    cursors.close()
    return data
    pass

def find_course_cno_mysql2(tpye, cname):
    global db2
    cursors = db2.cursor()
    value = (tpye, cname)
    sql = "SELECT c.cno FROM course c WHERE c.ctpye = %s and c.cname =%s"
    cursors.execute(sql, value)
    data = cursors.fetchone()
    print(data)
    db2.commit()
    cursors.close()
    return data
    pass

def update_grade_cno_mysql2(grade, cno, sno):
    global db2
    cursors = db2.cursor()
    value = (grade, cno, sno)
    sql = "UPDATE sct SET grade = %s WHERE cno = %s and sno = %s"
    cursors.execute(sql, value)

    db2.commit()
    cursors.close()
    pass

def find_grade_cname_mysql2(cno):
    global db2
    cursors = db2.cursor()
    value = (cno, )
    sql = "SELECT cname FROM course WHERE cno = %s"
    cursors.execute(sql, value)
    data = cursors.fetchone()
    db2.commit()
    cursors.close()
    return data
    pass

def find_grade_ctpye_mysql2(cno):
    global db2
    cursors = db2.cursor()
    value = (cno,)
    sql = "SELECT ctpye FROM course WHERE cno = %s"
    cursors.execute(sql, value)
    data = cursors.fetchone()
    db2.commit()
    cursors.close()
    return data
    pass

def grade_excl_mysql2(cno, tno, select = True):
    global db2
    cursors = db2.cursor()
    value = (cno, tno)
    sql = "SELECT c.ctpye AS 课程类型, c.cname AS 课程名称,sct.sno AS 学号,s.sname AS 姓名,s.class AS 班级,CASE WHEN sct.grade IS NULL THEN '' ELSE sct.grade END AS 成绩 FROM sct INNER JOIN student s ON s.sno = sct.sno INNER JOIN course c ON c.cno = sct.cno WHERE sct.cno = %s and sct.tno =%s ORDER BY sct.sno;"
    cursors.execute(sql, value)
    data = cursors.fetchall()
    tlow = cursors.description
    db2.commit()
    cursors.close()
    if select:
        return data
    else:
        return tlow
    pass

def get_time_mysql():
    global db2
    cursors = db2.cursor()

    # noinspection SqlResolve
    sql = "select * from course_release_time"
    cursors.execute(sql)
    data = cursors.fetchall()
    # print(data)
    db2.commit()
    cursors.close()
    return data
    pass

def mysql2_close():
    mysql_connect_csdb().close()
    pass