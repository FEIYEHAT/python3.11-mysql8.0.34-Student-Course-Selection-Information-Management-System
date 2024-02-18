import ttkbootstrap as ttk
from ttkbootstrap.constants import *

from tkinter import messagebox

from file_fun import select_file, save_file, batch_add
from gl import set_sevalue, get_sevalue, generate_random_number
from mysql import users_info, users_info_update, user_stduent_add, user_stduent_del, user_teacher_add, user_teacher_del
from mysql2 import dept_info, mysql_connect_csdb, mysql2_close, adept_info_update, adept_info_del, dept_add, \
    file_low_get, adept_info_add_low, dept_data_get, teacher_add, teacher_info_showall, teacher_info_del, \
    teacher_course_find, teacher_find_one, teacher_update, teacher_info_add_low, st_find, student_add, \
    student_info_add_low, student_find_name, student_find_sno, student_info_del, student_update, teacher_find_name, \
    teacher_course_update, course_find, teacher_find_course, mysql_course_add, course_info_low, couse_info_select, \
    course_update, course_del, teachercourse_info, tc_info_select, course_start_info, course_time_set, \
    course_flag_start, course_flag_end

class WinAGUI(ttk.Frame):
    def __init__(self, master, **kwargs):

        super().__init__(master, **kwargs)
        self.pack(fill=BOTH, expand=YES)

        self.tk_frame_top = self.__tk_frame_top(self)
        self.tk_frame_top_right = self.__tk_frame_top_right(self.tk_frame_top)

        ########## 学生管理 ###########
        self.tk_frame_top_left_S = self.__tk_frame_top_left(self.tk_frame_top)
        # ①学生添加
        self.tk_frame_left_1 = self.__tk_frame_left_1(self.tk_frame_top_left_S)
        self.tk_label_frame_student_add = self.__tk_label_frame_student_add(self.tk_frame_left_1)
        self.tk_label_sno = self.__tk_label_sno(self.tk_label_frame_student_add)
        self.tk_input_sno_txtin = self.__tk_input_sno_txtin(self.tk_label_frame_student_add)
        self.tk_label_sname = self.__tk_label_sname(self.tk_label_frame_student_add)
        self.tk_input_sname_txtin = self.__tk_input_sname_txtin(self.tk_label_frame_student_add)
        self.tk_label_class = self.__tk_label_class(self.tk_label_frame_student_add)
        self.tk_input_class_txtin = self.__tk_input_class_txtin(self.tk_label_frame_student_add)
        self.tk_label_dept = self.__tk_label_dept(self.tk_label_frame_student_add)
        self.tk_select_box_sdept_se = self.__tk_select_box_sdept_se(self.tk_label_frame_student_add)
        self.tk_label_ssex = self.__tk_label_ssex(self.tk_label_frame_student_add)
        self.tk_select_box_ssex_se = self.__tk_select_box_ssex_se(self.tk_label_frame_student_add)
        self.tk_label_sage = self.__tk_label_sage(self.tk_label_frame_student_add)
        self.tk_select_box_sage_se = self.__tk_select_box_sage_se(self.tk_label_frame_student_add)
        self.tk_button_student_add_enter = self.__tk_button_student_add_enter(self.tk_label_frame_student_add)
        self.tk_frame_left_2 = self.__tk_frame_left_2(self.tk_frame_top_left_S)
        self.tk_label_frame_student_add_batch = self.__tk_label_frame_student_add_batch(self.tk_frame_left_2)
        self.tk_button_excl_file_se = self.__tk_button_excl_file_se(self.tk_label_frame_student_add_batch)
        self.tk_button_excl_file_demp = self.__tk_button_excl_file_demp(self.tk_label_frame_student_add_batch)

        # ②学生修改
        self.tk_frame_top_left_S2 = self.__tk_frame_top_left_S2(self.tk_frame_top)
        self.tk_frame_s2left_1 = self.__tk_frame_s2left_1(self.tk_frame_top_left_S2)
        self.tk_label_frame_student_update = self.__tk_label_frame_student_update(self.tk_frame_s2left_1)
        self.tk_label_sno_up = self.__tk_label_sno_up(self.tk_label_frame_student_update)
        self.tk_label_sno_up_txtin = self.__tk_label_sno_up_txtin(self.tk_label_frame_student_update)
        self.tk_label_sname_up = self.__tk_label_sname_up(self.tk_label_frame_student_update)
        self.tk_input_sname_up_txtin = self.__tk_input_sname_up_txtin(self.tk_label_frame_student_update)
        self.tk_label_sdept_up = self.__tk_label_sdept_up(self.tk_label_frame_student_update)
        self.tk_select_box_sdept_up_se = self.__tk_select_box_sdept_up_se(self.tk_label_frame_student_update)
        self.tk_label_ssex_up = self.__tk_label_ssex_up(self.tk_label_frame_student_update)
        self.tk_select_box_ssex_up_se = self.__tk_select_box_ssex_up_se(self.tk_label_frame_student_update)
        self.tk_label_sage_up = self.__tk_label_sage_up(self.tk_label_frame_student_update)
        self.tk_select_box_sage_up_se = self.__tk_select_box_sage_up_se(self.tk_label_frame_student_update)
        self.tk_button_student_update_enter = self.__tk_button_student_update_enter(self.tk_label_frame_student_update)
        self.tk_button_student_del_enter = self.__tk_button_student_del_enter(self.tk_label_frame_student_update)
        # self.tk_label_s2left_tip = self.__tk_label_s2left_tip(self.tk_label_frame_student_update)
        self.tk_label_class_up = self.__tk_label_class_up(self.tk_label_frame_student_update)
        self.tk_input_class_up_txtin = self.__tk_input_class_up_txtin(self.tk_label_frame_student_update)
        self.tk_frame_s2left_2 = self.__tk_frame_s2left_2(self.tk_frame_top_left_S2)
        self.tk_table_st_find = self.__tk_table_st_find(self.tk_frame_s2left_2)
        self.tk_label_snotxt = self.__tk_label_snotxt(self.tk_frame_s2left_2)
        self.tk_input_sno_findin = self.__tk_input_sno_findin(self.tk_frame_s2left_2)
        self.tk_button_snofind_enter = self.__tk_button_snofind_enter(self.tk_frame_s2left_2)

        # ③学生信息表
        self.tk_frame_top_left_S3 = self.__tk_frame_top_left_S3(self.tk_frame_top)
        self.tk_frame_stinfo_left = self.__tk_frame_stinfo_left(self.tk_frame_top_left_S3)
        self.tk_label_frame_student_info3 = self.__tk_label_frame_student_info3(self.tk_frame_stinfo_left)
        self.tk_table_st_info_show = self.__tk_table_st_info_show(self.tk_label_frame_student_info3)
        # self.tk_input_st_info_find_sno = self.__tk_input_st_info_find_sno(self.tk_label_frame_student_info3)
        # self.tk_label_st_info_sno = self.__tk_label_st_info_sno(self.tk_label_frame_student_info3)
        self.tk_button_student_export_file_enter = self.__tk_button_student_export_file_enter(self.tk_label_frame_student_info3)
        self.tk_label_st_info_name = self.__tk_label_st_info_name(self.tk_label_frame_student_info3)
        self.tk_input_st_info_find_name = self.__tk_input_st_info_find_name(self.tk_label_frame_student_info3)
        self.tk_button_st_info_enter = self.__tk_button_st_info_enter(self.tk_label_frame_student_info3)
        ####### -- 学生管理 -- ########

        ########## 教工管理 ###########
        self.tk_frame_top_left_T = self.__tk_frame_top_left(self.tk_frame_top)
        # ①教工添加
        self.tk_frame_tleft_1 = self.__tk_frame_tleft_1(self.tk_frame_top_left_T)
        self.tk_label_frame_teacher_add = self.__tk_label_frame_teacher_add(self.tk_frame_tleft_1)
        self.tk_label_tno = self.__tk_label_tno(self.tk_label_frame_teacher_add)
        self.tk_input_tno_txtin = self.__tk_input_tno_txtin(self.tk_label_frame_teacher_add)
        self.tk_label_tname = self.__tk_label_tname(self.tk_label_frame_teacher_add)
        self.tk_input_tname_add_txtin = self.__tk_input_tname_add_txtin(self.tk_label_frame_teacher_add)
        self.tk_label_tdept = self.__tk_label_tdept(self.tk_label_frame_teacher_add)
        self.tk_select_box_tdept_se = self.__tk_select_box_tdept_se(self.tk_label_frame_teacher_add)
        self.tk_label_tsex = self.__tk_label_tsex(self.tk_label_frame_teacher_add)
        self.tk_select_box_tsex_se = self.__tk_select_box_tsex_se(self.tk_label_frame_teacher_add)
        self.tk_label_tage = self.__tk_label_tage(self.tk_label_frame_teacher_add)
        self.tk_select_box_tage_se = self.__tk_select_box_tage_se(self.tk_label_frame_teacher_add)
        self.tk_button_teacher_add_enter = self.__tk_button_teacher_add_enter(self.tk_label_frame_teacher_add)
        self.tk_label_teb = self.__tk_label_teb(self.tk_label_frame_teacher_add)
        self.tk_label_tpt = self.__tk_label_tpt(self.tk_label_frame_teacher_add)
        self.tk_select_box_teb_se = self.__tk_select_box_teb_se(self.tk_label_frame_teacher_add)
        self.tk_select_box_tpt_se = self.__tk_select_box_tpt_se(self.tk_label_frame_teacher_add)
        self.tk_frame_tleft_2 = self.__tk_frame_tleft_2(self.tk_frame_top_left_T)
        self.tk_label_frame_teacher_add_batch = self.__tk_label_frame_teacher_add_batch(self.tk_frame_tleft_2)
        self.tk_button_texcl_file_se = self.__tk_button_texcl_file_se(self.tk_label_frame_teacher_add_batch)
        # self.tk_button_teacher_add_batch_enter = self.__tk_button_teacher_add_batch_enter(self.tk_label_frame_teacher_add_batch)
        self.tk_button_texcl_file_demp = self.__tk_button_texcl_file_demp(self.tk_label_frame_teacher_add_batch)

        # ②教工修改
        self.tk_frame_top_left_T2 = self.__tk_frame_top_left_T2(self.tk_frame_top)
        self.tk_frame_t2left_1 = self.__tk_frame_t2left_1(self.tk_frame_top_left_T2)
        self.tk_label_frame_teacher_update = self.__tk_label_frame_teacher_update(self.tk_frame_t2left_1)
        self.tk_label_tno_up = self.__tk_label_tno_up(self.tk_label_frame_teacher_update)
        self.tk_label_tno_up_txtin = self.__tk_label_tno_up_txtin( self.tk_label_frame_teacher_update)
        self.tk_label_tname_up = self.__tk_label_tname_up(self.tk_label_frame_teacher_update)
        self.tk_input_tname_up_txtin = self.__tk_input_tname_txtin_up(self.tk_label_frame_teacher_update)
        self.tk_label_tdept_up = self.__tk_label_tdept_up(self.tk_label_frame_teacher_update)
        self.tk_select_box_tdept_up_se = self.__tk_select_box_tdept_up_se(self.tk_label_frame_teacher_update)
        self.tk_label_tsex_up = self.__tk_label_tsex_up(self.tk_label_frame_teacher_update)
        self.tk_select_box_tsex_up_se = self.__tk_select_box_tsex_up_se(self.tk_label_frame_teacher_update)
        self.tk_label_tage_up = self.__tk_label_tage_up(self.tk_label_frame_teacher_update)
        self.tk_select_box_tage_up_se = self.__tk_select_box_tage_up_se(self.tk_label_frame_teacher_update)
        self.tk_button_teacher_update_enter = self.__tk_button_teacher_update_enter(self.tk_label_frame_teacher_update)
        self.tk_button_teacher_del_enter = self.__tk_button_teacher_del_enter(self.tk_label_frame_teacher_update)
        # self.tk_label_t2left_tip = self.__tk_label_t2left_tip(self.tk_label_frame_teacher_update)
        self.tk_label_teb_up = self.__tk_label_teb_up(self.tk_label_frame_teacher_update)
        self.tk_label_tpt_up = self.__tk_label_tpt_up(self.tk_label_frame_teacher_update)
        self.tk_select_box_teb_up_se = self.__tk_select_box_teb_up_se(self.tk_label_frame_teacher_update)
        self.tk_select_box_tpt_up_se = self.__tk_select_box_tpt_up_se(self.tk_label_frame_teacher_update)
        self.tk_frame_t2left_2 = self.__tk_frame_t2left_2(self.tk_frame_top_left_T2)
        self.tk_table_te_find = self.__tk_table_te_find(self.tk_frame_t2left_2)
        self.tk_label_tnotxt = self.__tk_label_tnotxt(self.tk_frame_t2left_2)
        self.tk_input_tno_findin = self.__tk_input_tno_findin(self.tk_frame_t2left_2)
        self.tk_button_tnofind_enter = self.__tk_button_tnofind_enter(self.tk_frame_t2left_2)

        # ③教工信息表
        self.tk_frame_top_left_T3 = self.__tk_frame_top_left_T3(self.tk_frame_top)
        self.tk_frame_seinfo_left = self.__tk_frame_seinfo_left(self.tk_frame_top_left_T3)
        self.tk_label_frame_teacher_info3 = self.__tk_label_frame_teacher_info3(self.tk_frame_seinfo_left)
        self.tk_table_se_info_show = self.__tk_table_se_info_show(self.tk_label_frame_teacher_info3)
        self.tk_button_se_info_enter = self.__tk_button_se_info_enter(self.tk_label_frame_teacher_info3)

        self.tk_label_e_info_name = self.__tk_label_se_info_name(self.tk_label_frame_teacher_info3)
        self.tk_input_e_info_find_name = self.__tk_input_se_info_find_name(self.tk_label_frame_teacher_info3)
        self.tk_button_e_info_enter = self.__tk_button_e_info_enter(self.tk_label_frame_teacher_info3)
        ####### -- 教工管理 -- ########

        ########   院系管理   #########
        # ①院系添加
        self.tk_frame_top_left_D = self.__tk_frame_top_left_D(self.tk_frame_top)
        self.tk_frame_dleft_1 = self.__tk_frame_dleft_1(self.tk_frame_top_left_D)
        self.tk_label_frame_dept_add = self.__tk_label_frame_dept_add(self.tk_frame_dleft_1)
        self.tk_label_dno = self.__tk_label_dno(self.tk_label_frame_dept_add)
        self.tk_input_dno_txtin = self.__tk_input_dno_txtin(self.tk_label_frame_dept_add)
        self.tk_label_dname = self.__tk_label_dname(self.tk_label_frame_dept_add)
        self.tk_input_dname_txtin = self.__tk_input_dname_txtin(self.tk_label_frame_dept_add)
        self.tk_button_d_add_enter = self.__tk_button_d_add_enter(self.tk_label_frame_dept_add)
        # self.tk_label_dleft_tip = self.__tk_label_dleft_tip(self.tk_label_frame_dept_add)
        self.tk_label_dmanager = self.__tk_label_dmanager(self.tk_label_frame_dept_add)
        self.tk_input_dmanager_txtin = self.__tk_input_dmanager_txtin(self.tk_label_frame_dept_add)
        self.tk_frame_dtleft_2 = self.__tk_frame_dtleft_2(self.tk_frame_top_left_D)
        self.tk_label_frame_d_add_batch = self.__tk_label_frame_d_add_batch(self.tk_frame_dtleft_2)
        self.tk_button_dexcl_file_se = self.__tk_button_dexcl_file_se(self.tk_label_frame_d_add_batch)
        # self.tk_button_d_add_batch_enter = self.__tk_button_d_add_batch_enter(self.tk_label_frame_d_add_batch)
        self.tk_button_dexcl_file_demp = self.__tk_button_dexcl_file_demp(self.tk_label_frame_d_add_batch)
        # self.tk_label_dadd_batch_tip = self.__tk_label_dadd_batch_tip(self.tk_label_frame_d_add_batch)

        # ②院系修改
        self.tk_frame_top_left_D2 = self.__tk_frame_top_left_D2(self.tk_frame_top)
        self.tk_frame_D2left_1 = self.__tk_frame_D2left_1(self.tk_frame_top_left_D2)
        self.tk_label_frame_dept_update = self.__tk_label_frame_dept_update(self.tk_frame_D2left_1)
        self.tk_label_dno_up = self.__tk_label_dno_up(self.tk_label_frame_dept_update)
        self.tk_label_dno_up_txt = self.__tk_label_dno_up_txt( self.tk_label_frame_dept_update)
        self.tk_label_dname_up = self.__tk_label_dname_up(self.tk_label_frame_dept_update)
        self.tk_input_dname_up_txtin = self.__tk_input_dname_up_txtin(self.tk_label_frame_dept_update)
        self.tk_label_dmanager_up = self.__tk_label_dmanager_up(self.tk_label_frame_dept_update)
        self.tk_button_dept_del = self.__tk_button_dept_del(self.tk_label_frame_dept_update)
        self.tk_button_dept_update = self.__tk_button_dept_update( self.tk_label_frame_dept_update)
        # self.tk_label_d2left_tip = self.__tk_label_d2left_tip(self.tk_label_frame_dept_update)
        self.tk_input_dmanager_up_txtin = self.__tk_input_dmanager_up_txtin(self.tk_label_frame_dept_update)
        self.tk_frame_d2left_2 = self.__tk_frame_d2left_2(self.tk_frame_top_left_D2)
        self.tk_table_de_find = self.__tk_table_de_find(self.tk_frame_d2left_2)
        self.tk_label_dnotxt = self.__tk_label_dnotxt(self.tk_frame_d2left_2)

        # ③院系信息表
        self.tk_frame_top_left_D3 = self.__tk_frame_top_left_D3(self.tk_frame_top)
        self.tk_frame_deinfo_left = self.__tk_frame_deinfo_left(self.tk_frame_top_left_D3)
        self.tk_label_frame_dept_info3 = self.__tk_label_frame_dept_info3(self.tk_frame_deinfo_left)
        self.tk_table_de_info_show = self.__tk_table_de_info_show(self.tk_label_frame_dept_info3)
        # self.tk_button_print_form = self.__tk_button_print_form(self.tk_label_frame_dept_info3)
        self.tk_button_export_file = self.__tk_button_export_file(self.tk_label_frame_dept_info3)

        ####### -- 院系管理 -- ########

        ####### -- 课程管理 -- ########
        self.tk_frame_top_left_C = self.__tk_frame_top_left_C(self.tk_frame_top)
        self.tk_tabs_course_i = self.__tk_tabs_course_i(self.tk_frame_top_left_C)
        self.tk_label_c_address = self.__tk_label_c_address(self.tk_tabs_course_i_0)
        self.tk_input_c_id_txtin = self.__tk_input_c_id_txtin(self.tk_tabs_course_i_0)
        self.tk_label_c_time = self.__tk_label_c_time(self.tk_tabs_course_i_0)
        self.tk_input_c_name_txtin = self.__tk_input_c_name_txtin(self.tk_tabs_course_i_0)
        self.tk_label_c_credit = self.__tk_label_c_credit(self.tk_tabs_course_i_0)
        self.tk_input_c_credit_txtin = self.__tk_input_c_credit_txtin(self.tk_tabs_course_i_0)
        self.tk_label_c_name = self.__tk_label_c_name(self.tk_tabs_course_i_0)
        self.tk_label_c_id = self.__tk_label_c_id(self.tk_tabs_course_i_0)
        self.tk_input_c_time_txtin = self.__tk_input_c_time_txtin(self.tk_tabs_course_i_0)
        self.tk_input_c_address_txtin = self.__tk_input_c_address_txtin(self.tk_tabs_course_i_0)
        self.tk_button_c_add = self.__tk_button_c_add(self.tk_tabs_course_i_0)
        self.tk_label_frame_c_batch_info = self.__tk_label_frame_c_batch_info(self.tk_tabs_course_i_0)
        self.tk_button_c_batch_add = self.__tk_button_c_batch_add(self.tk_label_frame_c_batch_info)
        self.tk_button_c_batch_demo = self.__tk_button_c_batch_demo(self.tk_label_frame_c_batch_info)
        self.tk_label_c_add_type = self.__tk_label_c_add_type(self.tk_tabs_course_i_0)
        self.tk_select_box_c_se_type = self.__tk_select_box_c_se_type(self.tk_tabs_course_i_0)

        # 修改&删除课程
        self.tk_label_c_up_id = self.__tk_label_c_up_id(self.tk_tabs_course_i_1)
        self.tk_label_c_up_name = self.__tk_label_c_up_name(self.tk_tabs_course_i_1)
        self.tk_label_c_up_credit = self.__tk_label_c_up_credit(self.tk_tabs_course_i_1)
        self.tk_label_c_up_time = self.__tk_label_c_up_time(self.tk_tabs_course_i_1)
        self.tk_label_c_up_address = self.__tk_label_c_up_address(self.tk_tabs_course_i_1)
        self.tk_label_c_up_id_txtin = self.__tk_label_c_up_id_txtin(self.tk_tabs_course_i_1)
        self.tk_input_c_up_name_txtin = self.__tk_input_c_up_name_txtin(self.tk_tabs_course_i_1)
        self.tk_input_c_up_credit_txtin = self.__tk_input_c_up_credit_txtin(self.tk_tabs_course_i_1)
        self.tk_input_c_up_time_txtin = self.__tk_input_c_up_time_txtin(self.tk_tabs_course_i_1)
        self.tk_input_c_up_address_txtin = self.__tk_input_c_up_address_txtin(self.tk_tabs_course_i_1)
        self.tk_label_c_up_type = self.__tk_label_c_up_type(self.tk_tabs_course_i_1)
        self.tk_label_cnonum = self.__tk_label_cnonum(self.tk_tabs_course_i_1)
        self.tk_label_limnum = self.__tk_label_limnum(self.tk_tabs_course_i_1)
        self.tk_input_cnonum_in = self.__tk_input_cnonum_in(self.tk_tabs_course_i_1)
        self.tk_input_limnum_in = self.__tk_input_limnum_in(self.tk_tabs_course_i_1)
        self.tk_label_c_sel_type = self.__tk_label_c_sel_type(self.tk_tabs_course_i_1)
        self.tk_select_box_c_sel_types = self.__tk_select_box_c_sel_types(self.tk_tabs_course_i_1)
        self.tk_select_box_c_se_up_type = self.__tk_select_box_c_se_up_type(self.tk_tabs_course_i_1)
        self.tk_table_c_up_show = self.__tk_table_c_up_show(self.tk_tabs_course_i_1)
        self.tk_button_c_update = self.__tk_button_c_update(self.tk_tabs_course_i_1)
        self.tk_input_c_s_txtin = self.__tk_input_c_s_txtin(self.tk_tabs_course_i_1)
        self.tk_button_c_s_find = self.__tk_button_c_s_find(self.tk_tabs_course_i_1)
        self.tk_label_c_s_txt = self.__tk_label_c_s_txt(self.tk_tabs_course_i_1)
        self.tk_button_c_del = self.__tk_button_c_del(self.tk_tabs_course_i_1)

        # 查询课程
        self.tk_table_c_info_show = self.__tk_table_c_info_show(self.tk_tabs_course_i_2)
        self.tk_label_c_show_type = self.__tk_label_c_show_type(self.tk_tabs_course_i_2)
        self.tk_select_box_c_show_types = self.__tk_select_box_c_show_types(self.tk_tabs_course_i_2)
        self.tk_button_ci_find = self.__tk_button_ci_find(self.tk_tabs_course_i_2)
        self.tk_input_ci_txtin = self.__tk_input_ci_txtin(self.tk_tabs_course_i_2)
        self.tk_label_ci_txt = self.__tk_label_ci_txt(self.tk_tabs_course_i_2)
        self.tk_button_course_exclfiles = self.__tk_button_course_exclfiles(self.tk_tabs_course_i_2)

        # 课程发布
        self.tk_select_box_course_type_se = self.__tk_select_box_course_type_se(self.tk_tabs_course_i_3)
        self.tk_label_course_type = self.__tk_label_course_type(self.tk_tabs_course_i_3)
        self.tk_button_course_start = self.__tk_button_course_start(self.tk_tabs_course_i_3)
        self.tk_label_cr_start_time = self.__tk_label_cr_start_time(self.tk_tabs_course_i_3)
        self.tk_label_cr_start_time_txt = self.__tk_label_cr_start_time_txt(self.tk_tabs_course_i_3)
        self.tk_label_cr_end_time = self.__tk_label_cr_end_time(self.tk_tabs_course_i_3)
        self.tk_label_cr_end_time_txt = self.__tk_label_cr_end_time_txt(self.tk_tabs_course_i_3)
        self.tk_radio_button_t_start = self.__tk_radio_button_t_start(self.tk_tabs_course_i_3)
        self.tk_radio_button_t_end = self.__tk_radio_button_t_end(self.tk_tabs_course_i_3)
        self.tk_button_time_set = self.__tk_button_time_set(self.tk_tabs_course_i_3)
        self.tk_input_rili = self.__tk_input_rili(self.tk_tabs_course_i_3)
        self.tk_button_course_end = self.__tk_button_course_end(self.tk_tabs_course_i_3)
        self.tk_table_course_start_show = self.__tk_table_course_start_show(self.tk_tabs_course_i_3)
        self.tk_select_box_clock_hour = self.__tk_select_box_clock_hour(self.tk_tabs_course_i_3)
        self.tk_select_box_clock_min = self.__tk_select_box_clock_min(self.tk_tabs_course_i_3)

        # 添加授课教师
        self.tk_label_tc_ctpye_t = self.__tk_label_tc_ctpye_t(self.tk_tabs_course_i_4)
        self.tk_select_box_tc_ctpye = self.__tk_select_box_tc_ctpye(self.tk_tabs_course_i_4)
        self.tk_table_tc_tableshow = self.__tk_table_tc_tableshow(self.tk_tabs_course_i_4)
        self.tk_label_ct_name = self.__tk_label_ct_name(self.tk_tabs_course_i_4)
        self.tk_label_ct_name_txt = self.__tk_label_ct_name_txt(self.tk_tabs_course_i_4)
        self.tk_label_ct_tpye_txt = self.__tk_label_ct_tpye_txt(self.tk_tabs_course_i_4)
        self.tk_label_ct_tpye = self.__tk_label_ct_tpye(self.tk_tabs_course_i_4)
        self.tk_label_ct_tno = self.__tk_label_ct_tno(self.tk_tabs_course_i_4)
        self.tk_input_ct_tno_txt = self.__tk_input_ct_tno_txt(self.tk_tabs_course_i_4)
        self.tk_label_tc_fname = self.__tk_label_tc_fname(self.tk_tabs_course_i_4)
        self.tk_input_tc_fname_txt = self.__tk_input_tc_fname_txt(self.tk_tabs_course_i_4)
        self.tk_button_tc_find = self.__tk_button_tc_find(self.tk_tabs_course_i_4)
        self.tk_button_tc_enter = self.__tk_button_tc_enter(self.tk_tabs_course_i_4)
        ####### -- 课程管理 -- ########

        ####### -- 用户管理 -- ########
        self.tk_frame_top_left_U = self.__tk_frame_top_left_U(self.tk_frame_top)
        self.tk_select_box_userno_tpye_find_se = self.__tk_select_box_userno_tpye_find_se(self.tk_frame_top_left_U)
        self.tk_label_userno_findtxt = self.__tk_label_userno_findtxt(self.tk_frame_top_left_U)
        self.tk_input_userno_findtxt_in = self.__tk_input_userno_findtxt_in(self.tk_frame_top_left_U)
        self.tk_button_userno_find = self.__tk_button_userno_find(self.tk_frame_top_left_U)
        self.tk_button_user_save_excl = self.__tk_button_user_save_excl(self.tk_frame_top_left_U)
        self.tk_label_userno_tpye_find = self.__tk_label_userno_tpye_find(self.tk_frame_top_left_U)
        self.tk_table_userno_show = self.__tk_table_userno_show(self.tk_frame_top_left_U)
        self.tk_label_userno_tpye = self.__tk_label_userno_tpye(self.tk_frame_top_left_U)
        self.tk_label_userno_tpye_txt = self.__tk_label_userno_tpye_txt(self.tk_frame_top_left_U)
        self.tk_label_userno_up = self.__tk_label_userno_up(self.tk_frame_top_left_U)
        self.tk_label_userno_upintxt = self.__tk_label_userno_upintxt(self.tk_frame_top_left_U)
        self.tk_label_userno_key = self.__tk_label_userno_key(self.tk_frame_top_left_U)
        self.tk_input_userno_key_in = self.__tk_input_userno_key_in(self.tk_frame_top_left_U)
        self.tk_input_userno_password_in = self.__tk_input_userno_password_in(self.tk_frame_top_left_U)
        self.tk_label_userno_password = self.__tk_label_userno_password(self.tk_frame_top_left_U)
        self.tk_button_userno_update = self.__tk_button_userno_update(self.tk_frame_top_left_U)
        ####### -- 用户管理 -- ########

        # 底部信息栏
        self.tk_frame_button = self.__tk_frame_button(self)
        self.tk_text_button_txt = self.__tk_text_button_txt(self.tk_frame_button)

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

    def __tk_frame_top_left(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    # 学生管理：学生添加
    def __tk_frame_left_1(self,parent):
        frame = ttk.Frame(parent,)
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.73)
        return frame
    def __tk_label_frame_student_add(self,parent):
        frame = ttk.LabelFrame(parent,text="学生添加",)
        frame.place(relx=0.01, rely=0.03, relwidth=0.97, relheight=0.95)
        return frame
    def __tk_label_sno(self,parent):
        label = ttk.Label(parent,text="学 号：",anchor="center", )
        label.place(relx=0.07, rely=0.05, relwidth=0.07, relheight=0.08)
        return label
    def __tk_input_sno_txtin(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.06, relwidth=0.21, relheight=0.06)
        return ipt
    def __tk_label_sname(self,parent):
        label = ttk.Label(parent,text="姓 名：",anchor="center", )
        label.place(relx=0.07, rely=0.14, relwidth=0.07, relheight=0.08)
        return label
    def __tk_input_sname_txtin(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.15, relwidth=0.21, relheight=0.06)
        return ipt
    def __tk_label_class(self,parent):
        label = ttk.Label(parent,text="班 级：",anchor="center", )
        label.place(relx=0.07, rely=0.24, relwidth=0.07, relheight=0.08)
        return label
    def __tk_input_class_txtin(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.25, relwidth=0.21, relheight=0.06)
        return ipt
    def __tk_label_dept(self,parent):
        label = ttk.Label(parent,text="院 系：",anchor="center", )
        label.place(relx=0.07, rely=0.34, relwidth=0.07, relheight=0.08)
        return label
    def __tk_select_box_sdept_se(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        # sql获取院系名称
        data = dept_data_get()
        data = tuple([item for sublist in data for item in sublist])
        cb['values'] = ("请选择",) + data
        cb.place(relx=0.14, rely=0.35, relwidth=0.21, relheight=0.06)
        return cb
    def __tk_label_ssex(self,parent):
        label = ttk.Label(parent,text="性 别：",anchor="center", )
        label.place(relx=0.49, rely=0.05, relwidth=0.07, relheight=0.08)
        return label
    def __tk_select_box_ssex_se(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择","男","女")
        cb.place(relx=0.56, rely=0.06, relwidth=0.21, relheight=0.06)
        return cb
    def __tk_label_sage(self,parent):
        label = ttk.Label(parent,text="年 龄：",anchor="center", )
        label.place(relx=0.49, rely=0.14, relwidth=0.07, relheight=0.08)
        return label
    def __tk_select_box_sage_se(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择","14","15","16","17","18","19","20","21","22","23","24")
        cb.place(relx=0.56, rely=0.15, relwidth=0.21, relheight=0.06)
        return cb
    def __tk_button_student_add_enter(self,parent):
        btn = ttk.Button(parent, text="添加确认", takefocus=False, command=self.button_student_add_enter)
        btn.place(relx=0.25, rely=0.77, relwidth=0.10, relheight=0.06)
        return btn
    def button_student_add_enter(self):
        print('进入添加学生操作！')
        if len(self.tk_input_sno_txtin.get()) and len(self.tk_input_sname_txtin.get()) and len(self.tk_input_class_txtin.get()) \
                and self.tk_select_box_ssex_se.get() != "请选择" and self.tk_select_box_sage_se.get() != "请选择" and self.tk_select_box_sdept_se.get() != "请选择":
            result = messagebox.askokcancel("信息添加提示", '是否确认添加？')
            if result:
                print(self.tk_input_sno_txtin.get())
                # sql增加信息
                result = student_add(self.tk_input_sno_txtin.get(), self.tk_input_sname_txtin.get(),
                                     self.tk_select_box_ssex_se.get(), self.tk_select_box_sage_se.get(),
                                     self.tk_input_class_txtin.get(), self.tk_select_box_sdept_se.get()
                                     )
                if result:
                    # 添加对应的学生账号
                    user_stduent_add(self.tk_input_sno_txtin.get(), generate_random_number(), generate_random_number())
                    # 清空信息,填写初始化
                    self.tk_input_sno_txtin.delete(0, ttk.END)
                    self.tk_input_sname_txtin.delete(0, ttk.END)
                    self.tk_input_class_txtin.delete(0, ttk.END)
                    self.tk_select_box_ssex_se.current(0)
                    self.tk_select_box_sage_se.current(0)
                    self.tk_select_box_sdept_se.current(0)
                    self.tk_frame_top_left_S.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)

                    messagebox.showinfo("添加提示", "添加成功！")
                else:
                    messagebox.showerror("错误提示", "学号重复，请重新修改！")
                    pass
            else:
                print('取消添加学生操作！')
        else:
            messagebox.showerror("信息添加提示", '所填内容不能为空！')
            pass
        pass
    def __tk_frame_left_2(self,parent):
        frame = ttk.Frame(parent,)
        frame.place(relx=0.00, rely=0.73, relwidth=1.00, relheight=0.27)
        return frame
    def __tk_label_frame_student_add_batch(self,parent):
        frame = ttk.LabelFrame(parent,text="批量处理",)
        frame.place(relx=0.01, rely=0.00, relwidth=0.97, relheight=0.93)
        return frame
    def __tk_button_excl_file_se(self, parent):
        btn = ttk.Button(parent, text="选择excl文件", takefocus=False, command=self.excl_file_se)
        btn.place(relx=0.07, rely=0.07, relwidth=0.13, relheight=0.21)
        return btn
    def excl_file_se(self):
        filename = select_file()
        # 批量写入数据到mysql
        if filename:
            result = messagebox.askokcancel("信息提示", "是否导入信息？")
            if result:
                data = batch_add(filename)
                i = 1
                j = 0
                row = ()
                for data_item in data:
                    result = student_add(data_item[0], data_item[1], data_item[2],
                                         data_item[3], data_item[4], data_item[5],
                                         )
                    i += 1
                    if result is True:
                        # 添加对应的学生账号
                        user_stduent_add(data_item[0], generate_random_number(),
                                         generate_random_number())
                    if result is False:
                        j = i
                        row += (j,)
                if j != 0:
                    messagebox.showerror("信息提示", f"文件中的{row}行数据导入失败，学号已存在或数据存在错误！")
                else:
                    messagebox.showinfo("信息导入提示", '学生信息导入成功！')
                    print("信息导入成功！")
            else:
                print("信息导入取消！")
        pass
    def __tk_button_excl_file_demp(self, parent):
        btn = ttk.Button(parent, text="导出文档模板", takefocus=False, command=self.excl_file_demp)
        btn.place(relx=0.07, rely=0.43, relwidth=0.13, relheight=0.21)
        return btn
    def excl_file_demp(self):
        save_file("学生信息文件填写格式模板", None, student_info_add_low(), True)
        pass
    # ②学生修改
    def __tk_frame_top_left_S2(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_frame_s2left_1(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.30, relwidth=1.00, relheight=0.70)
        return frame

    def __tk_label_frame_student_update(self, parent):
        frame = ttk.LabelFrame(parent, text="学生信息修改", )
        frame.place(relx=0.01, rely=0.03, relwidth=0.97, relheight=0.96)
        return frame

    def __tk_label_sno_up(self, parent):
        label = ttk.Label(parent, text="学 号：", anchor="center", )
        label.place(relx=0.07, rely=0.05, relwidth=0.07, relheight=0.08)
        return label

    def __tk_label_sno_up_txtin(self,parent):
        label = ttk.Label(parent,text="",anchor="w", )
        label.place(relx=0.14, rely=0.06, relwidth=0.21, relheight=0.06)
        return label

    def __tk_label_sname_up(self, parent):
        label = ttk.Label(parent, text="姓 名：", anchor="center", )
        label.place(relx=0.07, rely=0.15, relwidth=0.07, relheight=0.08)
        return label

    def __tk_input_sname_up_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.16, relwidth=0.21, relheight=0.06)
        return ipt

    def __tk_label_sdept_up(self, parent):
        label = ttk.Label(parent, text="院 系：", anchor="center", )
        label.place(relx=0.07, rely=0.34, relwidth=0.07, relheight=0.08)
        return label

    def __tk_select_box_sdept_up_se(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        # sql获取院系名称
        data = dept_data_get()
        data = tuple([item for sublist in data for item in sublist])
        cb['values'] = ("请选择",) + data
        cb.place(relx=0.14, rely=0.35, relwidth=0.21, relheight=0.06)
        return cb

    def __tk_label_ssex_up(self, parent):
        label = ttk.Label(parent, text="性 别：", anchor="center", )
        label.place(relx=0.49, rely=0.05, relwidth=0.07, relheight=0.08)
        return label

    def __tk_select_box_ssex_up_se(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择", "男", "女")
        cb.place(relx=0.56, rely=0.06, relwidth=0.21, relheight=0.06)
        return cb

    def __tk_label_sage_up(self, parent):
        label = ttk.Label(parent, text="年 龄：", anchor="center", )
        label.place(relx=0.49, rely=0.16, relwidth=0.07, relheight=0.06)
        return label

    def __tk_select_box_sage_up_se(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24")
        cb.place(relx=0.56, rely=0.16, relwidth=0.21, relheight=0.06)
        return cb

    def __tk_button_student_update_enter(self, parent):
        btn = ttk.Button(parent, text="修改", takefocus=False, command=self.button_student_update_enter)
        btn.place(relx=0.07, rely=0.74, relwidth=0.07, relheight=0.06)
        return btn
    def button_student_update_enter(self):
        self.tk_button_student_del_enter.configure(state='disabled')
        if not (len(self.tk_label_sno_up_txtin.cget("text")) and len(self.tk_input_sname_up_txtin.get())
                and self.tk_select_box_ssex_up_se.get() != "请选择" and self.tk_select_box_sage_up_se.get() != "请选择"
                and len(self.tk_input_class_up_txtin.get()) and self.tk_select_box_sdept_up_se.get() != "请选择"):
            messagebox.showerror("信息提示", '请选择要进行修改的学生信息或修改信息欠缺！')
            pass
        else:
            result = messagebox.askokcancel("信息修改提示", '是否修改信息？')
            if result:
                student_update(self.tk_label_sno_up_txtin.cget("text"), self.tk_input_sname_up_txtin.get(),
                               self.tk_select_box_ssex_up_se.get(), self.tk_select_box_sage_up_se.get(),
                               self.tk_input_class_up_txtin.get(), self.tk_select_box_sdept_up_se.get(),
                               )
                # 统计课程的学生总数，course表从sct表进行统计并更新
                self.tk_input_sno_findin.delete(0, ttk.END)
                self.tk_label_sno_up_txtin.configure(text="")
                self.tk_input_sname_up_txtin.delete(0, ttk.END)
                self.tk_input_class_up_txtin.delete(0, ttk.END)
                self.tk_select_box_ssex_up_se.current(0)
                self.tk_select_box_sage_up_se.current(0)
                self.tk_select_box_sdept_up_se.current(0)

                self.tk_frame_top_left_S2.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
                data = st_find()
                for item in self.tk_table_st_find.get_children():
                    self.tk_table_st_find.delete(item)
                for col in data:
                    self.tk_table_st_find.insert("", "end", values=tuple(col))
            else:
                print('取消修改学生信息！')
        self.tk_button_student_del_enter.configure(state='normal')
        pass

    def __tk_button_student_del_enter(self,parent):
        btn = ttk.Button(parent, text="删除", takefocus=False, command=self.button_student_del_enter)
        btn.place(relx=0.28, rely=0.74, relwidth=0.07, relheight=0.06)
        return btn
    def button_student_del_enter(self):
        self.tk_button_student_update_enter.configure(state='disabled')
        if not (len(self.tk_label_sno_up_txtin.cget("text")) and len(self.tk_input_sname_up_txtin.get())
                and self.tk_select_box_ssex_up_se.get() != "请选择" and self.tk_select_box_sage_up_se.get() != "请选择"
                and len(self.tk_input_class_up_txtin.get()) and self.tk_select_box_sdept_up_se.get() != "请选择"):
            messagebox.showerror("信息提示", '请选择要进行删除的学生信息或填写的删除信息欠缺！')
            pass
        else:
            result = messagebox.askokcancel("信息删除提示", '是否删除信息？')
            if result:
                student_info_del(self.tk_label_sno_up_txtin.cget("text"))
                # 删除对应的学生账号
                user_stduent_del(self.tk_label_sno_up_txtin.cget("text"))

                # 统计课程的学生总数，course表从sct表进行统计并更新
                self.tk_input_sno_findin.delete(0, ttk.END)
                self.tk_label_sno_up_txtin.configure(text="")
                self.tk_input_sname_up_txtin.delete(0, ttk.END)
                self.tk_input_class_up_txtin.delete(0, ttk.END)
                self.tk_select_box_ssex_up_se.current(0)
                self.tk_select_box_sage_up_se.current(0)
                self.tk_select_box_sdept_up_se.current(0)

                self.tk_frame_top_left_S2.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
                data = st_find()
                for item in self.tk_table_st_find.get_children():
                    self.tk_table_st_find.delete(item)
                for col in data:
                    self.tk_table_st_find.insert("", "end", values=tuple(col))
                messagebox.showinfo("信息提示", "删除成功！")
            else:
                print('取消删除学生信息！')
        self.tk_button_student_update_enter.configure(state='normal')
        pass
    def __tk_label_class_up(self, parent):
        label = ttk.Label(parent, text="班 级：", anchor="center", )
        label.place(relx=0.07, rely=0.24, relwidth=0.07, relheight=0.08)
        return label

    def __tk_input_class_up_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.25, relwidth=0.21, relheight=0.06)
        return ipt

    def __tk_frame_s2left_2(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.30)
        return frame

    def __tk_table_st_find(self, parent):
        # 表头字段 表头宽度
        columns = {"学号": 143, "姓名": 143, "性别": 71, "年龄": 71, "班级": 143, "所属院系": 143}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.bind('<<TreeviewSelect>>', self.st_find_select)
        tk_table.place(relx=0.01, rely=0.290, relwidth=0.97, relheight=0.71)
        self.create_bar(parent, tk_table, True, False, 5, 49.5, 720, 115, 740, 165)
        return tk_table
    def st_find_select(self, event):
        selection = event.widget.selection()
        if selection:
            # 获取选中的行索引
            index = selection[0]
            # 获取行中的数据
            Tc = event.widget.set(index)
            print(f'{Tc}')
            # 刷新
            self.tk_input_sno_findin.delete(0, ttk.END)
            self.tk_label_sno_up_txtin.configure(text="")
            self.tk_input_sname_up_txtin.delete(0, ttk.END)
            self.tk_select_box_ssex_up_se.current(0)
            self.tk_select_box_sage_up_se.current(0)
            self.tk_input_class_up_txtin.delete(0, ttk.END)
            self.tk_select_box_sdept_up_se.current(0)

            # 填写
            self.tk_label_sno_up_txtin.configure(text=Tc['学号'])
            self.tk_input_sname_up_txtin.insert(0, Tc['姓名'])
            self.tk_input_class_up_txtin.insert(0, Tc['班级'])
            # 性别
            data = ('请选择', '男', '女')
            ssex_index = data.index(Tc['性别'])
            self.tk_select_box_ssex_up_se.current(ssex_index)
            # 年龄14-24 : 1-11
            sage_index = int(Tc['年龄']) - 14 + 1
            self.tk_select_box_sage_up_se.current(sage_index)
            # 院系
            data = dept_data_get()
            data = tuple([item for sublist in data for item in sublist])
            data = ("请选择",) + data
            print(data)
            print(Tc['所属院系'])
            if Tc['所属院系'] != "None":
                dept_index = data.index(Tc['所属院系'])
                print(dept_index)
                self.tk_select_box_sdept_up_se.current(dept_index)
        pass
    def __tk_label_snotxt(self, parent):
        label = ttk.Label(parent, text="请输入学号进行查找并选择：", anchor="center", )
        label.place(relx=0.01, rely=0.06, relwidth=0.23, relheight=0.18)
        return label

    def __tk_input_sno_findin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.24, rely=0.08, relwidth=0.20, relheight=0.14)
        return ipt

    def __tk_button_snofind_enter(self, parent):
        btn = ttk.Button(parent, text="查找", takefocus=False, command=self.button_snofind_enter)
        btn.place(relx=0.45, rely=0.08, relwidth=0.07, relheight=0.14)
        return btn
    def button_snofind_enter(self):
        # 查询学生信息是否存在
        print(self.tk_input_sno_findin.get())
        # 查询数据
        sdata = student_find_sno(self.tk_input_sno_findin.get())

        if sdata:
            print(sdata)
            # 刷新
            self.tk_label_sno_up_txtin.configure(text="")
            self.tk_input_sname_up_txtin.delete(0, ttk.END)
            self.tk_select_box_ssex_up_se.current(0)
            self.tk_select_box_sage_up_se.current(0)
            self.tk_input_class_up_txtin.delete(0, ttk.END)
            self.tk_select_box_sdept_up_se.current(0)
            # 填写
            self.tk_label_sno_up_txtin.configure(text=sdata[0])
            self.tk_input_sname_up_txtin.insert(0, sdata[1])
            self.tk_input_class_up_txtin.insert(0, sdata[4])
            # 性别
            data = ('请选择', '男', '女')
            ssex_index = data.index(sdata[2])
            self.tk_select_box_ssex_up_se.current(ssex_index)
            # 年龄14-24 : 1-11
            sage_index = int(sdata[3]) - 14 + 1
            self.tk_select_box_sage_up_se.current(sage_index)
            # 院系
            data = dept_data_get()
            data = tuple([item for sublist in data for item in sublist])
            data = ("请选择",) + data
            print(data)
            if sdata[5] != "None":
                dept_index = data.index(sdata[5])
                print(dept_index)
                self.tk_select_box_sdept_up_se.current(dept_index)
                messagebox.showinfo("信息提示", '查找成功！')
                pass
        else:
            messagebox.showerror("信息提示", '学生信息不存在，请重新输入信息！')
            pass
        pass

    # ③学生信息表
    def __tk_frame_top_left_S3(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_frame_stinfo_left(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=1.00)
        return frame

    def __tk_label_frame_student_info3(self, parent):
        frame = ttk.LabelFrame(parent, text="学生信息", )
        frame.place(relx=0.01, rely=0.00, relwidth=0.99, relheight=0.98)
        return frame

    def __tk_table_st_info_show(self, parent):
        # 表头字段 表头宽度
        columns = {"学号": 143, "姓名": 143, "性别": 71, "年龄": 71, "班级": 143, "所属院系": 143}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.005, rely=0.07, relwidth=0.99, relheight=0.91)
        self.create_bar(parent, tk_table, True, False, 5.5, 38.5, 720, 490, 730, 540)
        return tk_table
    def __tk_button_student_export_file_enter(self,parent):
        btn = ttk.Button(parent, text="导出表格", takefocus=False, command=self.button_student_export_file_enter)
        btn.place(relx=0.915, rely=0.01, relwidth=0.08, relheight=0.04)
        return btn
    def button_student_export_file_enter(self):
        save_file("学生信息表", student_info_add_low(True), student_info_add_low(False))
        pass

    def __tk_label_st_info_name(self, parent):
        label = ttk.Label(parent, text="姓 名：", anchor="center", )
        label.place(relx=0.52, rely=0.01, relwidth=0.07, relheight=0.04)
        return label

    def __tk_input_st_info_find_name(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.59, rely=0.01, relwidth=0.14, relheight=0.04)
        return ipt

    def __tk_button_st_info_enter(self, parent):
        btn = ttk.Button(parent, text="查找", takefocus=False, command=self.button_st_info_enter)
        btn.place(relx=0.73, rely=0.01, relwidth=0.07, relheight=0.04)
        return btn
    def button_st_info_enter(self):
        # 查询学生信息是否存在
        sdata = student_find_name(self.tk_input_st_info_find_name.get())
        print(sdata)
        if sdata:
            for item in self.tk_table_st_info_show.get_children():
                self.tk_table_st_info_show.delete(item)
            for col in sdata:
                self.tk_table_st_info_show.insert("", "end", values=tuple(col))
            pass
        else:
            data = student_info_add_low(True)
            for item in self.tk_table_st_info_show.get_children():
                self.tk_table_st_info_show.delete(item)
            for col in data:
                self.tk_table_st_info_show.insert("", "end", values=tuple(col))
            # messagebox.showerror("信息提示", '学生信息不存在，请重新输入信息！')
            pass
        pass

    ########## 教工管理 ###########
    # ①教工添加--def
    def __tk_frame_tleft_1(self,parent):
        frame = ttk.Frame(parent,)
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.73)
        return frame
    def __tk_label_frame_teacher_add(self,parent):
        frame = ttk.LabelFrame(parent,text="教工添加",)
        frame.place(relx=0.01, rely=0.03, relwidth=0.97, relheight=0.95)
        return frame
    def __tk_label_tno(self,parent):
        label = ttk.Label(parent,text="工 号：",anchor="center", )
        label.place(relx=0.07, rely=0.05, relwidth=0.07, relheight=0.08)
        return label
    def __tk_input_tno_txtin(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.06, relwidth=0.21, relheight=0.06)
        return ipt
    def __tk_label_tname(self,parent):
        label = ttk.Label(parent,text="姓 名：",anchor="center", )
        label.place(relx=0.07, rely=0.14, relwidth=0.07, relheight=0.08)
        return label
    def __tk_input_tname_add_txtin(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.15, relwidth=0.21, relheight=0.06)
        return ipt
    def __tk_input_tname_txtin(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.14, relwidth=0.21, relheight=0.08)
        return ipt
    def __tk_label_tdept(self,parent):
        label = ttk.Label(parent,text="院 系：",anchor="center", )
        label.place(relx=0.07, rely=0.42, relwidth=0.07, relheight=0.08)
        return label
    def __tk_select_box_tdept_se(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        # sql获取院系名称
        data = dept_data_get()
        data = tuple([item for sublist in data for item in sublist])
        cb['values'] = ("请选择",) + data
        cb.place(relx=0.14, rely=0.43, relwidth=0.21, relheight=0.06)
        return cb
    def __tk_label_tsex(self,parent):
        label = ttk.Label(parent,text="性 别：",anchor="center", )
        label.place(relx=0.49, rely=0.05, relwidth=0.07, relheight=0.08)
        return label
    def __tk_select_box_tsex_se(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择","男","女")
        cb.place(relx=0.56, rely=0.06, relwidth=0.21, relheight=0.06)
        return cb
    def __tk_label_tage(self,parent):
        label = ttk.Label(parent,text="年 龄：",anchor="center", )
        label.place(relx=0.49, rely=0.14, relwidth=0.07, relheight=0.08)
        return label
    def __tk_select_box_tage_se(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
        cb.place(relx=0.56, rely=0.15, relwidth=0.21, relheight=0.06)
        return cb
    def __tk_button_teacher_add_enter(self,parent):
        btn = ttk.Button(parent, text="添加确认", takefocus=False, command=self.button_teacher_add_enter)
        btn.place(relx=0.25, rely=0.77, relwidth=0.10, relheight=0.06)
        return btn
    def button_teacher_add_enter(self):
        print('进入添加教工操作！')
        if len(self.tk_input_tno_txtin.get()) and len(self.tk_input_tname_add_txtin.get()) \
                and self.tk_select_box_tsex_se.get() != "请选择" and self.tk_select_box_tage_se.get() != "请选择" \
                and self.tk_select_box_teb_se.get() != "请选择" and self.tk_select_box_tpt_se.get() != "请选择" \
                and self.tk_select_box_tdept_se.get() != "请选择":
            result = messagebox.askokcancel("信息添加提示", '是否确认添加？')
            if result:
                # sql增加信息
                result = teacher_add(self.tk_input_tno_txtin.get(), self.tk_input_tname_add_txtin.get(),
                                     self.tk_select_box_tsex_se.get(), self.tk_select_box_tage_se.get(),
                                     self.tk_select_box_teb_se.get(), self.tk_select_box_tpt_se.get(),
                                     self.tk_select_box_tdept_se.get(),
                                     )
                if result:
                    # 添加对应的教工账号
                    user_teacher_add(self.tk_input_tno_txtin.get(), generate_random_number(), generate_random_number())
                    # 清空信息,填写初始化
                    data = dept_data_get()
                    data = tuple([item for sublist in data for item in sublist])
                    self.tk_select_box_tdept_se['values'] = ("请选择",) + data
                    self.tk_input_tno_txtin.delete(0, ttk.END)
                    self.tk_input_tname_add_txtin.delete(0, ttk.END)
                    self.tk_select_box_tsex_se.current(0)
                    self.tk_select_box_tage_se.current(0)
                    self.tk_select_box_teb_se.current(0)
                    self.tk_select_box_tpt_se.current(0)
                    self.tk_select_box_tdept_se.current(0)
                    self.tk_input_dno_txtin.delete(0, ttk.END)
                    self.tk_input_dname_txtin.delete(0, ttk.END)
                    self.tk_input_dmanager_txtin.delete(0, ttk.END)
                    messagebox.showinfo("添加提示", "添加成功！")
                else:
                    messagebox.showerror("错误提示", "工号重复，请重新修改！")
            else:
                print('取消添加教工操作！')
        else:
            messagebox.showerror("信息添加提示", '所填内容不能为空！')
            pass
        pass
    def __tk_label_teb(self,parent):
        label = ttk.Label(parent,text="学 历：",anchor="center", )
        label.place(relx=0.07, rely=0.24, relwidth=0.07, relheight=0.08)
        return label
    def __tk_label_tpt(self,parent):
        label = ttk.Label(parent,text="职 称：",anchor="center", )
        label.place(relx=0.07, rely=0.33, relwidth=0.07, relheight=0.08)
        return label
    def __tk_select_box_teb_se(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择","学士","硕士","博士","博士后")
        cb.place(relx=0.14, rely=0.25, relwidth=0.21, relheight=0.06)
        return cb
    def __tk_select_box_tpt_se(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择","助教","讲师","副教授","教授")
        cb.place(relx=0.14, rely=0.34, relwidth=0.21, relheight=0.06)
        return cb
    def __tk_frame_tleft_2(self,parent):
        frame = ttk.Frame(parent,)
        frame.place(relx=0.00, rely=0.73, relwidth=1.00, relheight=0.27)
        return frame
    def __tk_label_frame_teacher_add_batch(self,parent):
        frame = ttk.LabelFrame(parent,text="批量处理",)
        frame.place(relx=0.01, rely=0.00, relwidth=0.97, relheight=0.93)
        return frame
    def __tk_button_texcl_file_se(self, parent):
        btn = ttk.Button(parent, text="选择excl文件", takefocus=False, command=self.texcl_file_se)
        btn.place(relx=0.07, rely=0.07, relwidth=0.13, relheight=0.21)
        return btn
    def texcl_file_se(self):
        filename = select_file()
        # 批量写入数据到mysql
        if filename:
            result = messagebox.askokcancel("信息提示", "是否导入信息？")
            if result:
                data = batch_add(filename)
                i = 1
                j = 0

                row = ()
                for data_item in data:
                    i += 1
                    resultS = teacher_add(data_item[0], data_item[1], data_item[2],
                                          data_item[3], data_item[4], data_item[5],
                                          data_item[6],
                                          )
                    if resultS is True:
                        # 添加对应的教工账号
                        user_teacher_add(data_item[0], generate_random_number(),
                                         generate_random_number())
                    else:
                        j = i
                        row += (j,)
                if j != 0:
                    messagebox.showerror("信息提示", f"文件中的{row}行数据导入失败，教工号已存在或数据存在错误！")
                else:
                    messagebox.showinfo("信息导入提示", '教工信息导入成功！')
                    print("信息导入成功！")
            else:
                print("信息导入取消！")
        pass
    def __tk_button_texcl_file_demp(self, parent):
        btn = ttk.Button(parent, text="导出文档模板", takefocus=False, command=self.texcl_file_demp)
        btn.place(relx=0.07, rely=0.43, relwidth=0.13, relheight=0.21)
        return btn
    def texcl_file_demp(self):
        save_file("教工信息文件填写格式模板", None, teacher_info_add_low(), True)
        pass
    def __tk_label_teadd_batch_tip(self, parent):
        label = ttk.Label(parent,text="信息提示", anchor="center", )
        label.place(relx=0.07, rely=0.50, relwidth=0.58, relheight=0.21)
        return label

    # ②教工修改
    def __tk_frame_top_left_T2(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_frame_t2left_1(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.30, relwidth=1.00, relheight=0.70)
        return frame

    def __tk_label_frame_teacher_update(self, parent):
        frame = ttk.LabelFrame(parent, text="教工信息修改", )
        frame.place(relx=0.01, rely=0.03, relwidth=0.97, relheight=0.96)
        return frame

    def __tk_label_tno_up(self, parent):
        label = ttk.Label(parent, text="工 号：", anchor="center", )
        label.place(relx=0.07, rely=0.05, relwidth=0.07, relheight=0.08)
        return label

    def __tk_label_tno_up_txtin(self, parent):
        label = ttk.Label(parent, text="", anchor="center", )
        label.place(relx=0.14, rely=0.06, relwidth=0.21, relheight=0.06)
        return label

    def __tk_label_tname_up(self, parent):
        label = ttk.Label(parent, text="姓 名：", anchor="center", )
        label.place(relx=0.07, rely=0.15, relwidth=0.07, relheight=0.08)
        return label

    def __tk_input_tname_txtin_up(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.16, relwidth=0.21, relheight=0.06)
        return ipt

    def __tk_label_tdept_up(self, parent):
        label = ttk.Label(parent, text="院 系：", anchor="center", )
        label.place(relx=0.07, rely=0.43, relwidth=0.07, relheight=0.08)
        return label

    def __tk_select_box_tdept_up_se(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        data = dept_data_get()
        data = tuple([item for sublist in data for item in sublist])
        cb['values'] = ("请选择",) + data
        cb.place(relx=0.14, rely=0.44, relwidth=0.21, relheight=0.06)
        return cb

    def __tk_label_tsex_up(self, parent):
        label = ttk.Label(parent, text="性 别：", anchor="center", )
        label.place(relx=0.49, rely=0.05, relwidth=0.07, relheight=0.08)
        return label

    def __tk_select_box_tsex_up_se(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择", "男", "女")
        cb.place(relx=0.56, rely=0.06, relwidth=0.21, relheight=0.06)
        return cb

    def __tk_label_tage_up(self, parent):
        label = ttk.Label(parent, text="年 龄：", anchor="center", )
        label.place(relx=0.49, rely=0.15, relwidth=0.07, relheight=0.08)
        return label

    def __tk_select_box_tage_up_se(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择", "24", "25", "26", "27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37",
                        "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50", "51", "52", "53",
                        "54", "55", "56", "57", "58", "59", "60")
        cb.place(relx=0.56, rely=0.16, relwidth=0.21, relheight=0.06)
        return cb

    def __tk_button_teacher_update_enter(self, parent):
        btn = ttk.Button(parent, text="修改", takefocus=False, command=self.button_teacher_update_enter)
        btn.place(relx=0.07, rely=0.69, relwidth=0.07, relheight=0.06)
        return btn

    def button_teacher_update_enter(self):
        global Ctno
        self.tk_button_teacher_del_enter.configure(state='disabled')
        if not (len(self.tk_label_tno_up_txtin.cget("text")) and len(self.tk_input_tname_up_txtin.get())
                and self.tk_select_box_tsex_up_se.get() != "请选择" and self.tk_select_box_tage_up_se.get() != "请选择"
                and self.tk_select_box_teb_up_se.get() != "请选择" and self.tk_select_box_tpt_up_se.get() != "请选择"
                and self.tk_select_box_tdept_up_se.get() != "请选择"):
            messagebox.showerror("信息提示", '请选择要进行修改的教工信息或填写的修改信息欠缺！')
            pass
        else:
            Ctno = self.tk_label_tno_up_txtin.cget("text")
            result = messagebox.askokcancel("信息修改提示", '是否修改信息？')
            if result:
                print("信息修改中")
                teacher_update(self.tk_label_tno_up_txtin.cget("text"), self.tk_input_tname_up_txtin.get(),
                               self.tk_select_box_tsex_up_se.get(), self.tk_select_box_tage_up_se.get(),
                               self.tk_select_box_teb_up_se.get(), self.tk_select_box_tpt_up_se.get(),
                               self.tk_select_box_tdept_up_se.get(), )
                # !@#
                data = teacher_info_showall()
                for item in self.tk_table_te_find.get_children():
                    self.tk_table_te_find.delete(item)
                for col in data:
                    self.tk_table_te_find.insert("", "end", values=tuple(col))
                # 初始化填写信息
                self.tk_input_tno_findin.delete(0, ttk.END)
                self.tk_label_tno_up_txtin.configure(text="")
                self.tk_input_tname_up_txtin.delete(0, ttk.END)
                self.tk_select_box_tsex_up_se.current(0)
                self.tk_select_box_tage_up_se.current(0)
                self.tk_select_box_teb_up_se.current(0)
                self.tk_select_box_tpt_up_se.current(0)
                self.tk_select_box_tdept_up_se.current(0)
                data = dept_data_get()
                data = tuple([item for sublist in data for item in sublist])
                self.tk_select_box_tdept_up_se['values'] = ("请选择",) + data
                print("信息修改成功！")
                # !@#
            else:
                print('取消修改教工信息！')
        self.tk_button_teacher_del_enter.configure(state='normal')
        pass

    def __tk_button_teacher_del_enter(self,parent):
        btn = ttk.Button(parent, text="删除", takefocus=False, command=self.button_teacher_del_enter)
        btn.place(relx=0.28, rely=0.69, relwidth=0.07, relheight=0.06)
        return btn
    def button_teacher_del_enter(self):
        global Ctno

        self.tk_button_teacher_update_enter.configure(state='disabled')
        if not (len(self.tk_label_tno_up_txtin.cget("text")) and len(self.tk_input_tname_up_txtin.get())
                and self.tk_select_box_tsex_up_se.get() != "请选择" and self.tk_select_box_tage_up_se.get() != "请选择"
                and self.tk_select_box_teb_up_se.get() != "请选择" and self.tk_select_box_tpt_up_se.get() != "请选择"
                and self.tk_select_box_tdept_up_se.get() != "请选择"):
            messagebox.showerror("信息提示", '请选择要进行删除的教工信息或填写的删除信息欠缺！')
            pass
        else:
            Ctno = self.tk_label_tno_up_txtin.cget("text")
            # 教工编号tno，查看教师当前是否存在授课
            data = teacher_course_find(Ctno)
            if data:
                messagebox.showinfo("信息删除提示", '当前教师存在授课课程！\n请对指定课程更新授课教师！')
                Tinc()
            else:
                result = messagebox.askokcancel("信息删除提示", '是否删除信息？')
                if result:
                    # 删除教工信息
                    teacher_info_del(self.tk_label_tno_up_txtin.cget("text"))
                    # 删除对应的教工账号
                    user_teacher_del(self.tk_label_tno_up_txtin.cget("text"))
                    # !@#
                    data = teacher_info_showall()
                    for item in self.tk_table_te_find.get_children():
                        self.tk_table_te_find.delete(item)
                    for col in data:
                        self.tk_table_te_find.insert("", "end", values=tuple(col))
                    # 初始化填写信息
                    self.tk_input_tno_findin.delete(0, ttk.END)
                    self.tk_label_tno_up_txtin.configure(text="")
                    self.tk_input_tname_up_txtin.delete(0, ttk.END)
                    self.tk_select_box_tsex_up_se.current(0)
                    self.tk_select_box_tage_up_se.current(0)
                    self.tk_select_box_teb_up_se.current(0)
                    self.tk_select_box_tpt_up_se.current(0)
                    self.tk_select_box_tdept_up_se.current(0)

                    data = dept_data_get()
                    data = tuple([item for sublist in data for item in sublist])
                    self.tk_select_box_tdept_up_se['values'] = ("请选择",) + data
                    # !@#
                    messagebox.showinfo("信息提示", "删除成功！")
                else:
                    print('取消删除教工信息！')
        self.tk_button_teacher_update_enter.configure(state='normal')
        pass

    def __tk_label_t2left_tip(self, parent):
        label = ttk.Label(parent, text="信息提示", anchor="center", )
        label.place(relx=0.07, rely=0.81, relwidth=0.58, relheight=0.08)
        return label

    def __tk_label_teb_up(self, parent):
        label = ttk.Label(parent, text="学 历：", anchor="center", )
        label.place(relx=0.07, rely=0.24, relwidth=0.07, relheight=0.08)
        return label

    def __tk_label_tpt_up(self, parent):
        label = ttk.Label(parent, text="职 称：", anchor="center", )
        label.place(relx=0.07, rely=0.34, relwidth=0.07, relheight=0.08)
        return label

    def __tk_select_box_teb_up_se(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择", "学士", "硕士", "博士", "博士后")
        cb.place(relx=0.14, rely=0.25, relwidth=0.21, relheight=0.06)
        return cb

    def __tk_select_box_tpt_up_se(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择", "助教", "讲师", "副教授", "教授")
        cb.place(relx=0.14, rely=0.35, relwidth=0.21, relheight=0.06)
        return cb

    def __tk_frame_t2left_2(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.30)
        return frame

    def __tk_table_te_find(self, parent):
        # 表头字段 表头宽度
        columns = {"教工号": 103, "姓名": 103, "性别": 71, "年龄": 71, "学历": 113, "职称": 113, "所属院系":140}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.bind('<<TreeviewSelect>>', self.tc_find_select)
        tk_table.place(relx=0.01, rely=0.30, relwidth=0.97, relheight=0.70)
        self.create_bar(parent, tk_table, True, False, 4.3, 50, 720, 114, 740, 165)
        return tk_table
    def tc_find_select(self, event):
        selection = event.widget.selection()
        if selection:
            # 获取选中的行索引
            index = selection[0]
            # 获取行中的数据
            Tc = event.widget.set(index)
            print(f'{Tc}')
            # 刷新
            self.tk_label_tno_up_txtin.configure(text="")
            self.tk_input_tname_up_txtin.delete(0, ttk.END)
            self.tk_select_box_tsex_up_se.current(0)
            self.tk_select_box_tage_up_se.current(0)
            self.tk_select_box_teb_up_se.current(0)
            self.tk_select_box_tpt_up_se.current(0)
            self.tk_select_box_tdept_up_se.current(0)
            # 填写
            self.tk_label_tno_up_txtin.configure(text=Tc['教工号'])
            self.tk_input_tname_up_txtin.insert(0, Tc['姓名'])
            # 性别
            data = ('请选择', '男', '女')
            tsex_index = data.index(Tc['性别'])
            self.tk_select_box_tsex_up_se.current(tsex_index)
            # 年龄24-60 : 1-37
            tage_index = int(Tc['年龄']) - 24 + 1
            self.tk_select_box_tage_up_se.current(tage_index)
            # 学历
            data = ('请选择', '学士', '硕士', '博士', '博士后')
            teb_index = data.index(Tc['学历'])
            self.tk_select_box_teb_up_se.current(teb_index)
            # 职称
            data = ('请选择', '助教', '讲师', '副教授', '教授')
            tpt_index = data.index(Tc['职称'])
            self.tk_select_box_tpt_up_se.current(tpt_index)
            # 院系
            data = dept_data_get()
            data = tuple([item for sublist in data for item in sublist])
            data = ("请选择",) + data
            print(data)
            print(Tc['所属院系'])
            if Tc['所属院系'] != "None":
                dept_index = data.index(Tc['所属院系'])
                print(dept_index)
                self.tk_select_box_tdept_up_se.current(dept_index)
        pass
    def __tk_label_tnotxt(self, parent):
        label = ttk.Label(parent, text="请输入教工号进行查找并选择：", anchor="center", )
        label.place(relx=0.01, rely=0.06, relwidth=0.23, relheight=0.18)
        return label

    def __tk_input_tno_findin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.24, rely=0.08, relwidth=0.20, relheight=0.14)
        return ipt

    def __tk_button_tnofind_enter(self, parent):
        btn = ttk.Button(parent, text="查找", takefocus=False, command=self.button_tnofind_enter)
        btn.place(relx=0.45, rely=0.08, relwidth=0.07, relheight=0.14)
        return btn

    def button_tnofind_enter(self):
        # 查询教师信息是否存在
        print(self.tk_input_tno_findin.get())
        # 查询数据
        tdata = teacher_find_one(self.tk_input_tno_findin.get())
        print(tdata)
        if tdata:
            # 刷新
            self.tk_label_tno_up_txtin.configure(text="")
            self.tk_input_tname_up_txtin.delete(0, ttk.END)
            self.tk_select_box_tsex_up_se.current(0)
            self.tk_select_box_tage_up_se.current(0)
            self.tk_select_box_teb_up_se.current(0)
            self.tk_select_box_tpt_up_se.current(0)
            self.tk_select_box_tdept_up_se.current(0)
            # 填写
            self.tk_label_tno_up_txtin.configure(text=tdata[0])
            self.tk_input_tname_up_txtin.insert(0, tdata[1])
            # 性别
            data = ('请选择', '男', '女')
            tsex_index = data.index(tdata[2])
            self.tk_select_box_tsex_up_se.current(tsex_index)
            # 年龄24-60 : 1-37
            tage_index = int(tdata[3]) - 24 + 1
            self.tk_select_box_tage_up_se.current(tage_index)
            # 学历
            data = ('请选择', '学士', '硕士', '博士', '博士后')
            teb_index = data.index(tdata[4])
            self.tk_select_box_teb_up_se.current(teb_index)
            # 职称
            data = ('请选择', '助教', '讲师', '副教授', '教授')
            tpt_index = data.index(tdata[5])
            self.tk_select_box_tpt_up_se.current(tpt_index)
            # 院系
            data = dept_data_get()
            data = tuple([item for sublist in data for item in sublist])
            data = ("请选择",) + data
            dept_index = data.index(tdata[6])
            print(dept_index)
            self.tk_select_box_tdept_up_se.current(dept_index)
            messagebox.showinfo("信息提示", '查找成功！')
            pass
        else:
            messagebox.showerror("信息提示", '教工信息不存在，请重新输入信息！')
            pass
        pass

    # ③教工信息表
    def __tk_frame_top_left_T3(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_frame_seinfo_left(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=1.00)
        return frame

    def __tk_label_frame_teacher_info3(self, parent):
        frame = ttk.LabelFrame(parent, text="教工信息", )
        frame.place(relx=0.01, rely=0.00, relwidth=0.99, relheight=0.98)
        return frame

    def __tk_table_se_info_show(self, parent):
        # 表头字段 表头宽度
        columns = {"教工号": 103, "姓名": 103, "性别": 71, "年龄": 71, "学历": 113, "职称": 113, "所属院系":140}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.005, rely=0.07, relwidth=0.99, relheight=0.91)
        self.create_bar(parent, tk_table, True, False, 5.5, 39, 720, 490, 730, 542)
        return tk_table

    def __tk_button_se_info_enter(self, parent):
        btn = ttk.Button(parent, text="导出表格", takefocus=False, command=self.button_se_info_enter)
        btn.place(relx=0.915, rely=0.01, relwidth=0.08, relheight=0.04)
        return btn
    def button_se_info_enter(self):
        save_file("教工信息表", teacher_info_showall(), teacher_info_add_low())
        pass

    def __tk_label_se_info_name(self, parent):
        label = ttk.Label(parent, text="姓 名：", anchor="center", )
        label.place(relx=0.52, rely=0.00, relwidth=0.07, relheight=0.06)
        return label

    def __tk_input_se_info_find_name(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.59, rely=0.01, relwidth=0.14, relheight=0.04)
        return ipt

    def __tk_button_e_info_enter(self, parent):
        btn = ttk.Button(parent, text="查找", takefocus=False, command=self.button_e_info_enter)
        btn.place(relx=0.73, rely=0.01, relwidth=0.07, relheight=0.04)
        return btn
    def button_e_info_enter(self):
        # 查询教师信息是否存在
        tdata = teacher_find_name(self.tk_input_e_info_find_name.get())
        print(self.tk_input_e_info_find_name.get())
        print(tdata)
        if tdata:
            for item in self.tk_table_se_info_show.get_children():
                self.tk_table_se_info_show.delete(item)
            for col in tdata:
                self.tk_table_se_info_show.insert("", "end", values=tuple(col))
            pass
        else:
            data = teacher_info_showall()
            for item in self.tk_table_se_info_show.get_children():
                self.tk_table_se_info_show.delete(item)
            for col in data:
                self.tk_table_se_info_show.insert("", "end", values=tuple(col))
            # messagebox.showerror("信息提示", '学生信息不存在，请重新输入信息！')
            pass
        pass
    ####### -- 教工管理 -- ########

    ########   院系管理   #########
    # ①院系添加
    def __tk_frame_top_left_D(self,parent):
        frame = ttk.Frame(parent,)
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame
    def __tk_frame_dleft_1(self,parent):
        frame = ttk.Frame(parent,)
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.73)
        return frame
    def __tk_label_frame_dept_add(self,parent):
        frame = ttk.LabelFrame(parent,text="院系添加",)
        frame.place(relx=0.01, rely=0.03, relwidth=0.97, relheight=0.95)
        return frame
    def __tk_label_dno(self,parent):
        label = ttk.Label(parent,text="编 号：",anchor="center", )
        label.place(relx=0.07, rely=0.05, relwidth=0.07, relheight=0.08)
        return label
    def __tk_input_dno_txtin(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.06, relwidth=0.21, relheight=0.06)
        return ipt
    def __tk_label_dname(self,parent):
        label = ttk.Label(parent,text="名 称：",anchor="center", )
        label.place(relx=0.07, rely=0.14, relwidth=0.07, relheight=0.08)
        return label
    def __tk_input_dname_txtin(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.15, relwidth=0.21, relheight=0.06)
        return ipt
    def __tk_button_d_add_enter(self,parent):
        btn = ttk.Button(parent, text="添加确认", takefocus=False, command=self.button_d_add_enter)
        btn.place(relx=0.25, rely=0.77, relwidth=0.10, relheight=0.06)
        return btn
    def button_d_add_enter(self):
        print('进入添加院系操作！')
        if len(self.tk_input_dno_txtin.get()) and len(self.tk_input_dname_txtin.get()):
            result = messagebox.askokcancel("信息添加提示", '是否确认添加？')
            if result:
                # sql增加信息
                result = dept_add(self.tk_input_dno_txtin.get(), self.tk_input_dname_txtin.get(),
                                  self.tk_input_dmanager_txtin.get())
                print(result)
                if result:
                    # 清空信息
                    self.tk_input_dno_txtin.delete(0, ttk.END)
                    self.tk_input_dname_txtin.delete(0, ttk.END)
                    self.tk_input_dmanager_txtin.delete(0, ttk.END)
                    messagebox.showinfo("添加提示", "添加成功！")
                else:
                    messagebox.showerror("错误提示", "院系编号重复，请重新修改！")
            else:
                print('取消添加院系操作！')
        else:
            messagebox.showerror("信息添加提示", '院系编号和院系名称所填内容不能为空！')

            pass
        pass
    def __tk_label_dmanager(self,parent):
        label = ttk.Label(parent,text="系主任：",anchor="center", )
        label.place(relx=0.07, rely=0.24, relwidth=0.07, relheight=0.08)
        return label
    def __tk_input_dmanager_txtin(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.25, relwidth=0.21, relheight=0.06)
        return ipt
    def __tk_frame_dtleft_2(self,parent):
        frame = ttk.Frame(parent,)
        frame.place(relx=0.00, rely=0.73, relwidth=1.00, relheight=0.27)
        return frame
    def __tk_label_frame_d_add_batch(self,parent):
        frame = ttk.LabelFrame(parent,text="批量处理",)
        frame.place(relx=0.01, rely=0.00, relwidth=0.97, relheight=0.93)
        return frame
    def __tk_button_dexcl_file_se(self,parent):
        btn = ttk.Button(parent, text="选择excl文件", takefocus=False, command=self.dexcl_file_selcet)
        btn.place(relx=0.07, rely=0.07, relwidth=0.13, relheight=0.21)
        return btn
    def dexcl_file_selcet(self):
        filename = select_file()
        # 批量写入数据到mysql
        if filename:
            result = messagebox.askokcancel("信息提示", "是否导入信息？")
            if result:
                data = batch_add(filename)
                i = 1
                j = 0
                row = ()
                for data_item in data:
                    result = dept_add(data_item[0], data_item[1], data_item[2])
                    i += 1
                    if result is False:
                        j = i
                        row += (j,)
                if j != 0:
                    messagebox.showerror("信息提示", f"文件中的{row}行数据导入失败，院系编号已存在！")
                else:
                    messagebox.showinfo("信息导入提示", '院系信息导入成功！')
                    print("导入信息成功！")
            else:
                print("导入信息取消！")
        pass
    def __tk_button_dexcl_file_demp(self, parent):
        btn = ttk.Button(parent, text="导出文档模板", takefocus=False,command=self.dexcl_file_demp)
        btn.place(relx=0.07, rely=0.43, relwidth=0.13, relheight=0.21)

        return btn
    def dexcl_file_demp(self):
        save_file("院系信息文件填写格式模板", None, adept_info_add_low(), True)
        pass
    # ②院系修改
    def __tk_frame_top_left_D2(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_frame_D2left_1(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.44, relwidth=1.00, relheight=0.56)
        return frame

    def __tk_label_frame_dept_update(self, parent):
        frame = ttk.LabelFrame(parent, text="院系信息修改", )
        frame.place(relx=0.01, rely=0.03, relwidth=0.97, relheight=0.93)
        return frame

    def __tk_label_dno_up(self, parent):
        label = ttk.Label(parent, text="编 号：", anchor="center", )
        label.place(relx=0.07, rely=0.07, relwidth=0.07, relheight=0.10)
        return label

    def __tk_label_dno_up_txt(self, parent):
        label = ttk.Label(parent, anchor="w", )
        label.place(relx=0.14, rely=0.08, relwidth=0.21, relheight=0.08)
        return label

    def __tk_label_dname_up(self, parent):
        label = ttk.Label(parent, text="名 称：", anchor="center", )
        label.place(relx=0.07, rely=0.19, relwidth=0.07, relheight=0.10)
        return label

    def __tk_input_dname_up_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.20, relwidth=0.21, relheight=0.08)
        return ipt

    def __tk_label_dmanager_up(self, parent):
        label = ttk.Label(parent, text="主 任：", anchor="center", )
        label.place(relx=0.07, rely=0.31, relwidth=0.07, relheight=0.10)
        return label

    def __tk_button_dept_del(self, parent):
        btn = ttk.Button(parent, text="删除", takefocus=False, command=self.button_dept_del)
        btn.place(relx=0.25, rely=0.60, relwidth=0.10, relheight=0.08)
        return btn

    def button_dept_del(self):
        self.tk_button_dept_update.configure(state='disabled')
        if not self.tk_label_dno_up_txt.cget("text"):
            messagebox.showerror("院系选择提示", '请先选择要进行删除的院系信息！')
            pass
        else:
            result = messagebox.askokcancel("信息删除提示", '是否确认删除信息？')
            if result:
                # 调用sql
                # 院系编号dno
                adept_info_del(self.tk_label_dno_up_txt.cget("text"))
                # !@#
                data = dept_info()
                for item in self.tk_table_de_find.get_children():
                    self.tk_table_de_find.delete(item)

                for col in data:
                    self.tk_table_de_find.insert("", "end", values=tuple(col))
                # 清空信息
                self.tk_label_dno_up_txt.configure(text="")
                self.tk_input_dname_up_txtin.delete(0, ttk.END)
                self.tk_input_dmanager_up_txtin.delete(0, ttk.END)
                # !@#
            else:
                print('取消修改院系信息！')

        self.tk_button_dept_update.configure(state='normal')
        pass

    def __tk_button_dept_update(self,parent):
        btn = ttk.Button(parent, text="修改", takefocus=False, command=self.button_dept_update)
        btn.place(relx=0.07, rely=0.60, relwidth=0.07, relheight=0.08)
        return btn

    def button_dept_update(self):
        self.tk_button_dept_del.configure(state='disabled')
        if not self.tk_label_dno_up_txt.cget("text"):
            messagebox.showerror("院系选择提示", '请先选择要进行修改信息的院系！')
            pass
        else:
            if len(self.tk_input_dname_up_txtin.get()) == 0 and len(self.tk_input_dmanager_up_txtin.get()) == 0:
                messagebox.showerror("信息内容提示", '填写的信息内容不能为空！\n请重新填写修改信息！')
            else:
                result = messagebox.askokcancel("信息修改提示", '是否确认修改信息？')
                if result:
                    # 调用sql
                    # 院系编号dno，院系名称dname，院系主任dmanager
                    adept_info_update(self.tk_input_dname_up_txtin.get(),
                                      self.tk_input_dmanager_up_txtin.get(),
                                      self.tk_label_dno_up_txt.cget("text"),
                                      )
                    # !@#
                    data = dept_info()
                    for item in self.tk_table_de_find.get_children():
                        self.tk_table_de_find.delete(item)

                    for col in data:
                        self.tk_table_de_find.insert("", "end", values=tuple(col))
                    # 清空信息
                    self.tk_label_dno_up_txt.configure(text="")
                    self.tk_input_dname_up_txtin.delete(0, ttk.END)
                    self.tk_input_dmanager_up_txtin.delete(0, ttk.END)
                    # !@#
                else:
                    print('取消修改院系信息！')
        self.tk_button_dept_del.configure(state='normal')
        pass

    def __tk_label_d2left_tip(self, parent):
        label = ttk.Label(parent, text="信息提示", anchor="center", )
        label.place(relx=0.07, rely=0.69, relwidth=0.28, relheight=0.10)
        return label

    def __tk_input_dmanager_up_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.32, relwidth=0.21, relheight=0.08)
        return ipt

    def __tk_frame_d2left_2(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.44)
        return frame

    def __tk_table_de_find(self, parent):
        # 表头字段 表头宽度
        columns = {"院系编号": 143, "院系名称": 143, "系主任": 143, "院系教工数": 143}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.bind('<<TreeviewSelect>>', self.dept_find_select)
        tk_table.place(relx=0.01, rely=0.16, relwidth=0.97, relheight=0.83)
        self.create_bar(parent, tk_table,True, False,4.5, 39.2, 720,200,740,242.3)

        return tk_table
    def dept_find_select(self, event):
        selection = event.widget.selection()
        if selection:
            # 获取选中的行索引
            index = selection[0]
            # 获取行中的数据
            dept = event.widget.set(index)
            print(f'{dept}')
            # 刷新文本框
            # self.tk_label_dno_up_txt.delete(0, tkinter.END)
            self.tk_input_dname_up_txtin.delete(0, ttk.END)
            self.tk_input_dmanager_up_txtin.delete(0, ttk.END)
            # 填写文本框
            self.tk_label_dno_up_txt.configure(text=dept['院系编号'])
            self.tk_input_dname_up_txtin.insert(0, dept['院系名称'])
            self.tk_input_dmanager_up_txtin.insert(0, dept['系主任'])
        pass

    def __tk_label_dnotxt(self, parent):
        label = ttk.Label(parent, text="请点击需要修改信息的院系!", anchor="w", )
        label.place(relx=0.01, rely=0.04, relwidth=0.22, relheight=0.11)
        return label

    # ③院系信息表
    def __tk_frame_top_left_D3(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_frame_deinfo_left(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=1.00)
        return frame

    def __tk_label_frame_dept_info3(self, parent):
        frame = ttk.LabelFrame(parent, text="院系信息", )
        frame.place(relx=0.01, rely=0.00, relwidth=0.99, relheight=0.98)
        return frame

    def __tk_table_de_info_show(self, parent):
        # 表头字段 表头宽度
        columns = {"院系编号": 143, "院系名称": 143, "系主任": 143, "院系教工数": 143}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.01, rely=0.06, relwidth=0.985, relheight=0.925)
        self.create_bar(parent, tk_table, True, False, 0.75, 34, 725, 495, 730, 540)
        return tk_table

    def __tk_button_export_file(self,parent):
        btn = ttk.Button(parent, text="导出表格", takefocus=False,command=self.button_export_file)
        btn.place(relx=0.915, rely=0.01, relwidth=0.08, relheight=0.04)
        return btn

    def button_export_file(self):
        save_file("院系信息表", dept_info(), file_low_get())
        pass

    def __tk_input_de_info_find_dno(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.22, rely=0.00, relwidth=0.21, relheight=0.06)
        return ipt

    def __tk_label_de_info_dno(self, parent):
        label = ttk.Label(parent, text="院系编号：", anchor="center", )
        label.place(relx=0.12, rely=0.00, relwidth=0.10, relheight=0.06)
        return label

    def __tk_label_de_info_name(self, parent):
        label = ttk.Label(parent, text="院系名称：", anchor="center", )
        label.place(relx=0.49, rely=0.00, relwidth=0.10, relheight=0.06)
        return label

    def __tk_input_de_info_find_name(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.59, rely=0.00, relwidth=0.21, relheight=0.06)
        return ipt

    def __tk_button_de_info_enter(self, parent):
        btn = ttk.Button(parent, text="查找", takefocus=False, )
        btn.place(relx=0.92, rely=0.00, relwidth=0.07, relheight=0.06)
        return btn
    ####### -- 院系管理 -- ########

    # 权限管理
    def __tk_frame_top_left_R(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_frame_Rleft_1(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.63, relwidth=1.00, relheight=0.37)
        return frame

    def __tk_label_frame_root_update(self, parent):
        frame = ttk.LabelFrame(parent, text="权限管理", )
        frame.place(relx=0.01, rely=0.00, relwidth=0.97, relheight=0.89)
        return frame

    def __tk_label_rt(self, parent):
        label = ttk.Label(parent, text="工 号：", anchor="center", )
        label.place(relx=0.15, rely=0.00, relwidth=0.07, relheight=0.16)
        return label

    def __tk_button_root_update_enter(self, parent):
        btn = ttk.Button(parent, text="修改", takefocus=False, )
        btn.place(relx=0.29, rely=0.60, relwidth=0.07, relheight=0.16)
        return btn

    def __tk_label_rnametxt(self, parent):
        label = ttk.Label(parent, anchor="center", )
        label.place(relx=0.22, rely=0.16, relwidth=0.14, relheight=0.16)
        return label

    def __tk_label_rname(self, parent):
        label = ttk.Label(parent, text="姓 名：", anchor="center", )
        label.place(relx=0.15, rely=0.16, relwidth=0.07, relheight=0.16)
        return label

    def __tk_label_rtxt(self, parent):
        label = ttk.Label(parent, anchor="center", )
        label.place(relx=0.22, rely=0.00, relwidth=0.14, relheight=0.16)
        return label

    def __tk_label_roots(self, parent):
        label = ttk.Label(parent, text="权 限：", anchor="center", )
        label.place(relx=0.15, rely=0.33, relwidth=0.07, relheight=0.16)
        return label

    def __tk_select_box_rootslet(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("0 【管理员】", "1 【主任】", "2 【教师】")
        cb.place(relx=0.22, rely=0.33, relwidth=0.14, relheight=0.16)
        return cb

    def __tk_frame_rleft_2(self, parent):
        frame = ttk.Frame(parent, )
        frame.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.63)
        return frame

    def __tk_table_rtno_show(self, parent):
        # 表头字段 表头宽度
        columns = {"教工号": 215, "姓名": 287, "权限等级": 215}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.01, rely=0.01, relwidth=0.97, relheight=0.87)
        self.create_bar(parent, tk_table, True, False, 7, 5, 720, 300, 740, 345)
        return tk_table

    def __tk_label_rstnotxt(self, parent):
        label = ttk.Label(parent, text="教工号：", anchor="center", )
        label.place(relx=0.64, rely=0.90, relwidth=0.07, relheight=0.09)
        return label

    def __tk_input_rstno_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.71, rely=0.90, relwidth=0.20, relheight=0.09)
        return ipt

    def __tk_button_rstnofind_enter(self, parent):
        btn = ttk.Button(parent, text="查找", takefocus=False, )
        btn.place(relx=0.91, rely=0.90, relwidth=0.07, relheight=0.09)
        return btn

    # 课程管理
    def __tk_frame_top_left_C(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_tabs_course_i(self, parent):
        frame = ttk.Notebook(parent)
        self.tk_tabs_course_i_0 = self.__tk_frame_course_i_0(frame)
        frame.add(self.tk_tabs_course_i_0, text="添加课程")
        self.tk_tabs_course_i_1 = self.__tk_frame_course_i_1(frame)
        frame.add(self.tk_tabs_course_i_1, text="修改&删除课程")
        self.tk_tabs_course_i_2 = self.__tk_frame_course_i_2(frame)
        frame.add(self.tk_tabs_course_i_2, text="查询课程")
        self.tk_tabs_course_i_3 = self.__tk_frame_course_i_3(frame)
        frame.add(self.tk_tabs_course_i_3, text="课程发布")
        self.tk_tabs_course_i_4 = self.__tk_frame_course_i_4(frame)
        frame.add(self.tk_tabs_course_i_4, text="添加授课教师")
        frame.place(relx=0.01, rely=0.00, relwidth=0.99, relheight=0.97)
        frame.bind("<<NotebookTabChanged>>", self.on_tabs_select)
        return frame
    def on_note_select_1(self):
        self.course_add_display()
        pass
    def on_note_select_2(self):
        self.course_deup_display()
        pass
    def on_note_select_3(self):
        self.course_i_display()
        pass
    def on_note_select_4(self):
        self.course_start_display()
        pass
    def on_note_select_5(self):
        self.course_add_teacher_display()
        pass
    def on_tabs_select(self, event):
        # 获取当前选中的标签页
        index_txt = self.tk_tabs_course_i.tab('current')['text']
        print(index_txt)
        if index_txt == "添加课程":
            self.on_note_select_1()
            pass
        if index_txt == "修改&删除课程":
            self.on_note_select_2()
            pass
        if index_txt == "查询课程":
            self.on_note_select_3()
            pass
        if index_txt == "课程发布":
            self.on_note_select_4()
            pass
        if index_txt == "添加授课教师":
            self.on_note_select_5()
            pass
        pass
    # 添加课程
    def __tk_frame_course_i_0(self, parent):
        frame = ttk.Frame(parent)
        frame.place(relx=0.01, rely=0.00, relwidth=0.99, relheight=0.97)
        return frame
    def course_add(self):
        print('进入添加课程操作！')

        if (len(self.tk_input_c_id_txtin.get()) and len(self.tk_input_c_name_txtin.get()) and
            len(self.tk_input_c_credit_txtin.get()) and len(self.tk_input_c_time_txtin.get())
            and len(self.tk_input_c_address_txtin.get()) and self.tk_select_box_c_se_type.get() != "请选择"):
            result = messagebox.askokcancel("信息添加提示", '是否确认添加？')
            if result:
                # 显示课程编号
                print(self.tk_input_c_id_txtin.get())
                # sql增加信息
                result = mysql_course_add(self.tk_select_box_c_se_type.get(), self.tk_input_c_id_txtin.get(),
                                          self.tk_input_c_name_txtin.get(), self.tk_input_c_credit_txtin.get(),
                                          self.tk_input_c_time_txtin.get(), self.tk_input_c_address_txtin.get(),
                                          )
                if result:
                    # 清空信息,填写初始化
                    self.tk_select_box_c_se_type.current(0)
                    self.tk_input_c_id_txtin.delete(0, ttk.END)
                    self.tk_input_c_name_txtin.delete(0, ttk.END)
                    self.tk_input_c_credit_txtin.delete(0, ttk.END)
                    self.tk_input_c_time_txtin.delete(0, ttk.END)
                    self.tk_input_c_address_txtin.delete(0, ttk.END)

                    messagebox.showinfo("添加提示", "添加成功！")
                else:
                    messagebox.showerror("错误提示", "课程编号重复，请重新修改！")
                    pass
            else:
                print('取消添加课程操作！')
        else:
            messagebox.showerror("信息添加提示", '所填内容不能为空！')
            pass
        pass
    # 修改&删除课程
    def __tk_frame_course_i_1(self, parent):
        frame = ttk.Frame(parent)
        frame.place(relx=0.01, rely=0.00, relwidth=0.99, relheight=0.97)
        return frame

    # 查询课程
    def __tk_frame_course_i_2(self, parent):
        frame = ttk.Frame(parent)
        frame.place(relx=0.01, rely=0.00, relwidth=0.99, relheight=0.97)
        return frame

    # 课程发布
    def __tk_frame_course_i_3(self, parent):
        frame = ttk.Frame(parent)
        frame.place(relx=0.01, rely=0.00, relwidth=0.99, relheight=0.97)
        return frame
    # 授课教师添加
    def __tk_frame_course_i_4(self,parent):
        frame = ttk.Frame(parent)
        frame.place(relx=0.01, rely=0.00, relwidth=0.99, relheight=0.97)
        return frame
    def __tk_label_c_address(self, parent):
        label = ttk.Label(parent, text="上课地点：", anchor="w", )
        label.place(relx=0.06, rely=0.35, relwidth=0.08, relheight=0.06)
        return label

    def __tk_input_c_id_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.12, relwidth=0.27, relheight=0.04)
        return ipt

    def __tk_label_c_time(self, parent):
        label = ttk.Label(parent, text="上课时间：", anchor="w", )
        label.place(relx=0.06, rely=0.29, relwidth=0.08, relheight=0.06)
        return label

    def __tk_input_c_name_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.18, relwidth=0.27, relheight=0.04)
        return ipt

    def __tk_label_c_credit(self, parent):
        label = ttk.Label(parent, text="学 分：", anchor="w", )
        label.place(relx=0.06, rely=0.23, relwidth=0.08, relheight=0.06)
        return label

    def __tk_input_c_credit_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.24, relwidth=0.27, relheight=0.04)
        return ipt

    def __tk_label_c_name(self, parent):
        label = ttk.Label(parent, text="课程名：", anchor="w", )
        label.place(relx=0.06, rely=0.17, relwidth=0.08, relheight=0.06)
        return label

    def __tk_label_c_id(self, parent):
        label = ttk.Label(parent, text="课程ID：", anchor="w", )
        label.place(relx=0.06, rely=0.11, relwidth=0.08, relheight=0.06)
        return label

    def __tk_input_c_time_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.30, relwidth=0.27, relheight=0.04)
        return ipt

    def __tk_input_c_address_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.14, rely=0.36, relwidth=0.27, relheight=0.04)
        return ipt
    def __tk_button_c_add(self, parent):
        btn = ttk.Button(parent, text="添加", takefocus=False, command=self.course_add)
        btn.place(relx=0.34, rely=0.48, relwidth=0.07, relheight=0.04)
        return btn

    def __tk_label_frame_c_batch_info(self, parent):
        frame = ttk.LabelFrame(parent, text="课程批量添加", )
        frame.place(relx=0.06, rely=0.57, relwidth=0.35, relheight=0.32)
        return frame

    def __tk_button_c_batch_add(self, parent):
        btn = ttk.Button(parent, text="选择excl文件", takefocus=False, command=self.button_c_batch_add)
        btn.place(relx=0.21, rely=0.14, relwidth=0.41, relheight=0.17)
        return btn
    def button_c_batch_add(self):
        filename = select_file()
        # 批量写入数据到mysql
        if filename:
            result = messagebox.askokcancel("信息提示", "是否导入信息？")
            if result:
                # 获取excl文件的数据
                data = batch_add(filename)
                i = 1
                j = 0
                row = ()
                for data_item in data:
                    result = mysql_course_add(data_item[0], data_item[1], data_item[2],
                                              data_item[3], data_item[4], data_item[5],
                                              data_item[6], data_item[7],
                                              )
                    i += 1
                    if result is False:
                        j = i
                        row += (j,)
                if j != 0:
                    messagebox.showerror("信息提示", f"文件中的{row}行数据导入失败，学号已存在或数据存在错误！")
                else:
                    messagebox.showinfo("信息导入提示", '课程信息导入成功！')
                    print("信息导入成功！")
            else:
                print("信息导入取消！")
        pass

    def __tk_button_c_batch_demo(self, parent):
        btn = ttk.Button(parent, text="导出文档模板", takefocus=False, command=self.course_excl_file_demp)
        btn.place(relx=0.21, rely=0.44, relwidth=0.41, relheight=0.17)
        return btn
    def course_excl_file_demp(self):
        save_file("课程信息文件填写格式模板", None, course_info_low(), True)
        pass
    def __tk_label_c_add_type(self,parent):
        label = ttk.Label(parent,text="课程类型：",anchor="center", )
        label.place(relx=0.48, rely=0.11, relwidth=0.08, relheight=0.06)
        return label
    def __tk_select_box_c_se_type(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择", "必修课", "选修课", "体育课", "文化课", "通识课")
        cb.place(relx=0.57, rely=0.12, relwidth=0.12, relheight=0.04)
        return cb

    def __tk_label_c_up_id(self, parent):
        label = ttk.Label(parent, text="课程ID：", anchor="w", )
        label.place(relx=0.07, rely=0.64, relwidth=0.08, relheight=0.04)
        return label

    def __tk_label_c_up_name(self, parent):
        label = ttk.Label(parent, text="课程名：", anchor="w", )
        label.place(relx=0.07, rely=0.69, relwidth=0.08, relheight=0.06)
        return label

    def __tk_label_c_up_credit(self, parent):
        label = ttk.Label(parent, text="学 分：", anchor="w", )
        label.place(relx=0.07, rely=0.75, relwidth=0.08, relheight=0.06)
        return label

    def __tk_label_c_up_time(self, parent):
        label = ttk.Label(parent, text="上课时间：", anchor="w", )
        label.place(relx=0.07, rely=0.81, relwidth=0.08, relheight=0.06)
        return label

    def __tk_label_c_up_address(self, parent):
        label = ttk.Label(parent, text="上课地点：", anchor="w", )
        label.place(relx=0.07, rely=0.87, relwidth=0.08, relheight=0.06)
        return label
    def __tk_label_c_up_id_txtin(self,parent):
        label = ttk.Label(parent,anchor="w", )
        label.place(relx=0.15, rely=0.64, relwidth=0.27, relheight=0.04)
        return label

    def __tk_input_c_up_name_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.15, rely=0.70, relwidth=0.27, relheight=0.04)
        return ipt

    def __tk_input_c_up_credit_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.15, rely=0.76, relwidth=0.27, relheight=0.04)
        return ipt

    def __tk_input_c_up_time_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.15, rely=0.82, relwidth=0.27, relheight=0.04)
        return ipt

    def __tk_input_c_up_address_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.15, rely=0.88, relwidth=0.27, relheight=0.04)
        return ipt

    def __tk_label_c_up_type(self, parent):
        label = ttk.Label(parent, text="课程类型：", anchor="center", )
        label.place(relx=0.50, rely=0.63, relwidth=0.08, relheight=0.06)
        return label
    def __tk_label_cnonum(self,parent):
        label = ttk.Label(parent,text="限选总数：",anchor="center", )
        label.place(relx=0.50, rely=0.69, relwidth=0.08, relheight=0.06)
        return label
    def __tk_label_limnum(self,parent):
        label = ttk.Label(parent,text="已选人数：",anchor="center", )
        label.place(relx=0.50, rely=0.75, relwidth=0.08, relheight=0.06)
        return label
    def __tk_input_cnonum_in(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.58, rely=0.70, relwidth=0.11, relheight=0.04)
        return ipt
    def __tk_input_limnum_in(self,parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.58, rely=0.76, relwidth=0.11, relheight=0.04)
        return ipt
    def __tk_label_c_sel_type(self,parent):
        label = ttk.Label(parent,text="课程类型：",anchor="center", )
        label.place(relx=0.31, rely=0.00, relwidth=0.08, relheight=0.06)
        return label
    def __tk_select_box_c_sel_types(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("全部","必修课","选修课","体育课","文化课","通识课")
        cb.place(relx=0.40, rely=0.01, relwidth=0.12, relheight=0.04)
        return cb
    def __tk_select_box_c_se_up_type(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择", "必修课", "选修课", "体育课", "文化课", "通识课")
        cb.place(relx=0.58, rely=0.64, relwidth=0.11, relheight=0.04)
        return cb

    def __tk_table_c_up_show(self, parent):
        # 表头字段 表头宽度
        columns = {"课程类型":58,"课程编号":58,"课程名":131,"学分":36,"上课时间":212,"上课地点":130,"限选":36,"已选":36,"":12}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.005, rely=0.06, relwidth=0.99, relheight=0.56)
        self.create_bar(parent, tk_table, True, False, 0, 33, 725.3, 297, 730, 535.5)
        tk_table.bind('<<TreeviewSelect>>', self.c_up_find)
        return tk_table

    def c_up_find(self, event):
        selection = event.widget.selection()
        if selection:
            # 获取选中的行索引
            index = selection[0]
            # 获取行中的数据
            sel = event.widget.set(index)
            print(f'{sel}')
            # 刷新
            self.tk_select_box_c_se_up_type.current(0)
            self.tk_label_c_up_id_txtin.configure(text="")
            self.tk_input_c_up_name_txtin.delete(0, ttk.END)
            self.tk_input_c_up_credit_txtin.delete(0, ttk.END)
            self.tk_input_c_up_time_txtin.delete(0, ttk.END)
            self.tk_input_c_up_address_txtin.delete(0, ttk.END)
            self.tk_input_cnonum_in.delete(0, ttk.END)
            self.tk_input_limnum_in.delete(0, ttk.END)
            # 填写
            data = ("全部", "必修课", "选修课", "体育课", "文化课", "通识课")
            cindex = data.index(sel['课程类型'])
            self.tk_select_box_c_se_up_type.current(cindex)
            self.tk_label_c_up_id_txtin.configure(text=sel['课程编号'])
            self.tk_input_c_up_name_txtin.insert(0, sel['课程名'])
            self.tk_input_c_up_credit_txtin.insert(0, sel['学分'])
            self.tk_input_c_up_time_txtin.insert(0, sel['上课时间'])
            self.tk_input_c_up_address_txtin.insert(0, sel['上课地点'])
            self.tk_input_cnonum_in.insert(0, sel['限选'])
            self.tk_input_limnum_in.insert(0, sel['已选'])

    pass
    def __tk_button_c_update(self, parent):
        btn = ttk.Button(parent, text="修改", takefocus=False, command=self.button_c_update)
        btn.place(relx=0.62, rely=0.88, relwidth=0.07, relheight=0.04)
        return btn
    def button_c_update(self):
        self.tk_button_c_del.configure(state='disabled')
        if not (len(self.tk_label_c_up_id_txtin.cget("text")) and len(self.tk_input_c_up_name_txtin.get())
                and len(self.tk_input_c_up_credit_txtin.get()) and len(self.tk_input_c_up_time_txtin.get())
                and len(self.tk_input_c_up_address_txtin.get()) and len(self.tk_input_cnonum_in.get())
                and len(self.tk_input_limnum_in.get()) and self.tk_select_box_c_se_up_type.get() != "请选择"):
            messagebox.showerror("信息提示", '请选择要进行修改的课程信息或修改信息欠缺！')
            pass
        else:
            result = messagebox.askokcancel("信息修改提示", '是否修改信息？')
            if result:
                course_update(self.tk_select_box_c_se_up_type.get(), self.tk_label_c_up_id_txtin.cget("text"),
                              self.tk_input_c_up_name_txtin.get(), self.tk_input_c_up_credit_txtin.get(),
                              self.tk_input_c_up_time_txtin.get(), self.tk_input_c_up_address_txtin.get(),
                              self.tk_input_cnonum_in.get(), self.tk_input_limnum_in.get(),
                              )
                # 刷新
                self.course_deup_display()
                messagebox.showinfo("信息提示", "修改成功！")
            else:
                print('取消修改课程信息！')
        self.tk_button_c_del.configure(state='normal')
        pass

    def __tk_input_c_s_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.72, rely=0.01, relwidth=0.21, relheight=0.04)
        return ipt

    def __tk_button_c_s_find(self, parent):
        btn = ttk.Button(parent, text="查找", takefocus=False, command=self.course_select_up_type)
        btn.place(relx=0.934, rely=0.01, relwidth=0.061, relheight=0.04)
        return btn
    def course_select_up_type(self):
        if len(self.tk_input_c_s_txtin.get()):
            self.print_course_up_data(self.tk_select_box_c_sel_types.get(), self.tk_input_c_s_txtin.get())
        else:
            self.print_course_up_data(self.tk_select_box_c_sel_types.get())
            pass
        pass

    # 课程查询
    def print_course_up_data(self, ctype, cname=None):
        data = couse_info_select(ctype, cname)
        for item in self.tk_table_c_up_show.get_children():
            self.tk_table_c_up_show.delete(item)
        for col in data:
            self.tk_table_c_up_show.insert("", "end", values=tuple(col))
        pass
    def __tk_label_c_s_txt(self, parent):
        label = ttk.Label(parent, text="课程名：", anchor="center", )
        label.place(relx=0.65, rely=0.00, relwidth=0.07, relheight=0.06)
        return label

    def __tk_button_c_del(self, parent):
        btn = ttk.Button(parent, text="删除", takefocus=False, command=self.button_c_del)
        btn.place(relx=0.51, rely=0.88, relwidth=0.07, relheight=0.04)
        return btn
    def button_c_del(self):
        self.tk_button_c_update.configure(state='disabled')
        if not (len(self.tk_label_c_up_id_txtin.cget("text")) and len(self.tk_input_c_up_name_txtin.get())
                and len(self.tk_input_c_up_credit_txtin.get()) and len(self.tk_input_c_up_time_txtin.get())
                and len(self.tk_input_c_up_address_txtin.get()) and len(self.tk_input_cnonum_in.get())
                and len(self.tk_input_limnum_in.get()) and self.tk_select_box_c_se_up_type.get() != "请选择"):
            messagebox.showerror("信息提示", '请选择要进行删除的课程信息或删除信息欠缺！')
            pass
        else:
            result = messagebox.askokcancel("信息删除提示", '是否删除信息？')
            if result:
                course_del(self.tk_label_c_up_id_txtin.cget("text"))
                # 刷新
                self.course_deup_display()
                messagebox.showinfo("信息提示", "删除成功！")
            else:
                print('取消删除课程信息！')
        self.tk_button_c_update.configure(state='normal')
        pass

    def __tk_table_c_info_show(self, parent):
        # 表头字段 表头宽度
        columns = {"课程类型":58,"课程编号":58,"课程名":131,"学分":36,"上课时间":212,"上课地点":130,"限选":40,"已选":40,"":12}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.005, rely=0.065, relwidth=0.99, relheight=0.925)
        self.create_bar(parent, tk_table, True, False, 0, 36, 725, 488, 730, 532)
        return tk_table
    def __tk_label_c_show_type(self,parent):
        label = ttk.Label(parent,text="课程类型：",anchor="center", )
        label.place(relx=0.16, rely=0.01, relwidth=0.08, relheight=0.04)
        return label
    def __tk_select_box_c_show_types(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("全部","必修课","选修课","体育课","文化课","通识课")
        cb.place(relx=0.25, rely=0.01, relwidth=0.12, relheight=0.04)
        # cb.bind("<<ComboboxSelected>>", self.course_select_type)
        return cb

    def course_select_type(self):
        if len(self.tk_input_ci_txtin.get()):
            self.print_course_data(self.tk_select_box_c_show_types.get(), self.tk_input_ci_txtin.get())
        else:
            self.print_course_data(self.tk_select_box_c_show_types.get())
            pass
        pass

    # 课程查询
    def print_course_data(self, ctype, cname=None):
        data = couse_info_select(ctype, cname)
        for item in self.tk_table_c_info_show.get_children():
            self.tk_table_c_info_show.delete(item)
        for col in data:
            self.tk_table_c_info_show.insert("", "end", values=tuple(col))
        pass
    def __tk_button_ci_find(self, parent):
        btn = ttk.Button(parent, text="查找", takefocus=False, command=self.course_select_type)
        btn.place(relx=0.74, rely=0.01, relwidth=0.07, relheight=0.04)
        return btn

    def __tk_input_ci_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.52, rely=0.01, relwidth=0.21, relheight=0.04)
        return ipt

    def __tk_label_ci_txt(self, parent):
        label = ttk.Label(parent, text="课程名：", anchor="center", )
        label.place(relx=0.45, rely=0.01, relwidth=0.07, relheight=0.04)
        return label

    def __tk_button_course_exclfiles(self, parent):
        btn = ttk.Button(parent, text="导出表格", takefocus=False, command=self.button_course_exclfiles )
        btn.place(relx=0.915, rely=0.01, relwidth=0.08, relheight=0.04)
        return btn
    def button_course_exclfiles(self):
        save_file("课程信息表", course_info_low(True), course_info_low(False))
        pass

    def __tk_select_box_course_type_se(self,parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择","必修课","选修课","体育课","文化课","通识课")
        cb.place(relx=0.22, rely=0.63, relwidth=0.16, relheight=0.04)
        return cb
    def __tk_label_course_type(self,parent):
        label = ttk.Label(parent,text="课程类型：",anchor="center", )
        label.place(relx=0.14, rely=0.62, relwidth=0.08, relheight=0.06)
        return label
    def __tk_button_course_start(self,parent):
        btn = ttk.Button(parent, text="发布", takefocus=False, command=self.button_course_start)
        btn.place(relx=0.14, rely=0.83, relwidth=0.07, relheight=0.04)
        return btn
    def button_course_start(self):
        if self.tk_label_cr_start_time_txt.cget('text') != "无" and self.tk_label_cr_end_time_txt.cget('text') != "无" and self.tk_select_box_course_type_se.get() != "请选择":
            # sql
            course_flag_start(self.tk_select_box_course_type_se.get())
            data = course_start_info()
            for item in self.tk_table_course_start_show.get_children():
                self.tk_table_course_start_show.delete(item)
            for col in data:
                self.tk_table_course_start_show.insert("", "end", values=tuple(col))
        else:
            messagebox.showinfo("信息提示","请先设置时间！")
            pass
        pass

    def __tk_label_cr_start_time(self, parent):
        label = ttk.Label(parent, text="选课时间：", anchor="center", )
        label.place(relx=0.14, rely=0.68, relwidth=0.08, relheight=0.06)
        return label

    def __tk_label_cr_start_time_txt(self, parent):
        label = ttk.Label(parent, text="2023/12/22 21:24:00", anchor="w", )
        label.place(relx=0.22, rely=0.69, relwidth=0.18, relheight=0.04)
        return label

    def __tk_label_cr_end_time(self, parent):
        label = ttk.Label(parent, text="选课结束：", anchor="center", )
        label.place(relx=0.14, rely=0.74, relwidth=0.08, relheight=0.06)
        return label

    def __tk_label_cr_end_time_txt(self, parent):
        label = ttk.Label(parent, text="2023/12/22 21:24:00", anchor="w", )
        label.place(relx=0.22, rely=0.75, relwidth=0.18, relheight=0.04)
        return label

    def __tk_radio_button_t_start(self, parent):
        rb = ttk.Radiobutton(parent, text="开始时间", value=1, command=self.setvalue_1)
        rb.place(relx=0.52, rely=0.68, relwidth=0.11, relheight=0.06)
        return rb
    def setvalue_1(self):
        set_sevalue(self.tk_radio_button_t_start.cget('value'))
        print(get_sevalue())
        pass

    def __tk_radio_button_t_end(self, parent):
        rb = ttk.Radiobutton(parent, text="结束时间", value=0, command=self.setvalue_2)
        rb.place(relx=0.67, rely=0.68, relwidth=0.11, relheight=0.06)
        return rb
    def setvalue_2(self):
        set_sevalue(self.tk_radio_button_t_end.cget('value'))
        print(get_sevalue())
        pass

    def __tk_button_time_set(self, parent):
        btn = ttk.Button(parent, text="设置", takefocus=False, command=self.button_time_set)
        btn.place(relx=0.52, rely=0.83, relwidth=0.07, relheight=0.04)
        return btn
    def button_time_set(self):
        select = get_sevalue()
        # 时间格式
        print(self.tk_input_rili.entry.get())
        t_time = self.tk_input_rili.entry.get()
        t_time += " "
        t_time += self.tk_select_box_clock_hour.get()
        t_time += ":" + self.tk_select_box_clock_min.get()
        print(t_time)
        time_year = t_time[:4]
        time_month = t_time[5:7]
        time_day = t_time[8:10]
        print(time_year, time_month, time_day)
        if (select == 1 and self.tk_select_box_clock_hour.get() != "小时"
                and self.tk_select_box_clock_min.get() != "分钟"):
            # 选课设置：开始时间
            self.tk_label_cr_start_time_txt.configure(text=t_time)
        elif (select == 0 and self.tk_select_box_clock_hour.get() != "小时"
              and self.tk_select_box_clock_min.get() != "分钟"):
            # 选课设置：结束时间
            self.tk_label_cr_end_time_txt.configure(text=t_time)
        else:
            messagebox.showinfo("信息提示","请选择设置的时间段：开始时间或者结束时间！")
        # sql更新
        course_time_set(self.tk_label_cr_start_time_txt.cget('text'),
                        self.tk_label_cr_end_time_txt.cget('text'), self.tk_select_box_course_type_se.get())
        # 刷新
        data = course_start_info()
        for item in self.tk_table_course_start_show.get_children():
            self.tk_table_course_start_show.delete(item)
        for col in data:
            self.tk_table_course_start_show.insert("", "end", values=tuple(col))
        pass

    def __tk_input_rili(self, parent):
        ipt = ttk.DateEntry(parent, )
        ipt.place(relx=0.52, rely=0.62, relwidth=0.25, relheight=0.06)
        return ipt

    def __tk_button_course_end(self, parent):
        btn = ttk.Button(parent, text="停止", takefocus=False, command=self.button_course_end)
        btn.place(relx=0.32, rely=0.83, relwidth=0.07, relheight=0.04)
        return btn
    def button_course_end(self):
        if self.tk_select_box_course_type_se.get() !="请选择":
            # sql
            course_flag_end(self.tk_select_box_course_type_se.get())
            data = course_start_info()
            for item in self.tk_table_course_start_show.get_children():
                self.tk_table_course_start_show.delete(item)
            for col in data:
                self.tk_table_course_start_show.insert("", "end", values=tuple(col))
            messagebox.showinfo("信息提示", "课程选课已停止！")
        else:
            messagebox.showerror("信息提示","请选择要终止选课的课程类型！")
        pass

    def __tk_table_course_start_show(self, parent):
        # 表头字段 表头宽度
        columns = {"课程类型": 112, "选课时间": 220, "选课结束": 220, "选课状态": 70, "": 8}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸
        tk_table.place(relx=0.00, rely=0.00, relwidth=1.00, relheight=0.56)
        self.create_bar(parent, tk_table, True, False, 0, 1, 729, 298, 730, 536)
        tk_table.bind('<<TreeviewSelect>>', self.course_start_find)
        return tk_table
    def course_start_find(self, event):
        selection = event.widget.selection()
        if selection:
            # 获取选中的行索引
            index = selection[0]
            # 获取行中的数据
            sel = event.widget.set(index)
            print(f'{sel}')
            # 刷新
            self.tk_select_box_course_type_se.current(0)
            self.tk_label_cr_start_time_txt.configure(text='')
            self.tk_label_cr_end_time_txt.configure(text='')
            # 填写
            data = ("请选择", "必修课", "选修课", "体育课", "文化课", "通识课")
            cindex = data.index(sel['课程类型'])
            self.tk_select_box_course_type_se.current(cindex)
            self.tk_label_cr_start_time_txt.configure(text=sel['选课时间'])
            self.tk_label_cr_end_time_txt.configure(text=sel['选课结束'])
        pass

    def __tk_select_box_clock_hour(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("小时","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24")
        cb.place(relx=0.80, rely=0.63, relwidth=0.07, relheight=0.04)
        return cb

    def __tk_select_box_clock_min(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("分钟","0","1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31","32","33","34","35","36","37","38","39","40","41","42","43","44","45","46","47","48","49","50","51","52","53","54","55","56","57","58","59","60")
        cb.place(relx=0.87, rely=0.63, relwidth=0.07, relheight=0.04)
        return cb

    # 课程管理
    def __tk_label_tc_ctpye_t(self, parent):
        label = ttk.Label(parent, text="课程类型：", anchor="center", )
        label.place(relx=0.71, rely=0.03, relwidth=0.08, relheight=0.06)
        return label

    def __tk_select_box_tc_ctpye(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("全部", "必修课", "选修课", "体育课", "文化课", "通识课")
        cb.place(relx=0.79, rely=0.04, relwidth=0.12, relheight=0.04)
        return cb

    def __tk_table_tc_tableshow(self, parent):
        # 表头字段 表头宽度
        columns = {"课程类型": 101, "课程名称": 142, "授课教师": 142, "教工编号": 101,'':20}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸

        tk_table.place(relx=0.00, rely=0.00, relwidth=0.70, relheight=0.95)
        self.create_bar(parent, tk_table, True, False, 0, 1, 510, 507, 730, 536)
        tk_table.bind('<<TreeviewSelect>>', self.tc_i_find)

        return tk_table
    def tc_i_find(self, event):
        selection = event.widget.selection()
        if selection:
            # 获取选中的行索引
            index = selection[0]
            # 获取行中的数据
            sel = event.widget.set(index)
            print(f'{sel}')
            # 刷新
            self.tk_label_ct_tpye_txt.configure(text="")
            self.tk_label_ct_name_txt.configure(text="")
            # self.tk_label_ct_tno_txt.configure(text="")
            self.tk_input_ct_tno_txt.delete(0, ttk.END)
            # 填写
            self.tk_label_ct_tpye_txt.configure(text=sel['课程类型'])
            self.tk_label_ct_name_txt.configure(text=sel['课程名称'])
            # self.tk_label_ct_tno_txt.configure(text=sel['教工编号'])
            self.tk_input_ct_tno_txt.insert(0, sel['教工编号'])
    pass

    def __tk_label_ct_tpye(self,parent):
        label = ttk.Label(parent,text="课程类型：",anchor="w", )
        label.place(relx=0.71, rely=0.35, relwidth=0.08, relheight=0.06)
        return label
    def __tk_label_ct_tpye_txt(self,parent):
        label = ttk.Label(parent,anchor="w", )
        label.place(relx=0.79, rely=0.35, relwidth=0.21, relheight=0.06)
        return label
    def __tk_label_ct_name_txt(self,parent):
        label = ttk.Label(parent,anchor="w", )
        label.place(relx=0.79, rely=0.41, relwidth=0.21, relheight=0.06)
        return label
    def __tk_label_ct_name(self,parent):
        label = ttk.Label(parent,text="课程名称：",anchor="w", )
        label.place(relx=0.71, rely=0.41, relwidth=0.08, relheight=0.06)
        return label

    def __tk_label_ct_tno(self, parent):
        label = ttk.Label(parent, text="教工编号：", anchor="w", )
        label.place(relx=0.71, rely=0.52, relwidth=0.08, relheight=0.06)
        return label

    def __tk_input_ct_tno_txt(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.79, rely=0.53, relwidth=0.205, relheight=0.04)
        return ipt

    def __tk_label_tc_fname(self, parent):
        label = ttk.Label(parent, text="课程名称：", anchor="w", )
        label.place(relx=0.71, rely=0.09, relwidth=0.08, relheight=0.06)
        return label

    def __tk_input_tc_fname_txt(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.79, rely=0.10, relwidth=0.205, relheight=0.04)
        return ipt

    def __tk_button_tc_find(self, parent):
        btn = ttk.Button(parent, text="查找", takefocus=False, command=self.tc_select_type)
        btn.place(relx=0.93, rely=0.04, relwidth=0.065, relheight=0.04)
        return btn
    def tc_select_type(self):
        if len(self.tk_input_tc_fname_txt.get()):
            self.print_tc_data(self.tk_select_box_tc_ctpye.get(), self.tk_input_tc_fname_txt.get())
        else:
            self.print_tc_data(self.tk_select_box_tc_ctpye.get())
            pass
        pass
    def print_tc_data(self, ctype, cname=None):
        data = tc_info_select(ctype, cname)
        for item in self.tk_table_tc_tableshow.get_children():
            self.tk_table_tc_tableshow.delete(item)
        for col in data:
            self.tk_table_tc_tableshow.insert("", "end", values=tuple(col))
        pass
    def __tk_button_tc_enter(self, parent):
        btn = ttk.Button(parent, text="更改", takefocus=False, command=self.button_tc_enter)
        btn.place(relx=0.93, rely=0.62, relwidth=0.065, relheight=0.04)
        return btn
    def button_tc_enter(self):
        # ssss
        fl_tcid = True
        if len(self.tk_input_ct_tno_txt.get()):
            # 查询教师是否存在
            if teacher_find_one(self.tk_input_ct_tno_txt.get()):
                # 当前课程的ID
                tc_id = course_find(self.tk_label_ct_name_txt.cget("text"))
                # 查找当前修改值是否为当前课程的授课教师，如果是，则弹出警告，否，则继续执行
                tecoid = teacher_find_course(self.tk_input_ct_tno_txt.get())
                for tcid in tecoid:
                    if tcid[0] == tc_id[0]:
                        messagebox.showinfo("信息提示", "课程已存在该授课教师，请重新选择！")
                        fl_tcid = False
                        break
                if fl_tcid is True:
                    # sql
                    teacher_course_update(self.tk_input_ct_tno_txt.get(), tc_id[0])
                    # 刷新
                    self.course_add_teacher_display()
                    messagebox.showinfo("信息提示", "修改成功！")
                    pass
            else:
                messagebox.showerror("信息提示", "工号不存在，请重新输入！")
                pass
        else:
            messagebox.showinfo("信息提示", "输入内容不能为空！")
            pass
        pass

    def __tk_frame_top_left_U(self, parent):
        frame = ttk.Frame(parent, )
        # frame.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        return frame

    def __tk_select_box_userno_tpye_find_se(self, parent):
        cb = ttk.Combobox(parent, state="readonly", )
        cb['values'] = ("请选择", "管理员", "教工", "学生")
        cb.place(relx=0.34, rely=0.02, relwidth=0.11, relheight=0.035)
        return cb

    def __tk_label_userno_findtxt(self, parent):
        label = ttk.Label(parent, text="账 号：", anchor="center", )
        label.place(relx=0.50, rely=0.015, relwidth=0.07, relheight=0.05)
        return label

    def __tk_input_userno_findtxt_in(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.57, rely=0.02, relwidth=0.20, relheight=0.04)
        return ipt

    def __tk_button_userno_find(self, parent):
        btn = ttk.Button(parent, text="查找", takefocus=False, command=self.button_userno_find)
        btn.place(relx=0.79, rely=0.02, relwidth=0.07, relheight=0.04)
        return btn
    def button_userno_find(self, select=True):
        if self.tk_select_box_userno_tpye_find_se.cget("text") != "请选择":
            if len(self.tk_input_userno_findtxt_in.get()):
                urol = self.users_info_show(self.tk_select_box_userno_tpye_find_se.get(), self.tk_input_userno_findtxt_in.get(), select)
            else:
                urol = self.users_info_show(self.tk_select_box_userno_tpye_find_se.get(), None, select)
                pass
            return urol
        pass
    def users_info_show(self, ctype, uno = None, select=True):
        data = users_info(ctype, uno, select)
        if select is True and data:
            for item in self.tk_table_userno_show.get_children():
                self.tk_table_userno_show.delete(item)
            for col in data:
                self.tk_table_userno_show.insert("", "end", values=tuple(col))
            return data
        else:
            return data
        pass
    def __tk_button_user_save_excl(self, parent):
        btn = ttk.Button(parent, text="导出表格", takefocus=False, command=self.button_user_save_excl)
        btn.place(relx=0.91, rely=0.02, relwidth=0.08, relheight=0.04)
        return btn
    def button_user_save_excl(self):
        if self.tk_select_box_userno_tpye_find_se.cget("text") != "请选择":
            filename = self.tk_select_box_userno_tpye_find_se.get()
            filename += "账号表"
            print(122)
            data = self.button_userno_find()
            rowl = self.button_userno_find(select=False)
            if data:
                save_file(filename, data, rowl)
        else:
            messagebox.showerror("信息提示", "选择数据不能为空！")
        pass
    def __tk_label_userno_tpye_find(self, parent):
        label = ttk.Label(parent, text="用户类型：", anchor="center", )
        label.place(relx=0.24, rely=0.018, relwidth=0.09, relheight=0.04)
        return label

    def __tk_table_userno_show(self, parent):
        # 表头字段 表头宽度
        columns = {"用户类型": 146, "用户账号": 146, "用户密码": 146, "用户密钥": 146,"":15}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='center')
            tk_table.column(text, anchor='center', width=width, stretch=True)  # stretch 不自动拉伸
        tk_table.bind('<<TreeviewSelect>>', self.user_find_select)
        tk_table.place(relx=0.00, rely=0.07, relwidth=0.99, relheight=0.70)
        self.create_bar(parent, tk_table, True, False, 0, 39.2, 732, 383, 740, 550)
        return tk_table
    def user_find_select(self, event):
        selection = event.widget.selection()
        if selection:
            # 获取选中的行索引
            index = selection[0]
            # 获取行中的数据
            sel = event.widget.set(index)
            print(f'{sel}')
            # 刷新
            self.tk_label_userno_tpye_txt.configure(text="")
            self.tk_label_userno_upintxt.configure(text="")
            self.tk_input_userno_password_in.delete(0, ttk.END)
            self.tk_input_userno_key_in.delete(0, ttk.END)
            # 填写
            self.tk_label_userno_tpye_txt.configure(text=sel['用户类型'])
            self.tk_label_userno_upintxt.configure(text=sel['用户账号'])
            self.tk_input_userno_password_in.insert(0, sel['用户密码'])
            self.tk_input_userno_key_in.insert(0, sel['用户密钥'])
        pass
    def __tk_label_userno_tpye(self, parent):
        label = ttk.Label(parent, text="用 户：", anchor="center", )
        label.place(relx=0.16, rely=0.79, relwidth=0.07, relheight=0.05)
        return label

    def __tk_label_userno_tpye_txt(self, parent):
        label = ttk.Label(parent, text="学生", anchor="w", )
        label.place(relx=0.22, rely=0.79, relwidth=0.07, relheight=0.05)
        return label

    def __tk_label_userno_up(self, parent):
        label = ttk.Label(parent, text="账 号：", anchor="center", )
        label.place(relx=0.16, rely=0.85, relwidth=0.07, relheight=0.05)
        return label

    def __tk_label_userno_upintxt(self, parent):
        label = ttk.Label(parent, text="账号", anchor="w", )
        label.place(relx=0.22, rely=0.85, relwidth=0.14, relheight=0.05)
        return label

    def __tk_label_userno_key(self, parent):
        label = ttk.Label(parent, text="密钥", anchor="center", )
        label.place(relx=0.55, rely=0.79, relwidth=0.07, relheight=0.05)
        return label

    def __tk_input_userno_key_in(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.62, rely=0.79, relwidth=0.20, relheight=0.05)
        return ipt

    def __tk_input_userno_password_in(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.62, rely=0.85, relwidth=0.20, relheight=0.05)
        return ipt

    def __tk_label_userno_password(self, parent):
        label = ttk.Label(parent, text="密码", anchor="center", )
        label.place(relx=0.55, rely=0.85, relwidth=0.07, relheight=0.05)
        return label

    def __tk_button_userno_update(self, parent):
        btn = ttk.Button(parent, text="修改", takefocus=False, command=self.button_userno_update)
        btn.place(relx=0.75, rely=0.93, relwidth=0.07, relheight=0.04)
        return btn
    def button_userno_update(self):
        if len(self.tk_input_userno_password_in.get()) and len(self.tk_input_userno_key_in.get()):
            # 修改密码或密钥
            users_info_update(self.tk_select_box_userno_tpye_find_se.get(),
                              self.tk_label_userno_upintxt.cget("text"),
                              self.tk_input_userno_password_in.get(),
                              self.tk_input_userno_key_in.get(),
                              )
            # 刷新
            self.tk_label_userno_tpye_txt.configure(text="")
            self.tk_label_userno_upintxt.configure(text="")
            self.tk_input_userno_password_in.delete(0, ttk.END)
            self.tk_input_userno_key_in.delete(0, ttk.END)
            # 更新数据
            self.button_userno_find()

            messagebox.showinfo("信息提示", "修改成功！")
        else:
            messagebox.showerror("信息提示", "修改的密钥和密码内容不能为空！")

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

    def course_add_display(self):
        self.tk_select_box_c_se_type.current(0)
        self.tk_input_c_id_txtin.delete(0, ttk.END)
        self.tk_input_c_name_txtin.delete(0, ttk.END)
        self.tk_input_c_credit_txtin.delete(0, ttk.END)
        self.tk_input_c_time_txtin.delete(0, ttk.END)
        self.tk_input_c_address_txtin.delete(0, ttk.END)
        pass
    def course_deup_display(self):
        self.tk_select_box_c_sel_types.current(0)
        self.tk_input_c_s_txtin.delete(0, ttk.END)
        data = course_info_low(True)
        for item in self.tk_table_c_up_show.get_children():
            self.tk_table_c_up_show.delete(item)
        for col in data:
            self.tk_table_c_up_show.insert("", "end", values=tuple(col))
        self.tk_select_box_c_se_up_type.current(0)
        self.tk_label_c_up_id_txtin.configure(text="")
        self.tk_input_c_up_name_txtin.delete(0, ttk.END)
        self.tk_input_c_up_credit_txtin.delete(0, ttk.END)
        self.tk_input_c_up_time_txtin.delete(0, ttk.END)
        self.tk_input_c_up_address_txtin.delete(0, ttk.END)
        self.tk_input_cnonum_in.delete(0, ttk.END)
        self.tk_input_limnum_in.delete(0, ttk.END)

        pass
    def course_i_display(self):
        self.tk_select_box_c_show_types.current(0)
        self.tk_input_ci_txtin.delete(0, ttk.END)
        data = course_info_low(True)
        for item in self.tk_table_c_info_show.get_children():
            self.tk_table_c_info_show.delete(item)
        for col in data:
            self.tk_table_c_info_show.insert("", "end", values=tuple(col))
        pass
    def course_start_display(self):
        self.tk_select_box_course_type_se.current(0)
        self.tk_select_box_clock_hour.current(0)
        self.tk_select_box_clock_min.current(0)
        self.tk_label_cr_start_time_txt.configure(text="")
        self.tk_label_cr_end_time_txt.configure(text="")
        data = course_start_info()
        for item in self.tk_table_course_start_show.get_children():
            self.tk_table_course_start_show.delete(item)
        for col in data:
            self.tk_table_course_start_show.insert("", "end", values=tuple(col))

        pass
    def course_add_teacher_display(self):

        data = teachercourse_info(True)
        for item in self.tk_table_tc_tableshow.get_children():
            self.tk_table_tc_tableshow.delete(item)
        for col in data:
            self.tk_table_tc_tableshow.insert("", "end", values=tuple(col))
        self.tk_select_box_tc_ctpye.current(0)
        self.tk_input_tc_fname_txt.delete(0, ttk.END)

        self.tk_label_ct_tpye_txt.configure(text="")
        self.tk_label_ct_name_txt.configure(text="")
        self.tk_input_ct_tno_txt.delete(0, ttk.END)
        pass

class AdminMenu(WinAGUI):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.__event_bind()
        # self.config(menu=self.create_menu())

    def create_menu(self):
        menu = ttk.Menu(self, tearoff=False)
        menu.add_cascade(label="学生管理", menu=self.menu_lpyscx3p(menu))
        menu.add_cascade(label="教工管理", menu=self.menu_lpysh9yx(menu))
        menu.add_cascade(label="院系管理", menu=self.menu_lpyto3tq(menu))
        menu.add_cascade(label="课程管理", command=self.course_info)
        menu.add_cascade(label="账号管理", command=self.users_up_info)
        menu.add_cascade(label="其他", menu=self.menu_lpywt6qx(menu))

        return menu
    def users_up_info(self):
        self.tk_frame_top_left_S.place_forget()
        self.tk_frame_top_left_S2.place_forget()
        self.tk_frame_top_left_S3.place_forget()
        self.tk_frame_top_left_T.place_forget()
        self.tk_frame_top_left_T2.place_forget()
        self.tk_frame_top_left_T3.place_forget()
        self.tk_frame_top_left_D.place_forget()
        self.tk_frame_top_left_D2.place_forget()
        self.tk_frame_top_left_D3.place_forget()
        self.tk_frame_top_left_C.place_forget()

        # 刷新
        self.tk_select_box_userno_tpye_find_se.current(0)
        self.tk_input_userno_findtxt_in.delete(0, ttk.END)
        self.tk_label_userno_tpye_txt.configure(text="")
        self.tk_label_userno_upintxt.configure(text="")
        self.tk_input_userno_password_in.delete(0, ttk.END)
        self.tk_input_userno_key_in.delete(0, ttk.END)

        self.tk_frame_top_left_U.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        for item in self.tk_table_userno_show.get_children():
            self.tk_table_userno_show.delete(item)
        pass

    def menu_lpyscx3p(self, parent):
        menu = ttk.Menu(parent, tearoff=False)
        menu.add_command(label="信息添加", command=self.stdata_add)
        menu.add_command(label="信息修改", command=self.stdata_update)
        menu.add_command(label="学生信息", command=self.student_info)
        return menu

    def menu_lpysh9yx(self, parent):
        menu = ttk.Menu(parent, tearoff=False)
        menu.add_command(label="信息添加", command=self.tedata_add)
        menu.add_command(label="信息修改", command=self.sedata_update)
        menu.add_command(label="教工信息", command=self.teacher_info)
        return menu

    def menu_lpyto3tq(self, parent):
        menu = ttk.Menu(parent, tearoff=False)
        menu.add_command(label="院系添加", command=self.dept_add)
        menu.add_command(label="院系修改", command=self.dept_update)
        menu.add_command(label="院系信息", command=self.dept_info)
        return menu
    def menu_user(self, parent):
        menu = ttk.Menu(parent, tearoff=False)
        return menu
    def menu_lpywt6qx(self, parent):
        menu = ttk.Menu(parent, tearoff=False)
        menu.add_command(label="退出", command=self.exit)
        return menu

    def stdata_add(self):

        self.tk_frame_top_left_S2.place_forget()
        self.tk_frame_top_left_S3.place_forget()
        self.tk_frame_top_left_T.place_forget()
        self.tk_frame_top_left_T2.place_forget()
        self.tk_frame_top_left_T3.place_forget()
        self.tk_frame_top_left_D.place_forget()
        self.tk_frame_top_left_D2.place_forget()
        self.tk_frame_top_left_D3.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_U.place_forget()

        # 初始化填写信息
        self.tk_input_sno_txtin.delete(0, ttk.END)
        self.tk_input_sname_txtin.delete(0, ttk.END)
        self.tk_input_class_txtin.delete(0, ttk.END)
        self.tk_select_box_ssex_se.current(0)
        self.tk_select_box_sage_se.current(0)
        self.tk_select_box_sdept_se.current(0)

        self.tk_frame_top_left_S.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        data = dept_data_get()
        data = tuple([item for sublist in data for item in sublist])
        self.tk_select_box_sdept_se['values'] = ("请选择",) + data
    def stdata_update(self):
        self.tk_frame_top_left_S.place_forget()
        self.tk_frame_top_left_S3.place_forget()
        self.tk_frame_top_left_T.place_forget()
        self.tk_frame_top_left_T2.place_forget()
        self.tk_frame_top_left_T3.place_forget()
        self.tk_frame_top_left_D.place_forget()
        self.tk_frame_top_left_D2.place_forget()
        self.tk_frame_top_left_D3.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_U.place_forget()

        # 初始化填写信息
        self.tk_input_sno_findin.delete(0, ttk.END)
        self.tk_label_sno_up_txtin.configure(text="")
        self.tk_input_sname_up_txtin.delete(0, ttk.END)
        self.tk_input_class_up_txtin.delete(0, ttk.END)
        self.tk_select_box_ssex_up_se.current(0)
        self.tk_select_box_sage_up_se.current(0)
        self.tk_select_box_sdept_up_se.current(0)

        self.tk_frame_top_left_S2.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        data = dept_data_get()
        data = tuple([item for sublist in data for item in sublist])
        self.tk_select_box_sdept_up_se['values'] = ("请选择",) + data
        data = st_find()
        for item in self.tk_table_st_find.get_children():
            self.tk_table_st_find.delete(item)
        for col in data:
            self.tk_table_st_find.insert("", "end", values=tuple(col))
        pass
    def student_info(self):
        self.tk_frame_top_left_S.place_forget()
        self.tk_frame_top_left_S2.place_forget()
        self.tk_frame_top_left_T.place_forget()
        self.tk_frame_top_left_T2.place_forget()
        self.tk_frame_top_left_T3.place_forget()
        self.tk_frame_top_left_D.place_forget()
        self.tk_frame_top_left_D2.place_forget()
        self.tk_frame_top_left_D3.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_U.place_forget()
        # 初始化
        self.tk_input_st_info_find_name.delete(0, ttk.END)
        self.student_info_show(self.tk_table_st_info_show)

        self.tk_frame_top_left_S3.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
    def student_info_show(self, student_info_table):
        data = student_info_add_low(True)
        for item in student_info_table.get_children():
            student_info_table.delete(item)

        for col in data:
            student_info_table.insert("", "end", values=tuple(col))
    def tedata_add(self):
        self.tk_frame_top_left_S.place_forget()
        self.tk_frame_top_left_S2.place_forget()
        self.tk_frame_top_left_S3.place_forget()
        self.tk_frame_top_left_T2.place_forget()
        self.tk_frame_top_left_T3.place_forget()
        self.tk_frame_top_left_D.place_forget()
        self.tk_frame_top_left_D2.place_forget()
        self.tk_frame_top_left_D3.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_U.place_forget()

        self.tk_frame_top_left_T.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        # 初始化填写信息
        self.tk_input_tno_txtin.delete(0, ttk.END)
        self.tk_input_tname_add_txtin.delete(0, ttk.END)
        self.tk_select_box_tsex_se.current(0)
        self.tk_select_box_tage_se.current(0)
        self.tk_select_box_teb_se.current(0)
        self.tk_select_box_tpt_se.current(0)
        self.tk_select_box_tdept_se.current(0)

        data = dept_data_get()
        data = tuple([item for sublist in data for item in sublist])
        self.tk_select_box_tdept_se['values'] = ("请选择",) + data
        pass
    def sedata_update(self):
        self.tk_frame_top_left_S.place_forget()
        self.tk_frame_top_left_S2.place_forget()
        self.tk_frame_top_left_S3.place_forget()
        self.tk_frame_top_left_T.place_forget()
        self.tk_frame_top_left_T3.place_forget()
        self.tk_frame_top_left_D.place_forget()
        self.tk_frame_top_left_D2.place_forget()
        self.tk_frame_top_left_D3.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_U.place_forget()

        self.tk_frame_top_left_T2.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        # 初始化填写信息
        self.tk_input_tno_findin.delete(0, ttk.END)
        self.tk_label_tno_up_txtin.configure(text="")
        self.tk_input_tname_up_txtin.delete(0, ttk.END)
        self.tk_select_box_tsex_up_se.current(0)
        self.tk_select_box_tage_up_se.current(0)
        self.tk_select_box_teb_up_se.current(0)
        self.tk_select_box_tpt_up_se.current(0)
        self.tk_select_box_tdept_up_se.current(0)

        data = dept_data_get()
        data = tuple([item for sublist in data for item in sublist])
        self.tk_select_box_tdept_up_se['values'] = ("请选择",) + data

        self.teacher_info_show(self.tk_table_te_find)
        pass
    def teacher_info(self):
        self.tk_frame_top_left_S.place_forget()
        self.tk_frame_top_left_S2.place_forget()
        self.tk_frame_top_left_S3.place_forget()
        self.tk_frame_top_left_T.place_forget()
        self.tk_frame_top_left_T2.place_forget()
        self.tk_frame_top_left_D.place_forget()
        self.tk_frame_top_left_D2.place_forget()
        self.tk_frame_top_left_D3.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_U.place_forget()
        # 初始化文本框及信息
        self.tk_input_e_info_find_name.delete(0, ttk.END)

        self.tk_frame_top_left_T3.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        self.teacher_info_show(self.tk_table_se_info_show)
    def teacher_info_show(self, teacher_info_table):
        data = teacher_info_showall()
        for item in teacher_info_table.get_children():
            teacher_info_table.delete(item)

        for col in data:
            teacher_info_table.insert("", "end", values=tuple(col))
    def dept_add(self):
        self.tk_frame_top_left_S.place_forget()
        self.tk_frame_top_left_S2.place_forget()
        self.tk_frame_top_left_S3.place_forget()
        self.tk_frame_top_left_T.place_forget()
        self.tk_frame_top_left_T2.place_forget()
        self.tk_frame_top_left_T3.place_forget()
        self.tk_frame_top_left_D2.place_forget()
        self.tk_frame_top_left_D3.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_U.place_forget()

        self.tk_frame_top_left_D.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)

        self.tk_input_dno_txtin.delete(0, ttk.END)
        self.tk_input_dname_txtin.delete(0, ttk.END)
        self.tk_input_dmanager_txtin.delete(0, ttk.END)
    def dept_update(self):
        self.tk_frame_top_left_S.place_forget()
        self.tk_frame_top_left_S2.place_forget()
        self.tk_frame_top_left_S3.place_forget()
        self.tk_frame_top_left_T.place_forget()
        self.tk_frame_top_left_T2.place_forget()
        self.tk_frame_top_left_T3.place_forget()
        self.tk_frame_top_left_D.place_forget()
        self.tk_frame_top_left_D3.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_U.place_forget()

        self.tk_frame_top_left_D2.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        self.dept_update_find_show()

    def dept_update_find_show(self):
        data = dept_info()
        for item in self.tk_table_de_find.get_children():
            self.tk_table_de_find.delete(item)

        for col in data:
            self.tk_table_de_find.insert("", "end", values=tuple(col))
        # 清空信息
        self.tk_label_dno_up_txt.configure(text="")
        self.tk_input_dname_up_txtin.delete(0, ttk.END)
        self.tk_input_dmanager_up_txtin.delete(0, ttk.END)
        pass

    def dept_info(self):
        self.tk_frame_top_left_S.place_forget()
        self.tk_frame_top_left_S2.place_forget()
        self.tk_frame_top_left_S3.place_forget()
        self.tk_frame_top_left_T.place_forget()
        self.tk_frame_top_left_T2.place_forget()
        self.tk_frame_top_left_T3.place_forget()
        self.tk_frame_top_left_D.place_forget()
        self.tk_frame_top_left_D2.place_forget()
        self.tk_frame_top_left_C.place_forget()
        self.tk_frame_top_left_U.place_forget()

        self.tk_frame_top_left_D3.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        # sql 更新数据：学号，姓名，班级
        self.dept_info_show()
    def dept_info_show(self):
        data = dept_info()
        for item in self.tk_table_de_info_show.get_children():
            self.tk_table_de_info_show.delete(item)
        for col in data:
            self.tk_table_de_info_show.insert("", "end", values=tuple(col))
        pass
    # 课程管理
    def course_info(self):
        self.tk_frame_top_left_S.place_forget()
        self.tk_frame_top_left_S2.place_forget()
        self.tk_frame_top_left_S3.place_forget()
        self.tk_frame_top_left_T.place_forget()
        self.tk_frame_top_left_T2.place_forget()
        self.tk_frame_top_left_T3.place_forget()
        self.tk_frame_top_left_D.place_forget()
        self.tk_frame_top_left_D2.place_forget()
        self.tk_frame_top_left_D3.place_forget()
        self.tk_frame_top_left_U.place_forget()

        self.tk_frame_top_left_C.place(relx=0.00, rely=0.00, relwidth=0.77, relheight=0.98)
        self.course_add_display()
        self.course_deup_display()
        self.course_i_display()
        self.course_start_display()
        self.course_add_teacher_display()
        pass

    def exit(self):
        self.master.destroy()

    def __event_bind(self):
        pass

class TcGUI(ttk.Toplevel):
    def __init__(self):
        super().__init__()
        self.__win()
        self.tk_table_te_course_info = self.__tk_table_te_course_info(self)
        self.tk_label_c_txt = self.__tk_label_c_txt(self)
        self.tk_label_c_txtin = self.__tk_label_c_txtin(self)
        self.tk_label_tno_c = self.__tk_label_tno_c(self)
        self.tk_input_tno_c_txtin = self.__tk_input_tno_c_txtin(self)
        self.tk_button_t_c_update = self.__tk_button_t_c_update(self)
        self.tk_button_t_c_exit = self.__tk_button_t_c_exit(self)
        # 刷新
        self.tk_input_tno_c_txtin.delete(0, ttk.END)
        self.tk_label_c_txtin.configure(text="")

    def __win(self):
        self.title("课程授课教师更改")
        # 设置窗口大小、居中
        width = 580
        height = 480
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

    def __tk_table_te_course_info(self, parent):
        # 表头字段 表头宽度
        columns = {"教工编号": 143, "教师名称": 143, "课程名": 239}
        tk_table = ttk.Treeview(parent, show="headings", columns=list(columns), )
        for text, width in columns.items():  # 批量设置列属性
            tk_table.heading(text, text=text, anchor='w')
            tk_table.column(text, anchor='w', width=width, stretch=False)  # stretch 不自动拉伸

        tk_table.bind('<<TreeviewSelect>>', self.find_select)
        tk_table.place(relx=0.005, rely=0.005, relwidth=0.99, relheight=0.71)
        self.create_bar(parent, tk_table, True, False, 0, 3, 477, 268, 480, 380)
        return tk_table
    def find_select(self, event):
        selection = event.widget.selection()
        if selection:
            # 获取选中的行索引
            index = selection[0]
            # 获取行中的数据
            sel = event.widget.set(index)
            print(f'{sel}')
            # 刷新
            self.tk_input_tno_c_txtin.delete(0, ttk.END)
            self.tk_label_c_txtin.configure(text="")
            # 填写
            self.tk_label_c_txtin.configure(text=sel['课程名'])
            self.tk_input_tno_c_txtin.insert(0, sel['教工编号'])

        pass
    def __tk_label_c_txt(self, parent):
        label = ttk.Label(parent, text="课程名：", anchor="center", )
        label.place(relx=0.04, rely=0.74, relwidth=0.13, relheight=0.08)
        return label

    def __tk_label_c_txtin(self, parent):
        label = ttk.Label(parent, text="标签", anchor="w", )
        label.place(relx=0.15, rely=0.74, relwidth=0.31, relheight=0.08)
        return label

    def __tk_label_tno_c(self, parent):
        label = ttk.Label(parent, text="教工号：", anchor="w", )
        label.place(relx=0.04, rely=0.82, relwidth=0.13, relheight=0.08)
        return label

    def __tk_input_tno_c_txtin(self, parent):
        ipt = ttk.Entry(parent, )
        ipt.place(relx=0.15, rely=0.82, relwidth=0.25, relheight=0.08)
        return ipt

    def __tk_button_t_c_update(self, parent):
        btn = ttk.Button(parent, text="修改", takefocus=False, command=self.button_t_c_update)
        btn.place(relx=0.67, rely=0.82, relwidth=0.10, relheight=0.08)
        return btn
    def button_t_c_update(self):
        flagid = True
        if len(self.tk_input_tno_c_txtin.get()):
            # 查询教师是否存在
            if teacher_find_one(self.tk_input_tno_c_txtin.get()):
                # 当前课程的ID
                courseid = course_find(self.tk_label_c_txtin.cget("text"))
                # 查找当前修改值是否为当前课程的授课教师，如果是，则弹出警告，否，则继续执行
                tecoid = teacher_find_course(self.tk_input_tno_c_txtin.get())
                for tcid in tecoid:
                    if tcid[0] == courseid[0]:
                        messagebox.showinfo("信息提示", "课程已存在此授课教师，请重新选择！")
                        flagid = False
                        break
                if flagid is True:
                    # sql
                    teacher_course_update(self.tk_input_tno_c_txtin.get(), courseid[0])
                    # 刷新
                    self.tk_input_tno_c_txtin.delete(0, ttk.END)
                    self.tk_label_c_txtin.configure(text="")
                    data = teacher_course_find(self.tk_input_tno_c_txtin.get())
                    for item in self.tk_table_te_course_info.get_children():
                        self.tk_table_te_course_info.delete(item)

                    for col in data:
                        self.tk_table_te_course_info.insert("", "end", values=tuple(col))
                    messagebox.showinfo("信息提示", "修改成功！")
                    pass
            else:
                messagebox.showerror("信息提示", "工号不存在，请重新输入！")
                pass
        else:
            messagebox.showinfo("信息提示", "输入内容不能为空！")
            pass
        pass

    def __tk_button_t_c_exit(self, parent):
        btn = ttk.Button(parent, text="退出", takefocus=False, command=self.destroy)
        btn.place(relx=0.895, rely=0.82, relwidth=0.10, relheight=0.08)
        return btn

class Tinc(TcGUI):
    def __init__(self):
        super().__init__()
        self.__event_bind()
        self.info_show()

    def __event_bind(self):
        pass
    def info_show(self):
        global Ctno
        data = teacher_course_find(Ctno)
        for item in self.tk_table_te_course_info.get_children():
            self.tk_table_te_course_info.delete(item)

        for col in data:
            self.tk_table_te_course_info.insert("", "end", values=tuple(col))
        pass

# 测试例
if __name__ == "__main__":
    mysql_connect_csdb()
    win = ttk.Window()

    win.title("管理端")
    ttk.Style("solar")
    # 设置窗口大小、居中
    width = 1570
    height = 1150
    screenwidth = win.winfo_screenwidth()
    screenheight = win.winfo_screenheight()
    geometry = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
    win.geometry(geometry)
    win.minsize(width=width, height=height)

    app_admin = AdminMenu(win)
    win.config(menu=app_admin.create_menu())
    win.mainloop()

    mysql2_close()