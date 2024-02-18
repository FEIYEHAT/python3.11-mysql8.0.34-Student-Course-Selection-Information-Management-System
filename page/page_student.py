import time
import datetime
import threading

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from mysql import student_info_update_mysql, student_info_get_mysql
from mysql2 import couse_data_info, couse_enter, student_info_update_mysql2, student_info_get_mysql2, \
    class_info_data_get, course_info_show, course_grade_show, course_judgment, course_total_number, get_time_mysql, \
    course_up_time_gets
from gl import global_login_name_get, sign_set_update_course, sign_set_update_course_get, get_user_password_flag

from file_fun import save_file

current_datetime = datetime.datetime.now()  # 获取当前日期和时间
time_com = False
Tdata = None
f_clear = [False,False,False,False,False]

btn1 = [True,True,True,True,True]
btn2 = [True,True,True,True,True]
course_vlist = {
    "必修课": 0,
    "选修课": 0,
    "体育课": 0,
    "文化课": 0,
    "通识课": 0
}
def student_info_update(m, u, p, k):
    student_info_update_mysql2(m, u)
    student_info_update_mysql(u, p, k)
    pass

def clear_treeview():
    global tktab
    for item in tktab.get_children():
        tktab.delete(item)

def print_course_data(ctype, cday):
    global tktab, course_vlist
    data = couse_data_info(ctype, cday)
    clear_treeview()
    for ct, value in course_vlist.items():
        if ct == ctype:
            if value == 1:
                for col in data:
                    tktab.insert("", "end", values=tuple(col))
    pass

def get_tday(value):
    global value_day
    value_day = value
    pass
def get_type(value):
    global value_type
    value_type = value
    pass

def on_week_selection(event):
    get_tday(event.widget.get())

    print_course_data(value_type, value_day)
def on_tpye_selection(event):
    get_type(event.widget.get())

    print_course_data(value_type, value_day)
    pass

