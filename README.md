# python3.11-mysql8.0.34-Student-Course-Selection-Information-Management-System

#### 1. Introduction
- python3.11-mysql8.0.34-学生选课信息管理系统
- https://gitee.com/in5430km/2024_2_18_scdb
#### 2. System description
The main function of the student course selection information management system is to collect, store, process, and query student course selection data, providing a convenient and efficient management tool for students, teachers, and school administrators. Secondly, the included database clearly identifies its target user group, mainly including students, teachers, and school management. Students can modify their personal information, select courses, view course information, and export information tables through the system; Teachers can view course information, view student course selection status, and carry out corresponding course management; The school management can use the system to add, delete, modify, check, statistically analyze data. This system has the integrity and consistency of data, ensuring normal operation, data synchronization, and accuracy in all situations.
###### Note:Due to the rushed programming time, it only took two weeks to program this program from scratch with a zero concept database and two weeks to learn Python and ttkbootstrap from scratch. However, there are still some shortcomings in database design, such as using class ID instead of full name, and encrypting user databases. At the same time, for user data in the program, I personally think it is better to achieve [ data encryption+data decryption program should be called as an interface by the application program ], and perhaps choose a better method than this.


#### 3. Development environment
- software：PyCharm 2023.2.1
- software：DataGrip 2023.2.1
- MySQL8.0.34
![MySQL8.0.34](/readme/mysql.png)
- Python3.11.5
![Python3.11.5](/readme/python.png)
- Tkinter布局助手：https://www.pytk.net/
![Tkinter布局助手](/readme/Tkinter%E5%B8%83%E5%B1%80%E5%8A%A9%E6%89%8B.png)
###### The website is sourced from the author of (iamxcd Fresh Orange Duo), whose work is open source at:https://github.com/iamxcd/tkinter-helper
###### Note:The author utilized this Tkinter布局助手 to solve the GUI layout problem of this program, while also making programming more convenient. Therefore, it is used here to express gratitude!
#### 4. Partial external link libraries
- Connect to the database ：PyMySQL
- GUI library for Python ：ttkbootstrap + tkinter
- Generate Table Files ：pandas
- Get the current clock ：datetime
- Multi threaded calling ：threading
#### 5. Function and Requirements Analysis
![功能框图](/readme/%E5%88%86%E6%9E%90%E5%9B%BE.png)
#### 6. E-R
![E-R图](/readme/E-R%E5%9B%BE.png)
#### 7. Database view of scdb
##### 【Primary key】
- scdb.department.dno
- scdb.student.sno
- scdb.teacher.tno
- scdb.course.cno
- scdb.course_release_time.ctpye
##### 【Foreign key】
- scdb.sct.cno              ---->    course.cno
- scdb.sct.sno              ---->    student.sno
- scdb.sct.tno              ---->    teacher.tno
- scdb.student.sdnoid       ---->    department.dno
- scdb.teacher.tdno         ---->    department.dno
- scdb.teachercourse.tecno  ---->    course.cno
- scdb.teachercourse.tno    ---->    teacher.tno
![scdb视图](/readme/scdb.jpg)
#### 8. Database view of users
##### 【Primary key】
- users.t_admin.t_admin_account	
- users.t_teacher.t_teacher_tno
- users.t_student.t_student_sno
![users视图](/readme/users.jpg)
#### 9. Functions
1. File class
【file_fun.py】
- Read file data：def batch_add(filename)
- Export and Save Files：def save_file(filename, data, low, sel = False)
- Read file path：def select_file()
2. Functional class
- 【page_login.py】
- Regular judgment of input content： **def validate_input(event)** 
- Set a new password： **def button_set_password(self)** 
- Login information verification： **def login_tip(self)** 
- 【page_admin.py】
- Add student information： **def button_student_add_enter(self)** 
- Import and error detection of student information data： **def excl_file_se(self)** 
- Student information modification： **def button_student_update_enter(self)** 
- Delete student information： **def button_student_del_enter(self)** 
- Add teaching staff information： **def button_teacher_add_enter(self)** 
- Import and error detection of teaching staff information data： **def texcl_file_se(self)** 
- Modification of teaching staff information： **def button_teacher_update_enter(self)** 
- Delete teaching staff information： **def button_teacher_del_enter(self)** 
- Add departmental information： **def button_d_add_enter(self)** 
- Import and error detection of departmental information data： **def dexcl_file_selcet(self)** 
- Delete departmental information： **def button_dept_del(self)** 
- Add Course information： **def course_add(self)** 
- Import and error detection of course information data： **def button_c_batch_add(self)** 
- Modify course information： **def button_c_update(self)** 
- Delete course information： **def button_c_del(self)** 
- 【page_student.py】 
- Refresh time per second： **def update_clock(self)** 
- Real time course selection time： **def time_compare(self)** 
- Feedback course selection： **def tree_select(self, event)** 
