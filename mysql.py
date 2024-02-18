import pymysql
from pymysql import cursors

def mysql_connect_users():
    global db1
    db1 = pymysql.connect(
        host="localhost",
        user="root",
        password="1234567",
        database="users",
    )
    return db1
    pass

# ① 获取个人数据函数
# 座右铭，姓名，学号||密码，密钥
def student_info_update_mysql(user, password, key):
    global db1
    cursors = db1.cursor()

    value = (password, key, user)
    # noinspection SqlResolve
    sql = "UPDATE t_student SET t_student_password=%s, t_student_key=%s WHERE t_student_sno = %s"
    cursors.execute(sql, value)

    db1.commit()
    cursors.close()
    pass

# ② 获取个人数据函数
# 座右铭，姓名，学号||密码，密钥
def student_info_get_mysql(user):
    global db1
    cursors = db1.cursor()

    value = (user,)
    # noinspection SqlResolve
    sql = "SELECT t_student_password,t_student_key as skey FROM t_student WHERE t_student_sno = %s"
    cursors.execute(sql, value)
    data = cursors.fetchone()

    db1.commit()
    cursors.close()
    return data
    pass

def check_key(user=None, key=None, flag=None):
    global db1
    cursors = db1.cursor()
    value = (user, key)
    print(value)
    if flag == 2:
        # noinspection SqlNoDataSourceInspection
        sql = "SELECT t_admin_key as t_key FROM t_admin where t_admin_account = %s and t_admin_key = %s"
        cursors.execute(sql, value)
        pass
    if flag == 3:
        sql = "SELECT t_teacher_key as t_key FROM t_teacher where t_teacher_tno = %s and t_teacher_key=%s"
        cursors.execute(sql, value)
        pass
    if flag == 4:
        sql = "SELECT t_student_key as t_key FROM t_student where t_student_sno=%s and t_student_key=%s"
        cursors.execute(sql, value)
        pass
    result = cursors.fetchone()
    print(result)
    db1.commit()
    cursors.close()
    if result:
        return True
    else:
        return False
    pass

def user_pass_set(user, password, flag=5):
    global db1
    cursors = db1.cursor()
    value = (password, user)
    if flag == 2:
        sql = "UPDATE t_admin SET t_admin_password=%s where t_admin_account = %s"
        cursors.execute(sql, value)
        pass
    if flag == 3:
        sql = "UPDATE t_teacher SET t_teacher_password=%s  where t_teacher_tno = %s"
        cursors.execute(sql, value)
        pass
    if flag == 4:
        sql = "UPDATE t_student SET t_student_password=%s  where t_student_sno=%s"
        cursors.execute(sql, value)
        pass
    db1.commit()
    cursors.close()
    pass

# 显示数据：用户类型，用户账号，用户密码，用户密钥
# 传参：@u_tpye    @u_uno
def users_info(u_tpye, u_uno=None, select=True):
    global db1
    if u_tpye != "请选择":
        cursors = db1.cursor()
        if u_tpye == "管理员":
            if u_uno is not None:
                value = (u_uno,)
                sql = "SELECT '管理员' AS 用户类型,t.t_admin_account AS 用户账号,t.t_admin_password AS 用户密码,t.t_admin_key AS 用户密钥 FROM t_admin t WHERE t.t_admin_account like %s"
                cursors.execute(sql, value)
            else:
                sql = "SELECT '管理员' AS 用户类型,t.t_admin_account AS 用户账号,t.t_admin_password AS 用户密码,t.t_admin_key AS 用户密钥 FROM t_admin t"
                cursors.execute(sql)
        if u_tpye == "教工":
            if u_uno is not None:
                value = (u_uno,)
                sql = "SELECT '教工' AS 用户类型,t.t_teacher_tno AS 用户账号,t.t_teacher_password AS 用户密码,t.t_teacher_key AS 用户密钥 FROM t_teacher t WHERE t.t_teacher_tno like %s"
                cursors.execute(sql, value)
            else:
                sql = "SELECT '教工' AS 用户类型,t.t_teacher_tno AS 用户账号,t.t_teacher_password AS 用户密码,t.t_teacher_key AS 用户密钥 FROM t_teacher t"
                cursors.execute(sql)
        if u_tpye == "学生":
            if u_uno is not None:
                value = (u_uno,)
                sql = "SELECT '学生' AS 用户类型,t.t_student_sno AS 用户账号,t.t_student_password AS 用户密码,t.t_student_key AS 用户密钥 FROM t_student t WHERE t.t_student_sno like %s"
                cursors.execute(sql, value)
            else:
                sql = "SELECT '学生' AS 用户类型,t.t_student_sno AS 用户账号,t.t_student_password AS 用户密码,t.t_student_key AS 用户密钥 FROM t_student t"
                cursors.execute(sql)
        ulow = cursors.description
        datat = cursors.fetchall()
        db1.commit()
        cursors.close()
        if select is True:
            return datat
        else:
            print(ulow)
            return ulow
    pass

