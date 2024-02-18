import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox

from file_fun import save_file
from gl import get_user_password_flag, global_login_name_get, global_course_tacno_set, global_course_tacno_get
from mysql import teacher_info_get_mysql, teacher_info_update_mysql
from mysql2 import teacher_info_get_mysql2, Tc_info_data_mysql2, Tac_info_data_mysql2, \
    find_course_cno_mysql2, update_grade_cno_mysql2, find_grade_cname_mysql2, \
    Tac_info_grade_mysql2, find_grade_ctpye_mysql2, grade_excl_mysql2


def check_treeview_empty(tree):
    # 获取表格中的行数
    num_rows = tree.get_children('')[0]
    # 遍历所有行
    for row in range(num_rows):
        # 检查每一行的所有列是否为空
        for column in range(len(tree.column)):
            value = tree.set(row, column)
            if value == '':
                return True  # 如果发现空值，返回True表示表格不为空
    # 如果遍历完所有行都没有发现空值，返回False表示表格为空
    return False
class WinGUI(ttk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__()
        # self.__win()
        self.pack(fill=BOTH, expand=YES)
        self.tk_frame_top = self.__tk_frame_top(self)
        self.tk_frame_top_right = self.__tk_frame_top_right(self.tk_frame_top)

        # 个人课程
        self.tk_frame_top_left_Te = self.__tk_frame_top_left_Te(self.tk_frame_top)
        self.tk_label_frame_te_info1 = self.__tk_label_frame_te_info1(self.tk_frame_top_left_Te)
        self.tk_table_Tc_info_show = self.__tk_table_Tc_info_show(self.tk_label_frame_te_info1)
        self.tk_button_t_course_excl = self.__tk_button_t_course_excl(self.tk_label_frame_te_info1)
        self.tk_label_infoc_tpye = self.__tk_label_infoc_tpye(self.tk_label_frame_te_info1)
        self.tk_select_box_tpye_1 = self.__tk_select_box_tpye_1(self.tk_label_frame_te_info1)

        # 课程班级
        self.tk_frame_top_left_Tac = self.__tk_frame_top_left_Tac(self.tk_frame_top)
        self.tk_label_frame_Tac_info1 = self.__tk_label_frame_Tac_info1(self.tk_frame_top_left_Tac)
        self.tk_table_Tac_grade_show = self.__tk_table_Tac_grade_show(self.tk_label_frame_Tac_info1)
        self.tk_button_tac_course_excl = self.__tk_button_tac_course_excl(self.tk_label_frame_Tac_info1)
        self.tk_select_box_tac_tpye_se = self.__tk_select_box_tac_tpye_se(self.tk_label_frame_Tac_info1)
        self.tk_label_tac_tpye = self.__tk_label_tac_tpye(self.tk_label_frame_Tac_info1)
        self.tk_table_Tac_course_show = self.__tk_table_Tac_course_show(self.tk_label_frame_Tac_info1)
        # self.tk_label_find_sno = self.__tk_label_find_sno(self.tk_label_frame_Tac_info1)
        # self.tk_input_find_sno_in = self.__tk_input_find_sno_in(self.tk_label_frame_Tac_info1)
        # self.tk_button_find_sno_enter = self.__tk_button_find_sno_enter(self.tk_label_frame_Tac_info1)
        self.tk_label_sno = self.__tk_label_sno(self.tk_label_frame_Tac_info1)
        self.tk_label_sno_txt = self.__tk_label_sno_txt(self.tk_label_frame_Tac_info1)
        self.tk_label_sname = self.__tk_label_sname(self.tk_label_frame_Tac_info1)
        self.tk_label_sname_txt = self.__tk_label_sname_txt(self.tk_label_frame_Tac_info1)
        self.tk_label_class = self.__tk_label_class(self.tk_label_frame_Tac_info1)
        self.tk_label_class_txt = self.__tk_label_class_txt(self.tk_label_frame_Tac_info1)
        self.tk_label_grade = self.__tk_label_grade(self.tk_label_frame_Tac_info1)
        self.tk_input_grade_in = self.__tk_input_grade_in(self.tk_label_frame_Tac_info1)
        self.tk_button_grade_enter = self.__tk_button_grade_enter(self.tk_label_frame_Tac_info1)

        # 个人信息
        self.tk_frame_top_left_Ti = self.__tk_frame_top_left_Ti(self.tk_frame_top)
        self.tk_label_frame_te_info3 = self.__tk_label_frame_te_info3(self.tk_frame_top_left_Ti)
        self.tk_label_name = self.__tk_label_name(self.tk_label_frame_te_info3)
        self.tk_label_name_txt = self.__tk_label_name_txt(self.tk_label_frame_te_info3)
        self.tk_label_age = self.__tk_label_age(self.tk_label_frame_te_info3)
        self.tk_label_age_txt = self.__tk_label_age_txt(self.tk_label_frame_te_info3)
        self.tk_label_sex = self.__tk_label_sex(self.tk_label_frame_te_info3)
        self.tk_label_sex_txt = self.__tk_label_sex_txt(self.tk_label_frame_te_info3)
        self.tk_label_tno = self.__tk_label_tno(self.tk_label_frame_te_info3)
        self.tk_label_tno_txt = self.__tk_label_tno_txt(self.tk_label_frame_te_info3)
        self.tk_label_deb = self.__tk_label_deb(self.tk_label_frame_te_info3)
        self.tk_label_tpt = self.__tk_label_tpt(self.tk_label_frame_te_info3)
        self.tk_label_teb_txt = self.__tk_label_teb_txt(self.tk_label_frame_te_info3)
        self.tk_label_tpt_txt = self.__tk_label_tpt_txt(self.tk_label_frame_te_info3)
        self.tk_label_dept = self.__tk_label_dept(self.tk_label_frame_te_info3)
        self.tk_label_dept_txt = self.__tk_label_dept_txt(self.tk_label_frame_te_info3)
        self.tk_label_password = self.__tk_label_password(self.tk_label_frame_te_info3)
        self.tk_input_password_in = self.__tk_input_password_in(self.tk_label_frame_te_info3)
        self.tk_label_key = self.__tk_label_key(self.tk_label_frame_te_info3)
        self.tk_input_key_in = self.__tk_input_key_in(self.tk_label_frame_te_info3)
        self.tk_button_update = self.__tk_button_update(self.tk_label_frame_te_info3)

        self.tk_frame_button = self.__tk_frame_button(self)
        self.tk_text_button_txt = self.__tk_text_button_txt(self.tk_frame_button)

        self.tk_label_tno_txt.configure(text=global_login_name_get())
    def scrollbar_autohide(self, vbar, hbar, widget):
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

    def v_scrollbar(self, vbar, widget, x, y, w, h, pw, ph):
        widget.configure(yscrollcommand=vbar.set)
        vbar.config(command=widget.yview)
        vbar.place(relx=(w + x) / pw, rely=y / ph, relheight=h / ph, anchor='ne')

    def h_scrollbar(self, hbar, widget, x, y, w, h, pw, ph):
        widget.configure(xscrollcommand=hbar.set)
        hbar.config(command=widget.xview)
        hbar.place(relx=x / pw, rely=(y + h) / ph, relwidth=w / pw, anchor='sw')

    def create_bar(self, master, widget, is_vbar, is_hbar, x, y, w, h, pw, ph):
        vbar, hbar = None, None
        if is_vbar:
            vbar = ttk.Scrollbar(master)
            self.v_scrollbar(vbar, widget, x, y, w, h, pw, ph)
        if is_hbar:
            hbar = ttk.Scrollbar(master, orient="horizontal")
            self.h_scrollbar(hbar, widget, x, y, w, h, pw, ph)
        self.scrollbar_autohide(vbar, hbar, widget)

    def __tk_frame_top(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.82)
        return frame

    def __tk_frame_top_right(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.77, rely=0.00, relwidth=0.23, relheight=0.98)
        return frame

    def __tk_label_frame_introduce(self, parent):
        frame = ttk.LabelFrame(parent, text="个人简介", )
        frame.place(relx=0.05, rely=0.02, relwidth=0.91, relheight=0.47)
        return frame

    def __tk_label_image(self, parent):
        label = ttk.Label(parent, text="图像", anchor="center", )
        label.place(relx=0.55, rely=0.00, relwidth=0.40, relheight=0.38)
        return label

    def __tk_frame_top_left_Te(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_label_frame_te_info1(self, parent):
        frame = ttk.LabelFrame(parent, text="个人课程", )
        frame.place(relx=0.01, rely=0.00, relwidth=0.99, relheight=0.98)
        return frame

    def __tk_table_Tc_info_show(self, parent):
        # 表头字段 表头宽度
        columns = {"课程类型": 107, "课程名": 143, "学分": 71, "上课时间": 179, "上课地点": 179, "": 15}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.01, rely=0.06, relwidth=0.98, relheight=0.93)
        self.create_bar(parent, tk_table, True, False, 3, 34, 719, 500, 730, 540)
        return tk_table

    def __tk_button_t_course_excl(self, parent):
        btn = ttk.Button(parent, text="导出表格", takefocus=False, command=self.button_t_course_excl)
        btn.place(relx=0.91, rely=0.00, relwidth=0.08, relheight=0.04)
        return btn
    def button_t_course_excl(self):
        user_n = self.tk_label_tno_txt.cget("text")
        user_n += self.tk_label_name_txt.cget("text")
        user_n += '_课程表'
        data = self.Tc_info_data(self.tk_select_box_tpye_1.get(), self.tk_label_tno_txt.cget("text"))
        tlow = self.Tc_info_data(self.tk_select_box_tpye_1.get(), self.tk_label_tno_txt.cget("text"), False)

        save_file(user_n, data, tlow)
        pass
    def __tk_label_infoc_tpye(self, parent):
        label = ttk.Label(parent, text="课程类型：", anchor="center", )
        label.place(relx=0.72, rely=0.00, relwidth=0.08, relheight=0.04)
        return label
    def __tk_select_box_tpye_1(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("全部", "必修课", "选修课", "体育课", "文化课", "通识课")
        cb.bind("<<ComboboxSelected>>", self.select_box_info)
        cb.place(relx=0.795, rely=0.00, relwidth=0.10, relheight=0.04)

        return cb

    def __tk_frame_top_left_Tac(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_label_frame_Tac_info1(self, parent):
        frame = ttk.LabelFrame(parent, text="课程班级", )
        frame.place(relx=0.01, rely=0.00, relwidth=0.99, relheight=0.98)
        return frame

    def __tk_table_Tac_grade_show(self, parent):
        # 表头字段 表头宽度
        columns = {"学号": 124, "姓名": 124, "班级": 124, "成绩": 99,"": 15}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.31, rely=0.06, relwidth=0.68, relheight=0.69)
        self.create_bar(parent, tk_table, True, False, 221, 34, 500, 370, 730, 540)
        tk_table.bind('<<TreeviewSelect>>', self.grade_select)
        return tk_table
    def grade_select(self, event):
        selection = event.widget.selection()
        if selection:
            # 获取选中的行索引
            index = selection[0]
            # 获取行中的数据
            grade = event.widget.set(index)
            print(f'{grade}')
            self.tk_label_sno_txt.configure(text=grade["学号"])
            self.tk_label_sname_txt.configure(text=grade["姓名"])
            self.tk_label_class_txt.configure(text=grade["班级"])
            self.tk_input_grade_in.delete(0, ttk.END)
            self.tk_input_grade_in.insert(0, grade["成绩"])
        pass
    def __tk_button_tac_course_excl(self, parent):
        btn = ttk.Button(parent, text="导出表格", takefocus=False, command=self.button_tac_course_excl)
        btn.place(relx=0.91, rely=0.01, relwidth=0.08, relheight=0.04)
        return btn
    def button_tac_course_excl(self):
        tno = global_login_name_get()
        cno = global_course_tacno_get()
        cname = find_grade_cname_mysql2(cno)
        tpye = find_grade_ctpye_mysql2(cno)
        print(cname)
        print(tpye)
        filename = tpye[0]
        filename += "_"
        filename += cname[0]
        filename += '_学生成绩表'
        # 课程类型_课程名_学生成绩表
        # sql
        data = grade_excl_mysql2(cno, tno)
        tlow = grade_excl_mysql2(cno, tno,False)
        save_file(filename, data, tlow)
        pass

    def __tk_select_box_tac_tpye_se(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("全部", "必修课", "选修课", "体育课", "文化课", "通识课")
        cb.place(relx=0.20, rely=0.01, relwidth=0.10, relheight=0.04)
        cb.bind("<<ComboboxSelected>>", self.select_tac_tpye)
        return cb
    def select_tac_tpye(self, event):
        # 刷新
        self.tk_label_sno_txt.configure(text="")
        self.tk_label_sname_txt.configure(text="")
        self.tk_label_class_txt.configure(text="")
        self.tk_input_grade_in.delete(0, ttk.END)

        tpye = event.widget.get()
        tno = self.tk_label_tno_txt.cget("text")
        data = Tac_info_data_mysql2(tpye, tno)
        for item in self.tk_table_Tac_course_show.get_children():
            self.tk_table_Tac_course_show.delete(item)
        for col in data:
            self.tk_table_Tac_course_show.insert("", "end", values=tuple(col))

        for item in self.tk_table_Tac_grade_show.get_children():
            self.tk_table_Tac_grade_show.delete(item)
        pass

    def __tk_label_tac_tpye(self, parent):
        label = ttk.Label(parent, text="课程类型：", anchor="center", )
        label.place(relx=0.12, rely=0.00, relwidth=0.08, relheight=0.06)
        return label

    def __tk_table_Tac_course_show(self, parent):
        # 表头字段 表头宽度
        columns = {"课程类型": 75, "课程": 145, "": 15}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.01, rely=0.06, relwidth=0.29, relheight=0.69)
        self.create_bar(parent, tk_table, True, False, 3, 34, 215, 370, 730, 540)
        tk_table.bind('<<TreeviewSelect>>', self.tpye_select)
        return tk_table
    def tpye_select(self, event):
        selection = event.widget.selection()
        if selection:
            # 获取选中的行索引
            index = selection[0]
            # 获取行中的数据
            course = event.widget.set(index)
            print(f'{course}')
            # 使用课程类型+课程名，来查找课程编号cno
            tpye = course['课程类型']
            cname = course['课程']

            cno = find_course_cno_mysql2(tpye, cname)
            # 刷新
            self.tk_label_sno_txt.configure(text="")
            self.tk_label_sname_txt.configure(text="")
            self.tk_label_class_txt.configure(text="")
            self.tk_input_grade_in.delete(0, ttk.END)
            global_course_tacno_set(cno)
            tno = self.tk_label_tno_txt.cget("text")

            data = self.Tac_info_grade(cno, tno)
            for item in self.tk_table_Tac_grade_show.get_children():
                self.tk_table_Tac_grade_show.delete(item)
            for col in data:
                self.tk_table_Tac_grade_show.insert("", "end", values=tuple(col))
        pass
    def Tac_info_grade(self, cno, tno):
        data = Tac_info_grade_mysql2(cno, tno)

        return data
        pass
    def __tk_label_find_sno(self, parent):
        label = ttk.Label(parent, text="学 号：", anchor="center", )
        label.place(relx=0.31, rely=0.00, relwidth=0.07, relheight=0.06)
        return label

    def __tk_input_find_sno_in(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.38, rely=0.01, relwidth=0.16, relheight=0.04)
        return ipt

    def __tk_button_find_sno_enter(self, parent):
        btn = ttk.Button(parent, text="查找", takefocus=False, command=self.button_find_sno_enter)
        btn.place(relx=0.55, rely=0.01, relwidth=0.07, relheight=0.04)
        return btn
    def button_find_sno_enter(self):
        result = check_treeview_empty(self.tk_table_Tac_grade_show)
        if result:

            pass
        else:
            messagebox.showerror("表格内容不能为空！请先选择课程！")
    def __tk_label_sno(self, parent):
        label = ttk.Label(parent, text="学 号：", anchor="center", )
        label.place(relx=0.31, rely=0.76, relwidth=0.07, relheight=0.06)
        return label

    def __tk_label_sno_txt(self, parent):
        label = ttk.Label(parent, text="学号", anchor="center", )
        label.place(relx=0.38, rely=0.76, relwidth=0.14, relheight=0.06)
        return label

    def __tk_label_sname(self, parent):
        label = ttk.Label(parent, text="姓 名：", anchor="center", )
        label.place(relx=0.31, rely=0.82, relwidth=0.07, relheight=0.06)
        return label

    def __tk_label_sname_txt(self, parent):
        label = ttk.Label(parent, text="姓名", anchor="center", )
        label.place(relx=0.38, rely=0.82, relwidth=0.14, relheight=0.06)
        return label

    def __tk_label_class(self, parent):
        label = ttk.Label(parent, text="班 级：", anchor="center", )
        label.place(relx=0.31, rely=0.88, relwidth=0.07, relheight=0.06)
        return label

    def __tk_label_class_txt(self, parent):
        label = ttk.Label(parent, text="班级", anchor="center", )
        label.place(relx=0.38, rely=0.88, relwidth=0.14, relheight=0.06)
        return label

    def __tk_label_grade(self, parent):
        label = ttk.Label(parent, text="成 绩：", anchor="center", )
        label.place(relx=0.60, rely=0.76, relwidth=0.07, relheight=0.06)
        return label

    def __tk_input_grade_in(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.68, rely=0.77, relwidth=0.14, relheight=0.04)
        return ipt

    def __tk_button_grade_enter(self, parent):
        btn = ttk.Button(parent, text="修改", takefocus=False, command=self.button_grade_enter)
        btn.place(relx=0.75, rely=0.88, relwidth=0.07, relheight=0.04)
        return btn
    def button_grade_enter(self):
        sno = self.tk_label_sno_txt.cget("text")
        if len(sno):
            grade = self.tk_input_grade_in.get()
            cno = global_course_tacno_get()
            tno = self.tk_label_tno_txt.cget("text")
            update_grade_cno_mysql2(grade, cno, sno)
            # 更新表格内容显示
            # 更新标签
            self.tk_label_sno_txt.configure(text="")
            self.tk_label_sname_txt.configure(text="")
            self.tk_label_class_txt.configure(text="")
            self.tk_input_grade_in.delete(0, ttk.END)
            # 更新表格
            data = self.Tac_info_grade(cno, tno)
            for item in self.tk_table_Tac_grade_show.get_children():
                self.tk_table_Tac_grade_show.delete(item)
            for col in data:
                self.tk_table_Tac_grade_show.insert("", "end", values=tuple(col))
        else:
            messagebox.showinfo("信息提示", "请选择内容！")
        pass
    def select_box_info(self, event):
        tpye = event.widget.get()
        tno = self.tk_label_tno_txt.cget("text")
        data = self.Tc_info_data(tpye, tno)
        for item in self.tk_table_Tc_info_show.get_children():
            self.tk_table_Tc_info_show.delete(item)
        for col in data:
            self.tk_table_Tc_info_show.insert("", "end", values=tuple(col))
        pass
    def Tc_info_data(self, tpye, tno, select=True):
        data = Tc_info_data_mysql2(tpye, tno, select)
        return data
        pass
    def __tk_frame_top_left_Ti(self, parent):
        frame = ttk.Frame(parent,)
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame
    def __tk_label_frame_te_info3(self,parent):
        frame = ttk.LabelFrame(parent,text="个人信息",)
        frame.place(relx=0.00, rely=0.00, relwidth=0.99, relheight=0.98)
        return frame
    def __tk_label_name(self,parent):
        label = ttk.Label(parent,text="姓 名：",anchor="center", )
        label.place(relx=0.07, rely=0.05, relwidth=0.07, relheight=0.06)
        return label
    def __tk_label_name_txt(self,parent):
        label = ttk.Label(parent,text="姓名",anchor="center", )
        label.place(relx=0.14, rely=0.05, relwidth=0.16, relheight=0.06)
        return label
    def __tk_label_age(self,parent):
        label = ttk.Label(parent,text="年 龄：",anchor="center", )
        label.place(relx=0.36, rely=0.11, relwidth=0.07, relheight=0.06)
        return label
    def __tk_label_age_txt(self,parent):
        label = ttk.Label(parent,text="年龄",anchor="center", )
        label.place(relx=0.43, rely=0.11, relwidth=0.07, relheight=0.06)
        return label
    def __tk_label_sex(self,parent):
        label = ttk.Label(parent,text="性 别：",anchor="center", )
        label.place(relx=0.36, rely=0.05, relwidth=0.07, relheight=0.06)
        return label
    def __tk_label_sex_txt(self,parent):
        label = ttk.Label(parent,text="性别",anchor="center", )
        label.place(relx=0.43, rely=0.05, relwidth=0.07, relheight=0.06)
        return label
    def __tk_label_tno(self,parent):
        label = ttk.Label(parent,text="工 号：",anchor="center", )
        label.place(relx=0.07, rely=0.11, relwidth=0.07, relheight=0.06)
        return label
    def __tk_label_tno_txt(self,parent):
        label = ttk.Label(parent,text="工号",anchor="center", )
        label.place(relx=0.14, rely=0.11, relwidth=0.16, relheight=0.06)
        return label
    def __tk_label_deb(self,parent):
        label = ttk.Label(parent,text="学 历：",anchor="center", )
        label.place(relx=0.07, rely=0.16, relwidth=0.07, relheight=0.06)
        return label
    def __tk_label_tpt(self,parent):
        label = ttk.Label(parent,text="职 称：",anchor="center", )
        label.place(relx=0.07, rely=0.22, relwidth=0.07, relheight=0.06)
        return label
    def __tk_label_teb_txt(self,parent):
        label = ttk.Label(parent,text="学历",anchor="center", )
        label.place(relx=0.14, rely=0.16, relwidth=0.16, relheight=0.06)
        return label
    def __tk_label_tpt_txt(self,parent):
        label = ttk.Label(parent,text="职称",anchor="center", )
        label.place(relx=0.14, rely=0.22, relwidth=0.16, relheight=0.06)
        return label
    def __tk_label_dept(self,parent):
        label = ttk.Label(parent,text="院 系：",anchor="center", )
        label.place(relx=0.07, rely=0.28, relwidth=0.07, relheight=0.06)
        return label
    def __tk_label_dept_txt(self,parent):
        label = ttk.Label(parent,text="院系",anchor="center", )
        label.place(relx=0.14, rely=0.28, relwidth=0.16, relheight=0.06)
        return label
    def __tk_label_password(self,parent):
        label = ttk.Label(parent,text="密 码：",anchor="center", )
        label.place(relx=0.07, rely=0.36, relwidth=0.07, relheight=0.06)
        return label
    def __tk_input_password_in(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.37, relwidth=0.16, relheight=0.04)
        return ipt
    def __tk_label_key(self,parent):
        label = ttk.Label(parent,text="密 钥：",anchor="center", )
        label.place(relx=0.07, rely=0.42, relwidth=0.07, relheight=0.06)
        return label
    def __tk_input_key_in(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.43, relwidth=0.16, relheight=0.04)
        return ipt
    def __tk_button_update(self,parent):
        btn = ttk.Button(parent, text="修改", takefocus=False, command=self.button_update)
        btn.place(relx=0.23, rely=0.51, relwidth=0.07, relheight=0.04)
        return btn
    def button_update(self):
        tno = self.tk_label_tno_txt.cget("text")
        tkey = self.tk_input_key_in.get()
        tpassword = self.tk_input_password_in.get()

        if len(tkey) and len(tpassword):
            result = messagebox.showinfo("信息提示", "是否修改？")
            if result:
                # 确认修改
                teacher_info_update_mysql(tno, tpassword, tkey)
                messagebox.showinfo("信息提示", "修改成功！")
                pass
            else:
                # 取消修改
                pass
        else:
            messagebox.showerror("信息提示", "修改内容不能为空！")
        pass

    def __tk_frame_button(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.82, relwidth=1.00, relheight=0.18)
        return frame

    def __tk_text_button_txt(self, parent):
        text = ttk.Text(parent)
        text.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=1.00)
        self.create_bar(parent, text, True, True, 0, 0, 960, 120, 960, 120)
        return text


class TeacherMenu(WinGUI):
    def __init__(self, master, login_name, login_password, **kwargs):
        get_user_password_flag(login_name, login_password)

        super().__init__(master, **kwargs)
        self.__event_bind()
    def create_menu(self):
        menu = ttk.Menu(self, tearoff=False)
        menu.add_cascade(label="课程管理", menu=self.menu_lpld203f(menu))
        menu.add_cascade(label="个人信息", command=self.T_info)
        menu.add_cascade(label="帮助(H)", menu=self.menu_lpld6uvi(menu))
        return menu

    def menu_lpld203f(self, parent):
        menu = ttk.Menu(parent, tearoff=False)
        menu.add_command(label="个人课程", command=self.Tc_course)
        menu.add_command(label="课程信息", command=self.Tac_info)
        return menu

    def menu_lpld6uvi(self, parent):
        menu = ttk.Menu(parent, tearoff=False)
        menu.add_command(label="关于(A)", command=self.app_read)
        menu.add_command(label="检查更新(G)", command=self.app_update)
        menu.add_command(label="退出(E)", command=self.app_destroy)
        return menu

    def Tc_course(self):
        self.tk_frame_top_left_Ti.place_forget()
        self.tk_frame_top_left_Tac.place_forget()

        self.tk_select_box_tpye_1.current(0)
        tpye = self.tk_select_box_tpye_1.get()
        tno = self.tk_label_tno_txt.cget("text")
        data = self.Tc_info_data(tpye, tno)

        for item in self.tk_table_Tc_info_show.get_children():
            self.tk_table_Tc_info_show.delete(item)
        for col in data:
            self.tk_table_Tc_info_show.insert("", "end", values=tuple(col))

        self.tk_frame_top_left_Te.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        pass



    def Tac_info(self):
        self.tk_frame_top_left_Te.place_forget()
        self.tk_frame_top_left_Ti.place_forget()

        self.tk_select_box_tac_tpye_se.current(0)
        self.tk_label_sno_txt.configure(text="")
        self.tk_label_sname_txt.configure(text="")
        self.tk_label_class_txt.configure(text="")
        self.tk_input_grade_in.delete(0, ttk.END)

        tpye = self.tk_select_box_tac_tpye_se.get()
        tno = self.tk_label_tno_txt.cget("text")
        data = Tac_info_data_mysql2(tpye, tno)
        for item in self.tk_table_Tac_course_show.get_children():
            self.tk_table_Tac_course_show.delete(item)
        for col in data:
            self.tk_table_Tac_course_show.insert("", "end", values=tuple(col))

        for item in self.tk_table_Tac_grade_show.get_children():
            self.tk_table_Tac_grade_show.delete(item)

        self.tk_frame_top_left_Tac.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        pass

    def T_info(self):
        self.tk_frame_top_left_Te.place_forget()
        self.tk_frame_top_left_Tac.place_forget()
        # 获取
        user_tno = self.tk_label_tno_txt.cget("text")
        password_key = teacher_info_get_mysql(user_tno)
        data = teacher_info_get_mysql2(user_tno)
        # 清空
        self.tk_input_key_in.delete(0, ttk.END)
        self.tk_input_password_in.delete(0, ttk.END)
        # 更新
        self.tk_input_password_in.insert(0, password_key[0])
        self.tk_input_key_in.insert(0, password_key[1])

        self.tk_label_name_txt.configure(text=data[0])
        self.tk_label_tno_txt.configure(text=data[1])
        self.tk_label_sex_txt.configure(text=data[2])
        self.tk_label_age_txt.configure(text=data[3])
        self.tk_label_teb_txt.configure(text=data[4])
        self.tk_label_tpt_txt.configure(text=data[5])
        self.tk_label_dept_txt.configure(text=data[6])

        self.tk_frame_top_left_Ti.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        pass
    def app_read(self):
        print("帮助与使用说明")
    def app_update(self):
        print("更新操作")
    def app_destroy(self):
        self.master.destroy()
    def __event_bind(self):
        pass
if __name__ == '__main__':
    pass