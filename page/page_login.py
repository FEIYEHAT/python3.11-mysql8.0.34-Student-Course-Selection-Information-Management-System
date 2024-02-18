import ttkbootstrap as ttk
from tkinter import messagebox
from mysql import check_login, check_key, user_pass_set
from page.page_admin import AdminMenu
from page.page_student import StudentMenu
from page.page_teacher import TeacherMenu

import re

# 监测输入框内容
def validate_input(event):  # 正则表达式：判断输入内容
    input_text = event.widget.get()
    if re.match("^[a-zA-Z0-9]*$", input_text):
        event.widget.config(foreground="white")
    elif re.match(".*[\u4e00-\u9fa5].*", input_text):
        event.widget.delete(0, ttk.END)
        event.widget.insert(0, input_text.replace(
            re.findall(r'[\u4e00-\u9fa5]', input_text)[0], ''))
        event.widget.config(foreground="red")
    else:
        event.widget.configure(foreground="white")

class WinGUI(ttk.Window):
    def __init__(self):
        super().__init__()
        # self.pack(fill=BOTH, expand=YES)
        self.__win()
        self.tk_frame_logo = self.__tk_frame_logo(self)
        self.tk_label_logo_image = self.__tk_label_logo_image(self.tk_frame_logo)
        self.tk_frame_cards = self.__tk_frame_cards(self)
        self.tk_tabs_sel_card = self.__tk_tabs_sel_card(self.tk_frame_cards)
        # 登录
        self.tk_input_user_in = self.__tk_input_user_in(self.tk_tabs_sel_card_0)
        self.tk_input_password_in = self.__tk_input_password_in(self.tk_tabs_sel_card_0)
        self.tk_label_user_txt = self.__tk_label_user_txt(self.tk_tabs_sel_card_0)
        self.tk_label_password_txt = self.__tk_label_password_txt(self.tk_tabs_sel_card_0)
        self.tk_label_tip = self.__tk_label_tip(self.tk_tabs_sel_card_0)
        self.tk_button_login = self.__tk_button_login(self.tk_tabs_sel_card_0)
        self.tk_button_exit = self.__tk_button_exit(self.tk_tabs_sel_card_0)
        # 忘记密码
        self.tk_label_user_txt2 = self.__tk_label_user_txt2(self.tk_tabs_sel_card_1)
        self.tk_input_user_in2 = self.__tk_input_user_in2(self.tk_tabs_sel_card_1)
        self.tk_label_password_txt2 = self.__tk_label_password_txt2(self.tk_tabs_sel_card_1)
        self.tk_input_password_in2 = self.__tk_input_password_in2(self.tk_tabs_sel_card_1)
        self.tk_label_key_txt = self.__tk_label_key_txt(self.tk_tabs_sel_card_1)
        self.tk_input_key_in = self.__tk_input_key_in(self.tk_tabs_sel_card_1)
        self.tk_label_tip2 = self.__tk_label_tip2(self.tk_tabs_sel_card_1)
        self.tk_button_set_passwrod = self.__tk_button_set_passwrod(self.tk_tabs_sel_card_1)

    def __win(self):
        self.title("学生选课管理信息系统")
        ttk.Style("solar")
        # 设置窗口大小、居中
        width = 460
        height = 500
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)
        ttk.Style("solar")
        self.minsize(width=width, height=height)

    def __win_student(self):
        self.title("学生端")
        ttk.Style("solar")
        # 设置窗口大小、居中
        width = 1570
        height = 1180
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.minsize(width=width, height=height)
    def __win_teacher(self):
        self.title("教师端")
        # 设置窗口大小、居中
        width = 1570
        height = 1180
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.minsize(width=width, height=height)
    def __win_admin(self):
        self.title("管理端")
        ttk.Style("solar")
        # 设置窗口大小、居中
        width = 1570
        height = 1150
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(geometry)

        self.minsize(width=width, height=height)
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

    def __tk_frame_logo(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.36)
        return frame

    def __tk_label_logo_image(self, parent):
        label = ttk.Label(parent, text="logo图标", anchor="center", )
        label.place(relx=0.01, rely=0.00, relwidth=0.98, relheight=0.95)
        return label

    def __tk_frame_cards(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.36, relwidth=1.00, relheight=0.64)
        return frame

    def __tk_tabs_sel_card(self, parent):
        frame = ttk.Notebook(parent)
        self.tk_tabs_sel_card_0 = self.__tk_frame_sel_card_0(frame)
        frame.add(self.tk_tabs_sel_card_0, text="登录")
        self.tk_tabs_sel_card_1 = self.__tk_frame_sel_card_1(frame)
        frame.add(self.tk_tabs_sel_card_1, text="忘记密码")
        frame.place(relx=0.03, rely=0.00, relwidth=0.93, relheight=1.00)
        return frame

    def __tk_frame_sel_card_0(self, parent):
        frame = ttk.Frame(parent)
        frame.place(relx=0.03, rely=0.00, relwidth=0.93, relheight=1.00)
        return frame

    def __tk_frame_sel_card_1(self, parent):
        frame = ttk.Frame(parent)
        frame.place(relx=0.03, rely=0.00, relwidth=0.93, relheight=1.00)
        return frame

    def __tk_input_user_in(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.30, rely=0.05, relwidth=0.59, relheight=0.15)
        ipt.bind("<Key>", validate_input)
        return ipt

    def __tk_input_password_in(self, parent):
        ipt = ttk.Entry(parent, show="*")
        ipt.place(relx=0.30, rely=0.23, relwidth=0.59, relheight=0.15)
        ipt.bind("<Key>", validate_input)
        return ipt

    def __tk_label_user_txt(self, parent):
        label = ttk.Label(parent, text="账 号：", anchor="center", )
        label.place(relx=0.11, rely=0.05, relwidth=0.19, relheight=0.15)
        return label

    def __tk_label_password_txt(self, parent):
        label = ttk.Label(parent, text="密 码：", anchor="center", )
        label.place(relx=0.11, rely=0.23, relwidth=0.19, relheight=0.15)
        return label

    def __tk_label_tip(self, parent):
        label = ttk.Label(parent, anchor="center",)
        label.place(relx=0.11, rely=0.56, relwidth=0.78, relheight=0.15)
        return label

    def __tk_button_login(self, parent):
        btn = ttk.Button(parent, text="登录", takefocus=False, command=self.login_tip)
        btn.place(relx=0.11, rely=0.72, relwidth=0.19, relheight=0.15)
        return btn

    def __tk_button_exit(self, parent):
        btn = ttk.Button(parent, text="退出", takefocus=False, command=self.destroy)
        btn.place(relx=0.70, rely=0.72, relwidth=0.19, relheight=0.15)
        return btn

    def __tk_label_user_txt2(self, parent):
        label = ttk.Label(parent, text="账 号：", anchor="center", )
        label.place(relx=0.11, rely=0.05, relwidth=0.19, relheight=0.15)
        return label

    def __tk_input_user_in2(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.30, rely=0.05, relwidth=0.59, relheight=0.15)
        ipt.bind("<Key>", validate_input)
        return ipt

    def __tk_label_password_txt2(self, parent):
        label = ttk.Label(parent, text="新密码：", anchor="center", )
        label.place(relx=0.11, rely=0.23, relwidth=0.19, relheight=0.15)
        return label

    def __tk_input_password_in2(self, parent):
        ipt = ttk.Entry(parent, show="*")
        ipt.place(relx=0.30, rely=0.23, relwidth=0.59, relheight=0.15)
        ipt.bind("<Key>", validate_input)
        return ipt

    def __tk_label_key_txt(self, parent):
        label = ttk.Label(parent, text="密 钥：", anchor="center", )
        label.place(relx=0.11, rely=0.41, relwidth=0.19, relheight=0.15)
        return label

    def __tk_input_key_in(self, parent):
        ipt = ttk.Entry(parent, show="*")
        ipt.place(relx=0.30, rely=0.41, relwidth=0.59, relheight=0.15)
        ipt.bind("<Key>", validate_input)
        return ipt

    def __tk_label_tip2(self, parent):
        label = ttk.Label(parent, anchor="w", )
        label.place(relx=0.11, rely=0.60, relwidth=0.57, relheight=0.30)
        return label

    def __tk_button_set_passwrod(self, parent):
        btn = ttk.Button(parent, text="确认", takefocus=False, command=self.button_set_password)
        btn.place(relx=0.70, rely=0.62, relwidth=0.19, relheight=0.15)
        return btn
    def button_set_password(self):
        if len(self.tk_input_user_in2.get()) and len(self.tk_input_password_in2.get()) and len(self.tk_input_key_in.get()):
            # 验证用户是否存在！
            sign = check_login(self.tk_input_user_in2.get(), None, False)
            if sign != 5 and sign != 6:
                # 验证密钥是否存在！
                print(sign)
                relust = check_key(self.tk_input_user_in2.get(), self.tk_input_key_in.get(), sign)
                if relust is True:
                    # 执行修改语句
                    user_pass_set(self.tk_input_user_in2.get(), self.tk_input_password_in2.get(), sign)
                    # 清空
                    self.tk_label_tip2.config(text="")
                    self.tk_input_user_in2.delete(0, ttk.END)
                    self.tk_input_password_in2.delete(0, ttk.END)
                    self.tk_input_key_in.delete(0, ttk.END)
                    messagebox.showinfo("信息提示", "新的密码设置成功！")
                    pass
                else:
                    self.tk_label_tip2.config(text="密钥输入错误！\n请联系管理员修改！")
            else:
                self.tk_label_tip2.config(text="账号不存在！请重新输入！")
            pass
        else:
            self.tk_label_tip2.config(text="输入内容不能为空！")


    def login_tip(self):
        # button登录信息提示
        sign = check_login(self.tk_input_user_in.get(), self.tk_input_password_in.get())
        if sign > 1:
            self.tk_label_tip.config(text="登录成功！")
            # 记录用户：账号//密码
            login_names = self.tk_input_user_in.get()
            login_passwords = self.tk_input_password_in.get()

            if sign == 4:
                """学生端"""
                # 清空界面
                self.tk_frame_logo.place_forget()
                self.tk_frame_cards.place_forget()
                # 显示
                self.__win_student()
                app_student = StudentMenu(self, login_names, login_passwords)
                self.config(menu=app_student.create_menu())
                pass
            if sign == 3:
                """教师端"""
                # 清空界面
                self.tk_frame_logo.place_forget()
                self.tk_frame_cards.place_forget()
                # 显示
                self.__win_teacher()
                app_teacher = TeacherMenu(self, login_names, login_passwords)
                self.config(menu=app_teacher.create_menu())
                pass
            if sign == 2:
                """管理端"""
                # 清空界面
                self.tk_frame_logo.place_forget()
                self.tk_frame_cards.place_forget()
                # 显示
                self.__win_admin()
                app_admin = AdminMenu(self)
                self.config(menu=app_admin.create_menu())
                pass

        elif sign == 1:
            self.tk_label_tip.config(text="密码输入错误！请重试！")
        else:
            self.tk_label_tip.config(text="账号不存在！请重新输入！")
        pass

class Login(WinGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()

    def __event_bind(self):
        pass


if __name__ == "__main__":
    win = Login()
    win.mainloop()