# 添加用户：@学生
# 参数：@学号sno @密码password @密钥key
def user_stduent_add(sno, password, key):
    global db1
    cursors = db1.cursor()
    value = (sno, password, key)
    sql = "INSERT INTO t_student (t_student_sno, t_student_password, t_student_key) VALUES (%s, %s, %s)"
    cursors.execute(sql, value)
    db1.commit()
    cursors.close()
    pass

# 删除用户：@学生
# 参数：@学号sno
def user_stduent_del(sno):
    global db1
    cursors = db1.cursor()
    value = (sno,)
    sql = "DELETE FROM t_student WHERE t_student_sno like %s"
    cursors.execute(sql, value)
    db1.commit()
    cursors.close()
    pass

# 添加用户：@教工
# 参数：@学号sno @密码password @密钥key
def user_teacher_add(tno, password, key):
    global db1
    cursors = db1.cursor()
    sql = "SELECT tno FROM scdb.teacher WHERE tno = %s"
    cursors.execute(sql, tno)

    data = cursors.fetchone()
    print(data)
    cursors.close()
    if data:
        cursors = db1.cursor()
        value = (tno, password, key)
        print(value)
        sql = "INSERT INTO t_teacher (t_teacher_tno, t_teacher_password, t_teacher_key) VALUES (%s, %s, %s)"
        cursors.execute(sql, value)
        db1.commit()
        cursors.close()
    pass

# 删除用户：@教工
# 参数：@教工号tno
def user_teacher_del(sno):
    global db1
    cursors = db1.cursor()
    value = (sno,)
    sql = "DELETE FROM t_teacher WHERE t_teacher_tno like %s"
    cursors.execute(sql, value)
    db1.commit()
    cursors.close()
    pass

# 修改数据：用户类型，用户账号，用户密码，用户密钥
# 传参：@u_tpye    @u_uno
def users_info_update(u_tpye, u_uno, u_password, u_key):
    global db1
    cursors = db1.cursor()
    value = (u_password, u_key, u_uno)
    if u_tpye == "管理员":
        sql = "UPDATE t_admin SET t_admin_password=%s,t_admin_key=%s where t_admin_account = %s"
        cursors.execute(sql, value)
    if u_tpye == "教工":
        sql = "UPDATE t_teacher SET t_teacher_password=%s,t_teacher_key=%s WHERE t_teacher_tno like %s"
        cursors.execute(sql, value)
    if u_tpye == "学生":
        sql = "UPDATE t_student SET t_student_password=%s,t_student_key=%s WHERE t_student_sno like %s"
        cursors.execute(sql, value)
    db1.commit()
    cursors.close()
    pass

def check_login(sno=None, password=None, u_set=True):
    global db1

    flag = 5
    if len(sno) is len('202324115001'):
        flag = 4
    elif len(sno) is len('202310002'):
        flag = 3
    if sno[:4] == 'root':
        flag = 2

    if db1 is None:
        return False
    try:
        with db1.cursor(pymysql.cursors.DictCursor) as cursor:
            if flag == 2:
                # noinspection SqlResolve
                sql = "SELECT t_admin_account as t_admin, t_admin_password as t_password FROM t_admin where t_admin_account=%s"
                cursor.execute(sql, sno)
                print("管理员！")
            elif flag == 3:
                # noinspection SqlResolve
                sql = "SELECT t_teacher_tno as t_tno, t_teacher_password as t_password FROM t_teacher where t_teacher_tno=%s"
                cursor.execute(sql, sno)
                print("教师！")
            elif flag == 4:
                # noinspection SqlResolve
                sql = "SELECT t_student_sno as t_sno, t_student_password as t_password FROM t_student where t_student_sno=%s"
                cursor.execute(sql, sno)
                print("学生！")
            else:
                print("登录异常！")
                return False
            result = cursor.fetchone()
            db1.commit()
            cursor.close()
            if u_set is True:
                if result:
                    # 账号存在
                    if password and result['t_password'] == password:
                        # 密码正确
                        return flag
                    else:
                        # 密码错误
                        return 1
                else:
                    # 账号不存在
                    return False
            else:
                if result is None:
                    flag = 6
                return flag
    except pymysql.Error as e:
        print(f"数据库查询出错：{e}")
        return False
    pass

def teacher_info_get_mysql(tno):
    global db1
    cursors = db1.cursor()
    value = (tno,)
    # noinspection SqlResolve
    sql = "SELECT t_teacher_password,t_teacher_key as skey FROM t_teacher WHERE t_teacher_tno = %s"
    cursors.execute(sql, value)
    data = cursors.fetchone()
    db1.commit()
    cursors.close()
    return data
    pass

def teacher_info_update_mysql(user, password, key):
    global db1
    cursors = db1.cursor()
    value = (password, key, user)
    # noinspection SqlResolve
    sql = "UPDATE t_teacher SET t_teacher_password=%s, t_teacher_key=%s WHERE t_teacher_tno = %s"
    cursors.execute(sql, value)
    db1.commit()
    cursors.close()
    pass

def mysql_close():
    mysql_connect_users().close()
    pass
