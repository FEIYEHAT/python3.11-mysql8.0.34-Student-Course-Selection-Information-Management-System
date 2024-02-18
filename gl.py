import random
import string

set_value = 2
def set_sevalue(value):
    global set_value
    set_value = value
    pass
def get_sevalue():
    global set_value
    return set_value
    pass

# 记录用户登录的账号和密码
login_name = None
login_password = None
sign_update = False
st = None

# 记录课程号
course_tacno = None

def global_course_tacno_set(cno):
    global course_tacno
    course_tacno = cno
def global_course_tacno_get():
    global course_tacno
    return course_tacno

def get_user_password_flag(u_user, u_password, u_update = None):
    global login_name, login_password, sign_update
    login_name = u_user
    login_password = u_password
    # 更新右侧信息
    sign_update = u_update
    pass

def sign_set_update_course(param):
    global st
    st = param
    pass
def sign_set_update_course_get():
    global st
    g = st
    return g
    pass
def global_login_name_get():
    global login_name
    name = login_name
    return name
    pass

# 随机生成6位数：密码 密钥
def generate_random_number(length=6):
    # 生成一个包含大小写字母和数字的字符串
    characters = string.ascii_letters + string.digits
    # 随机选择指定长度的字符串
    random_number = ''.join(random.choice(characters) for i in range(length))
    return random_number
if __name__ == '__main__':
    data = generate_random_number()
    print(data)

