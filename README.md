# python3.11-mysql8.0.34-Student-Course-Selection-Information-Management-System

#### 1. Introduction
- python3.11-mysql8.0.34-学生选课信息管理系统
- https://gitee.com/in5430km/2024_2_18_scdb
#### 2. System Description
The main function of the student course selection information management system is to collect, store, process, and query student course selection data, providing a convenient and efficient management tool for students, teachers, and school administrators. Secondly, the included database clearly identifies its target user group, mainly including students, teachers, and school management. Students can modify their personal information, select courses, view course information, and export information tables through the system; Teachers can view course information, view student course selection status, and carry out corresponding course management; The school management can use the system to add, delete, modify, check, statistically analyze data. This system has the integrity and consistency of data, ensuring normal operation, data synchronization, and accuracy in all situations.
###### Note：Due to the rushed programming time, it only took two weeks to program this program from scratch with a zero concept database and two weeks to learn Python and ttkbootstrap from scratch. However, there are still some shortcomings in database design, such as using class ID instead of full name, and encrypting user databases. At the same time, for user data in the program, I personally think it is better to achieve [ data encryption+data decryption program should be called as an interface by the application program ], and perhaps choose a better method than this.


#### 3. Development Environment
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
