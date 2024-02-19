# python3.11-mysql8.0.34-Student-Course-Selection-Information-Management-System
# python3.11-mysql8.0.34-学生选课信息管理系统

#### 1. 介绍
- python3.11-mysql8.0.34-Student-Course-Selection-Information-Management-System
- https://gitee.com/in5430km/2024_2_18_scdb
#### 2. 系统说明
该学生选课信息管理系统的主要功能是收集、存储、处理和查询学生选课数据，为学生、教师和学校管理人员提供一个便捷、高效的管理工具。其次，所含的数据库明确了其目标用户群体，主要包括学生、教师和学校管理层。学生可以通过系统修改个人信息、进行选课、查看课程信息、导出信息表等操作；教师可以查看课程信息、查看学生选课情况并进行相应的课程管理；学校管理层则可以通过系统进行数据的增删改查、统计和分析。本系统具备了数据的完整性和一致性，确保在各种情况下都能够正常运行，数据同步与准确。
###### 备注：由于编程时间比较仓促，仅用了两周时间从零构思数据库+两周时间从零学python+ttkbootstrap来编程此程序，在数据库设计方面，尚存在一些不足之处，如：班级应该用班级ID代替，而不是全称，用户数据库应该做到加密等。同时，用户数据对于程序来说，个人觉得应该做到【数据加密+数据解密程序应该作为接口被应用程序调用】这样比较好些，或许选用比这方法更好的。


#### 3. 开发环境
- 软件：PyCharm 2023.2.1
- 软件：DataGrip 2023.2.1
- MySQL8.0.34
![MySQL8.0.34](/readme/mysql.png)
- Python3.11.5
![Python3.11.5](/readme/python.png)
- Tkinter布局助手网址：https://www.pytk.net/
![Tkinter布局助手](/readme/Tkinter%E5%B8%83%E5%B1%80%E5%8A%A9%E6%89%8B.png)
###### 网址来源于他人作者所创作，其作者作品开源于：https://github.com/iamxcd/tkinter-helper
###### 备注：本作者利用这个Tkinter布局助手，解决了此程序的GUI布局问题，同时也使得程序编程更加便捷。故引用于此，以表感谢！
#### 4. 主要链接库
- 连接数据库 ：PyMySQL
- python的GUI库 ：ttkbootstrap + tkinter
- 生成表格文件 ：pandas
- 获取当前时钟 ：datetime
- 多线程调用 ：threading
#### 5. 功能与需求分析
![功能框图](/readme/%E5%88%86%E6%9E%90%E5%9B%BE.png)
#### 6. E-R图
![E-R图](/readme/E-R%E5%9B%BE.png)
#### 7. scdb数据库视图
##### 【主键】
- scdb.department.dno
- scdb.student.sno
- scdb.teacher.tno
- scdb.course.cno
- scdb.course_release_time.ctpye
##### 【外键】
- scdb.sct.cno              ---->    course.cno
- scdb.sct.sno              ---->    student.sno
- scdb.sct.tno              ---->    teacher.tno
- scdb.student.sdnoid       ---->    department.dno
- scdb.teacher.tdno         ---->    department.dno
- scdb.teachercourse.tecno  ---->    course.cno
- scdb.teachercourse.tno    ---->    teacher.tno
![scdb视图](/readme/scdb.jpg)
#### 8. users数据库视图
##### 【主键】
- users.t_admin.t_admin_account	
- users.t_teacher.t_teacher_tno
- users.t_student.t_student_sno
![users视图](/readme/users.jpg)
#### 9. 主要函数
1. 文件类
【file_fun.py】
- 读取文件数据：def batch_add(filename)
- 导出与保存文件：def save_file(filename, data, low, sel = False)
- 读取文件路径：def select_file()
2. 功能类
- 【page_login.py】
- 正则判断输入内容： **def validate_input(event)** 
- 设置新密码： **def button_set_password(self)** 
- 登录信息验证： **def login_tip(self)** 
- 【page_admin.py】
- 学生信息添加： **def button_student_add_enter(self)** 
- 学生信息数据导入与检错： **def excl_file_se(self)** 
- 学生信息修改： **def button_student_update_enter(self)** 
- 学生信息删除： **def button_student_del_enter(self)** 
- 教工信息添加： **def button_teacher_add_enter(self)** 
- 教工信息数据导入与检错： **def texcl_file_se(self)** 
- 教工信息修改： **def button_teacher_update_enter(self)** 
- 教工信息删除： **def button_teacher_del_enter(self)** 
- 院系信息添加： **def button_d_add_enter(self)** 
- 院系信息数据导入与检错： **def dexcl_file_selcet(self)** 
- 院系信息删除： **def button_dept_del(self)** 
- 课程信息添加： **def course_add(self)** 
- 课程信息数据导入与检错： **def button_c_batch_add(self)** 
- 课程信息修改： **def button_c_update(self)** 
- 课程信息删除： **def button_c_del(self)** 
- 【page_student.py】 
- 每秒刷新时间： **def update_clock(self)** 
- 选课时间实时： **def time_compare(self)** 
- 选课反馈： **def tree_select(self, event)** 