class WinGUI(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__()
        self.pack(fill=BOTH, expand=YES)
        self.tk_frame_top = self.__tk_frame_top(self)
        # 右侧信息界面
        self.tk_frame_top_right = self.__tk_frame_top_right(self.tk_frame_top)
        self.tk_label_frame_introduce = self.__tk_label_frame_introduce(self.tk_frame_top_right)
        self.tk_label_image = self.__tk_label_image(self.tk_label_frame_introduce)
        self.tk_label_name = self.__tk_label_name(self.tk_label_frame_introduce)
        self.tk_label_name_txt = self.__tk_label_name_txt(self.tk_label_frame_introduce)
        self.tk_label_class = self.__tk_label_class(self.tk_label_frame_introduce)
        self.tk_label_class_txt = self.__tk_label_class_txt(self.tk_label_frame_introduce)
        self.tk_label_motto = self.__tk_label_motto(self.tk_label_frame_introduce)
        self.tk_label_motto_txt = self.__tk_label_motto_txt(self.tk_label_frame_introduce)
        self.tk_label_tem = self.__tk_label_tem(self.tk_label_frame_introduce)
        self.tk_label_tem_txt = self.__tk_label_tem_txt(self.tk_label_frame_introduce)
        self.tk_label_sno = self.__tk_label_sno(self.tk_label_frame_introduce)
        self.tk_label_sno_txt = self.__tk_label_sno_txt(self.tk_label_frame_introduce)

        # 个人选课界面
        self.current_datetime = current_datetime
        self.tk_frame_top_left = self.__tk_frame_top_left( self.tk_frame_top)
        self.tk_frame_top_line = self.__tk_frame_top_line( self.tk_frame_top_left)
        self.tk_frame_c_tpye = self.__tk_frame_c_tpye( self.tk_frame_top_line)
        self.tk_select_box_tpye_select = self.__tk_select_box_tpye_select( self.tk_frame_c_tpye)
        self.tk_label_course_tpye = self.__tk_label_course_tpye( self.tk_frame_c_tpye)
        self.tk_frame_c_time = self.__tk_frame_c_time( self.tk_frame_top_line)
        self.tk_label_time_txt = self.__tk_label_time_txt( self.tk_frame_c_time)

        self.tk_label_current_time_txt = self.__tk_label_current_time_txt(self.tk_frame_top_line)
        self.tk_select_box_time_select = self.__tk_select_box_time_select( self.tk_frame_c_time)
        self.tk_table_info_txt = self.__tk_table_info_txt( self.tk_frame_top_left)

        # 个人信息界面 N
        self.tk_frame_top_left_N = self.__tk_frame_top_left_N(self.tk_frame_top)
        self.tk_label_frame_info = self.__tk_label_frame_info(self.tk_frame_top_left_N)
        self.tk_label_info_n_t = self.__tk_label_info_n_t(self.tk_label_frame_info)
        self.tk_label_info_c_t = self.__tk_label_info_c_t(self.tk_label_frame_info)
        self.tk_label_info_u_t = self.__tk_label_info_u_t(self.tk_label_frame_info)
        self.tk_label_info_m_t = self.__tk_label_info_m_t(self.tk_label_frame_info)
        self.tk_label_info_p_t = self.__tk_label_info_p_t(self.tk_label_frame_info)
        self.tk_label_info_k_t = self.__tk_label_info_k_t(self.tk_label_frame_info)
        self.tk_input_info_m_in = self.__tk_input_info_m_in(self.tk_label_frame_info)
        self.tk_input_info_p_in = self.__tk_input_info_p_in(self.tk_label_frame_info)
        self.tk_input_info_k_in = self.__tk_input_info_k_in(self.tk_label_frame_info)
        self.tk_button_info_update = self.__tk_button_info_update(self.tk_label_frame_info)
        self.tk_label_info_n_txt = self.__tk_label_info_n_txt(self.tk_label_frame_info)
        self.tk_label_info_c_txt = self.__tk_label_info_c_txt(self.tk_label_frame_info)
        self.tk_label_info_u_txt = self.__tk_label_info_u_txt(self.tk_label_frame_info)
        self.tk_label_info_tem_t = self.__tk_label_info_tem_t(self.tk_label_frame_info)
        self.tk_label_info_tem_txt = self.__tk_label_info_tem_txt(self.tk_label_frame_info)
        self.tk_label_sex = self.__tk_label_sex( self.tk_label_frame_info)
        self.tk_label_sex_txt = self.__tk_label_sex_txt( self.tk_label_frame_info)
        self.tk_label_age = self.__tk_label_age( self.tk_label_frame_info)
        self.tk_label_age_txt = self.__tk_label_age_txt( self.tk_label_frame_info)
        # 班级信息 C
        self.tk_frame_top_left_C = self.__tk_frame_top_left_C( self.tk_frame_top)
        self.tk_table_class_info = self.__tk_table_class_info( self.tk_frame_top_left_C)
        # 课程信息 K
        self.tk_frame_top_left_K = self.__tk_frame_top_left_K( self.tk_frame_top)
        self.tk_table_course_info = self.__tk_table_course_info( self.tk_frame_top_left_K)
        self.tk_button_course_excl = self.__tk_button_course_excl( self.tk_frame_top_left_K)
        # 成绩信息
        self.tk_frame_top_left_G = self.__tk_frame_top_left_G( self.tk_frame_top)
        self.tk_table_grade_info = self.__tk_table_grade_info( self.tk_frame_top_left_G)
        self.tk_button_grade_excl = self.__tk_button_grade_excl( self.tk_frame_top_left_G)

        self.update_right_info()

        # 底部界面，信息记录界面
        self.tk_frame_button = self.__tk_frame_button(self)
        self.tk_text_button_txt = self.__tk_text_button_txt(self.tk_frame_button)
        pass
    def update_clock(self):
        while True:
            global clock_var,current_datetime
            current_datetime = datetime.datetime.now()  # 获取当前日期和时间
            clock_var.set(current_datetime.strftime("%Y/%m/%d %H:%M"))  # 格式化日期和时间为年-月-日 时:分:秒
            self.current_datetime = clock_var.get()
            clock_var.set(current_datetime.strftime("当前时间：%Y年%m月%d日 %H:%M:%S.f"))  # 格式化日期和时间为年-月-日 时:分:秒
            self.tk_label_current_time_txt.config(text=clock_var)
            self.time_compare()
            time.sleep(1)
    def time_compare(self):
        global time_com, Tdata, course_vlist, f_clear
        global value_type, value_day
        if time_com is True:
            # 在界面， 获取MySQL 事件时间包data，time_com = True    其他界面里，time_com = Flase
            i = 0
            Tdata = get_time_mysql()
            for data_item in Tdata:
                # 记录数据包的发布状态：0 发布，1 停止
                course_vlist[data_item[0]] = data_item[3]
                # 状态识别
                if data_item[3] == 1 and data_item[1] <= self.current_datetime and self.current_datetime <= data_item[2]:
                    # 处于发布状态，允许显示
                    if data_item[1] <= self.current_datetime and self.current_datetime <= data_item[2]:
                        if not f_clear[i]:
                            if btn1[i]:
                                btn1[i] = False
                                btn2[i] = True
                                f_clear[i] = True
                    else:
                        course_up_time_gets(value_type)
                else:
                    if not f_clear[i]:
                        if btn2[i]:
                            btn1[i] = True
                            btn2[i] = False
                            f_clear[i] = True
                if f_clear[i]:
                    f_clear[i] = False
                    print_course_data(value_type, value_day)
                i += 1
                # 刷新表格
                pass
            pass
        pass

    # 右侧信息，初始化更新
    def update_right_info(self):
        user_tno = global_login_name_get()
        print(user_tno)
        name_mottor_class_sdept_sex_age = student_info_get_mysql2(user_tno)
        # 第一
        lent = len(name_mottor_class_sdept_sex_age[1])
        str1 = name_mottor_class_sdept_sex_age[1]
        if lent > 8:
            lent /= 2
        mottor = str1[:int(lent)] + '\n' + str1[int(lent):]

        self.tk_label_motto_txt.configure(text=mottor)
        self.tk_label_tem_txt.configure(text=name_mottor_class_sdept_sex_age[3])
        self.tk_label_class_txt.configure(text=name_mottor_class_sdept_sex_age[2])
        self.tk_label_name_txt.configure(text=name_mottor_class_sdept_sex_age[0])
        self.tk_label_sno_txt.configure(text=user_tno)

        print("更新右侧个人信息成功！")
        pass

    def scrollbar_autohide(self,vbar, hbar, widget):
        """自动隐藏滚动条"""
        def show():
            if vbar: vbar.lift(widget)
            if hbar: hbar.lift(widget)
        def hide():
            if vbar: vbar.lower(widget)
            if hbar: hbar.lower(widget)
        hide()
        widget.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Enter>", lambda e: show())
        if vbar: vbar.bind("<Leave>", lambda e: hide())
        if hbar: hbar.bind("<Enter>", lambda e: show())
        if hbar: hbar.bind("<Leave>", lambda e: hide())
        widget.bind("<Leave>", lambda e: hide())

    def v_scrollbar(self,vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')
    def h_scrollbar(self,hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')
    def create_bar(self,master, widget,is_vbar,is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = ttk.Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = ttk.Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)
    def __tk_frame_top(self,parent):
        frame = ttk.Frame(parent,)
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.82)
        return frame

    def __tk_frame_top_right(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.77, rely=0.00, relwidth=0.23, relheight=0.98)
        return frame

    def __tk_label_frame_introduce(self, parent):
        frame = ttk.LabelFrame(parent, text="个人简介", )
        frame.place(relx=0.05, rely=0.02, relwidth=0.91, relheight=0.43)
        return frame

    def __tk_label_image(self, parent):
        label = ttk.Label(parent, anchor="center", )
        label.place(relx=0.55, rely=0.00, relwidth=0.40, relheight=0.43)
        return label

    def __tk_label_name(self, parent):
        label = ttk.Label(parent, text="姓 名：", anchor="center", )
        label.place(relx=0.00, rely=0.72, relwidth=0.25, relheight=0.13)
        return label

    def __tk_label_name_txt(self, parent):
        label = ttk.Label(parent, text="姓名名字", anchor="w", )
        label.place(relx=0.25, rely=0.72, relwidth=0.70, relheight=0.13)
        return label

    def __tk_label_class(self, parent):
        label = ttk.Label(parent, text="班 级：", anchor="center", )
        label.place(relx=0.00, rely=0.60, relwidth=0.25, relheight=0.13)
        return label

    def __tk_label_class_txt(self, parent):
        label = ttk.Label(parent, text="班级名称", anchor="w", )
        label.place(relx=0.25, rely=0.60, relwidth=0.70, relheight=0.13)
        return label

    def __tk_label_motto(self, parent):
        label = ttk.Label(parent, text="座右铭：", anchor="center", )
        label.place(relx=0.00, rely=0.04, relwidth=0.25, relheight=0.13)
        return label

    def __tk_label_motto_txt(self, parent):
        label = ttk.Label(parent, text="工欲善其事，\n必先利其器！", anchor="center", )
        label.place(relx=0.00, rely=0.17, relwidth=0.50, relheight=0.26)
        return label

    def __tk_label_tem(self, parent):
        label = ttk.Label(parent, text="院 系：", anchor="center", )
        label.place(relx=0.00, rely=0.47, relwidth=0.25, relheight=0.13)
        return label

    def __tk_label_tem_txt(self, parent):
        label = ttk.Label(parent, text="院系名称", anchor="w", )
        label.place(relx=0.25, rely=0.47, relwidth=0.70, relheight=0.13)
        return label

    def __tk_label_sno(self, parent):
        label = ttk.Label(parent, text="学 号：", anchor="center", )
        label.place(relx=0.00, rely=0.85, relwidth=0.25, relheight=0.13)
        return label

    def __tk_label_sno_txt(self, parent):
        label = ttk.Label(parent, text="学号号码", anchor="w", )
        label.place(relx=0.25, rely=0.85, relwidth=0.70, relheight=0.13)
        return label
    def __tk_frame_top_left(self,parent):
        frame = ttk.Frame(parent,)
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame
    def __tk_frame_top_line(self,parent):
        frame = ttk.Frame(parent,)
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.07)
        return frame
    def __tk_frame_c_tpye(self,parent):
        frame = ttk.Frame(parent,)
        frame.place(relx=0.01, rely=0.25, relwidth=0.22, relheight=0.75)
        return frame
    def __tk_select_box_tpye_select(self,parent):
        global cb_type
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择","必修课","选修课","通识课","体育课","文化课")
        cb.bind("<<ComboboxSelected>>", on_tpye_selection)
        cb.place(relx=0.41, rely=0.10, relwidth=0.59, relheight=0.80)
        cb_type = cb
        #
        return cb
    def __tk_label_course_tpye(self,parent):
        label = ttk.Label(parent,text="课程类型：",anchor="center", )
        label.place(relx=0.00, rely=0.00, relwidth=0.41, relheight=1.00)
        return label
    def __tk_frame_c_time(self,parent):
        frame = ttk.Frame(parent,)
        frame.place(relx=0.24, rely=0.25, relwidth=0.22, relheight=0.75)
        return frame
    def __tk_label_time_txt(self,parent):
        label = ttk.Label(parent,text="上课时间：",anchor="center", )
        label.place(relx=0.00, rely=0.00, relwidth=0.41, relheight=1.00)
        return label
    def __tk_label_current_time_txt(self, parent):
        label = ttk.Label(parent, textvariable=clock_var, anchor="w", foreground="yellow")
        label.place(relx=0.74, rely=0.1, relwidth=0.3, relheight=1.00)
        return label
    def __tk_select_box_time_select(self,parent):
        global cb_time
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("全部","星期一","星期二","星期三","星期四","星期五","星期六","星期日")
        cb.bind("<<ComboboxSelected>>", on_week_selection)
        cb.place(relx=0.41, rely=0.10, relwidth=0.59, relheight=0.80)

        cb_time = cb
        return cb
    def __tk_table_info_txt(self,parent):
        # 表头字段 表头宽度
        global tktab
        columns = {"课程类型": 66, "课程编号": 0, "课程名": 147, "上课时间": 200, "上课地点": 126, "授课教师": 72, "限选": 57,
                   "已选": 57, }
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns),)
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='w')
            tk_table.column(text, anchor='w', width=width, stretch=True,)  # stretch 不自动拉伸
        # 隐藏 课程编号的数据
        tk_table.column(1, width=0, stretch=False)
        tk_table.bind('<<TreeviewSelect>>', self.tree_select)

        tk_table.place(relx=0.00, rely=0.07, relwidth=1.00, relheight=0.93)
        self.create_bar(parent, tk_table,True, False,1, 39, 738,510,740,550)

        tktab = tk_table
        return tk_table
    def __tk_frame_button(self,parent):
        frame = ttk.Frame(parent,)
        frame.place(relx=0.00, rely=0.82, relwidth=1.00, relheight=0.18)
        return frame
    def __tk_text_button_txt(self,parent):
        text = ttk.Text(parent)
        text.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=1.00)
        self.create_bar(parent, text,True, True, 0, 0, 960,120,960,120)
        return text

    # 选课点击，反馈操作
    def tree_select(self, event):
        user_tno = global_login_name_get()
        selection = event.widget.selection()
        if selection:
            # 获取选中的行索引
            index = selection[0]
            # 获取行中的数据
            course = event.widget.set(index)
            print(f'{course}')
            course_name = course['课程名']
            result = messagebox.askokcancel("选课提示", f'当前选课：{course_name}\n是否确认选课？')
            if result:
                # 查询学生是否已经选了该门课程，如果已选，则弹窗：请勿重选已选课程！
                if course_judgment(user_tno,course['课程编号']) is False:
                    messagebox.showinfo("选课提示", f'你已选了当前课程：{course_name}\n请勿重选已选课程！')
                else:
                    # 判断课程的人数是否已满人
                    if course_total_number(course['课程编号']) is False:
                        messagebox.showinfo("选课提示", f'你当前选的课程 {course_name} 已满人！\n请重选其他课程！')
                    else:
                        # 选课确定，同时更新课程表已选人数字段 @climnum 的信息
                        couse_enter(user_tno, course['课程编号'])
                        print(course['课程编号'])
                        print("选课成功")
                        # 更新选课显示内容
                        sign_set_update_course(True)
                        if sign_set_update_course_get() is True:
                            print(sign_set_update_course_get())
                            sign_set_update_course(False)

                            print_course_data(value_type, value_day)
                            messagebox.showinfo("信息提示", "选课成功！")
                            pass
            else:
                print("选课取消")
        event.widget.selection_clear()
        pass

    # 个人信息
    def __tk_frame_top_left_N(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_label_frame_info(self, parent):
        frame = ttk.LabelFrame(parent, text="个人信息", )
        frame.place(relx=0.03, rely=0.02, relwidth=0.86, relheight=0.75)
        return frame

    def __tk_label_info_n_t(self, parent):
        label = ttk.Label(parent, text="姓 名：", anchor="center", )
        label.place(relx=0.09, rely=0.02, relwidth=0.08, relheight=0.07)
        return label

    def __tk_label_info_c_t(self, parent):
        label = ttk.Label(parent, text="班 级：", anchor="center", )
        label.place(relx=0.09, rely=0.22, relwidth=0.08, relheight=0.07)
        return label

    def __tk_label_info_u_t(self, parent):
        label = ttk.Label(parent, text="学 号：", anchor="center", )
        label.place(relx=0.09, rely=0.12, relwidth=0.08, relheight=0.07)
        return label

    def __tk_label_info_m_t(self, parent):
        label = ttk.Label(parent, text="座右铭：", anchor="center", )
        label.place(relx=0.09, rely=0.41, relwidth=0.08, relheight=0.07)
        return label

    def __tk_label_info_p_t(self, parent):
        label = ttk.Label(parent, text="密 码：", anchor="center", )
        label.place(relx=0.09, rely=0.51, relwidth=0.08, relheight=0.07)
        return label

    def __tk_label_info_k_t(self, parent):
        label = ttk.Label(parent, text="密 钥：", anchor="center", )
        label.place(relx=0.09, rely=0.61, relwidth=0.08, relheight=0.07)
        return label

    def __tk_input_info_m_in(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.17, rely=0.41, relwidth=0.33, relheight=0.07)
        return ipt

    def __tk_input_info_p_in(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.17, rely=0.51, relwidth=0.33, relheight=0.07)
        return ipt

    def __tk_input_info_k_in(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.17, rely=0.61, relwidth=0.33, relheight=0.07)
        return ipt

    def __tk_button_info_update(self, parent):
        btn = ttk.Button(parent, text="修改", takefocus=False, command=self.button_update_set)
        btn.place(relx=0.42, rely=0.83, relwidth=0.08, relheight=0.07)
        return btn

    def __tk_label_info_n_txt(self, parent):
        label = ttk.Label(parent, anchor="w", )
        label.place(relx=0.17, rely=0.02, relwidth=0.33, relheight=0.07)
        return label

    def __tk_label_info_c_txt(self, parent):
        label = ttk.Label(parent, text="标签", anchor="w", )
        label.place(relx=0.17, rely=0.22, relwidth=0.33, relheight=0.07)
        return label

    def __tk_label_info_u_txt(self, parent):
        label = ttk.Label(parent, text="标签", anchor="w", )
        label.place(relx=0.17, rely=0.12, relwidth=0.33, relheight=0.07)
        return label

    def __tk_label_info_tem_t(self, parent):
        label = ttk.Label(parent, text="院 系：", anchor="center", )
        label.place(relx=0.09, rely=0.32, relwidth=0.08, relheight=0.07)
        return label

    def __tk_label_info_tem_txt(self, parent):
        label = ttk.Label(parent, text="标签", anchor="w", )
        label.place(relx=0.17, rely=0.32, relwidth=0.33, relheight=0.07)
        return label
    def __tk_label_sex(self,parent):
        label = ttk.Label(parent,text="性 别：",anchor="center", )
        label.place(relx=0.58, rely=0.02, relwidth=0.08, relheight=0.07)
        return label
    def __tk_label_sex_txt(self,parent):
        label = ttk.Label(parent,text="2001年01月01日",anchor="w", )
        label.place(relx=0.66, rely=0.02, relwidth=0.16, relheight=0.07)
        return label
    def __tk_label_age(self,parent):
        label = ttk.Label(parent,text="年 龄：",anchor="center", )
        label.place(relx=0.58, rely=0.12, relwidth=0.08, relheight=0.07)
        return label
    def __tk_label_age_txt(self,parent):
        label = ttk.Label(parent,text="24岁",anchor="w", )
        label.place(relx=0.66, rely=0.12, relwidth=0.16, relheight=0.07)
        return label

    # 班级信息
    def __tk_frame_top_left_C(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_table_class_info(self, parent):
        # 表头字段 表头宽度
        columns = {"学号": 255, "姓名": 220, "班级": 255}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.01, rely=0.01, relwidth=0.988, relheight=0.985)
        self.create_bar(parent, tk_table, True, False, 8, 7, 730, 540, 740, 552)
        return tk_table

    # 课程信息
    def __tk_frame_top_left_K(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_table_course_info(self, parent):
        # 表头字段 表头宽度
        columns = {"课程类型": 80, "课程名": 145, "上课时间": 200, "上课地点": 155,
                   "授课教师": 145, }
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='w')
            tk_table.column(text, anchor='w', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.01, rely=0.0495, relwidth=0.99, relheight=0.95)
        self.create_bar(parent, tk_table, True, False, 8, 28, 733, 521, 742, 550)
        return tk_table

    # 学生的选课课程信息
    def __tk_button_course_excl(self, parent):
        btn = ttk.Button(parent, text="导出表格", takefocus=False, command=self.button_course_excl)
        btn.place(relx=0.92, rely=0.00, relwidth=0.08, relheight=0.04)
        return btn
    def button_course_excl(self):
        user_n = self.tk_label_sno_txt.cget("text")
        user_n += self.tk_label_name_txt.cget("text")
        user_n += '_课程表'
        save_file(user_n, course_info_show(self.tk_label_sno_txt.cget("text"), True), course_info_show(self.tk_label_sno_txt.cget("text"), False))
        pass

    # 成绩信息
    def __tk_frame_top_left_G(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_table_grade_info(self, parent):
        # 表头字段 表头宽度
        columns = {"课程类型": 170, "课程名": 205, "学分": 175, "成绩": 180}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.01, rely=0.0495, relwidth=0.99, relheight=0.95)
        self.create_bar(parent, tk_table, True, False, 8, 28, 731, 521, 740, 550)
        return tk_table

    def __tk_button_grade_excl(self, parent):
        btn = ttk.Button(parent, text="导出表格", takefocus=False, command=self.button_grade_excl)
        btn.place(relx=0.92, rely=0.00, relwidth=0.08, relheight=0.04)
        return btn
    def button_grade_excl(self):
        user_n = self.tk_label_sno_txt.cget("text")
        user_n += self.tk_label_name_txt.cget("text")
        user_n += '_成绩表'
        save_file(user_n, course_grade_show(self.tk_label_sno_txt.cget("text"), True),
                  course_grade_show(self.tk_label_sno_txt.cget("text"), False))
        pass

    def button_update_set(self):
        if len(self.tk_input_info_m_in.get()) and len(self.tk_input_info_p_in.get()) and len(self.tk_input_info_k_in.get()):
            result = messagebox.askokcancel("提示", "是否确认修改？")
            if result:
                # 调用sql
                # 座右铭，学号||密码，密钥
                student_info_update(self.tk_input_info_m_in.get(), self.tk_label_info_u_txt.cget("text"),
                                    self.tk_input_info_p_in.get(), self.tk_input_info_k_in.get())
                # 更新右侧个人信息
                self.update_right_info()
                messagebox.showinfo("提示", "信息修改成功！")
        else:
            messagebox.showerror("提示", "填写内容不能为空！")
        pass
    def button_enter_set(self):
        global set
        if set is True:
            messagebox.showinfo("提示","信息修改成功！")
            print(set)
            set = False
            # 调用sql
            # 座右铭，学号||密码，密钥
            student_info_update(self.tk_input_info_m_in.get(), self.tk_label_info_u_txt.cget("text"),
                                self.tk_input_info_p_in.get(), self.tk_input_info_k_in.get())
            # 更新右侧个人信息
            self.update_right_info()
        else:
            messagebox.showinfo("提示", "请先按修改键进行信息修改！")
        pass



class StudentMenu(WinGUI):
    def __init__(self, master, login_name, login_password, **kwargs):
        get_user_password_flag(login_name, login_password)
        global clock_var, Tdata
        Tdata = get_time_mysql()
        clock_var = ttk.StringVar()  # 创建一个StringVar对象来存储时间
        self.thread1 = threading.Thread(target=self.update_clock)
        self.thread1.daemon = True
        self.thread1.start()

        super().__init__(master, **kwargs)
        self.__event_bind()
        # self.config(menu=self.create_menu())
    def create_menu(self):
        menu = ttk.Menu(self,tearoff=False)
        menu.add_cascade(label="选课报名(S)",menu=self.menu_selcourse(menu))
        menu.add_cascade(label="信息查询(I)",menu=self.menu_info(menu))
        menu.add_cascade(label="帮助(H)",menu=self.menu_help(menu))
        return menu
    def menu_selcourse(self, parent):
        menu = ttk.Menu(parent, tearoff=False)
        menu.add_command(label="个人选课(C)", command=self.course_selection)
        return menu
    def menu_info(self, parent):
        menu = ttk.Menu(parent, tearoff=False)
        menu.add_command(label="个人信息(N)", command=self.students_info)
        menu.add_command(label="班级信息(M)", command=self.class_info)
        menu.add_command(label="课程信息(K)", command=self.course_info)
        menu.add_command(label="课程成绩(G)", command=self.course_grade)

        return menu
    def menu_help(self, parent):
        menu = ttk.Menu(parent, tearoff=False)
        menu.add_command(label="关于(A)", command=self.app_read)
        menu.add_command(label="检查更新(G)", command=self.app_update)
        menu.add_command(label="退出(E)", command=self.app_destroy)
        return menu
    def course_selection(self):
        # 在界面， 获取MySQL 事件时间包data，time_com = True    其他界面里，time_com = Flase
        global time_com, Tdata

        print(Tdata)
        self.tk_select_box_tpye_select.current(0)
        self.tk_select_box_time_select.current(0)

        get_tday(self.tk_select_box_time_select.get())
        get_type(self.tk_select_box_tpye_select.get())
        time_com = True
        Tdata = get_time_mysql()
        print_course_data(value_type, value_day)

        # 显示选课报名
        self.tk_frame_top_left_N.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_K.place_forget()
        self.tk_frame_top_left_G.place_forget()
        self.tk_frame_top_left.place(relx=0.005, rely=0.00, relwidth=0.77, relheight=0.98)

    def students_info(self):
        global time_com
        time_com = False
        # 显示个人信息
        self.tk_frame_top_left.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_K.place_forget()
        self.tk_frame_top_left_G.place_forget()

        self.tk_frame_top_left_N.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        # 显示数据
        self.student_show()
    def class_info(self):
        global time_com
        time_com = False
        # 显示班级信息
        self.tk_frame_top_left.place_forget()
        self.tk_frame_top_left_N.place_forget()
        self.tk_frame_top_left_K.place_forget()
        self.tk_frame_top_left_G.place_forget()

        self.tk_frame_top_left_C.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        # sql 更新数据：学号，姓名，班级
        self.class_info_update()
        pass
    def class_info_update(self):
        # ddd
        user_tno = global_login_name_get()
        data = class_info_data_get(user_tno)
        print(data)
        for item in self.tk_table_class_info.get_children():
            self.tk_table_class_info.delete(item)

        for col in data:
            self.tk_table_class_info.insert("", "end", values=tuple(col))
        pass

    def course_info(self):
        global time_com
        time_com = False
        # 课程信息
        self.tk_frame_top_left.place_forget()
        self.tk_frame_top_left_N.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_G.place_forget()

        self.tk_frame_top_left_K.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        self.course_info_update()
    def course_info_update(self):
        user_tno = global_login_name_get()
        data = course_info_show(user_tno)

        for item in self.tk_table_course_info.get_children():
            self.tk_table_course_info.delete(item)

        for col in data:
            self.tk_table_course_info.insert("", "end", values=tuple(col))
        pass

    # 课程成绩信息
    def course_grade(self):
        global time_com
        time_com = False
        self.tk_frame_top_left.place_forget()
        self.tk_frame_top_left_N.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_K.place_forget()

        self.tk_frame_top_left_G.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)

        self.course_grade_update()
        pass
    def course_grade_update(self):
        user_sno = global_login_name_get()
        data = course_grade_show(user_sno)

        for item in self.tk_table_grade_info.get_children():
            self.tk_table_grade_info.delete(item)

        for col in data:
            self.tk_table_grade_info.insert("", "end", values=tuple(col))

        pass
    def app_read(self):
        global time_com
        time_com = False
        print("帮助与使用说明")
    def app_update(self):
        global time_com
        time_com = False
        print("更新操作")
    def app_destroy(self):
        self.master.destroy()
    def __event_bind(self):
        pass

    def student_show(self):
        user_sno = global_login_name_get()
        password_key = student_info_get_mysql(user_sno)
        name_mottor_class_sdept_sex_age = student_info_get_mysql2(user_sno)
        print(password_key)
        print(name_mottor_class_sdept_sex_age)
        # 设置
        self.tk_label_info_n_txt.configure(text=name_mottor_class_sdept_sex_age[0])
        self.tk_label_info_u_txt.configure(text=user_sno)
        self.tk_label_info_c_txt.configure(text=name_mottor_class_sdept_sex_age[2])
        self.tk_label_info_tem_txt.configure(text=name_mottor_class_sdept_sex_age[3])
        self.tk_label_sex_txt.configure(text=name_mottor_class_sdept_sex_age[4])
        self.tk_label_age_txt.configure(text=name_mottor_class_sdept_sex_age[5])

        self.tk_input_info_m_in.delete(0, ttk.END)
        self.tk_input_info_p_in.delete(0, ttk.END)
        self.tk_input_info_k_in.delete(0, ttk.END)

        self.tk_input_info_m_in.insert(0, name_mottor_class_sdept_sex_age[1])
        self.tk_input_info_p_in.insert(0, password_key[0])
        self.tk_input_info_k_in.insert(0, password_key[1])

        pass
# 测试例
if __name__ == "__main__":
    # win = StudentMenu()
    # win.mainloop()
    pass