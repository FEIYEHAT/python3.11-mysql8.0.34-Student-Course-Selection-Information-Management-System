import os
import pandas as pd
import tkinter as tk
from tkinter import filedialog

def batch_add(filename):
    df = pd.read_excel(filename)
    print(df)
    data = df.values.tolist()
    return data
    pass

# 保存文件
# 形参：@filename: 文件名称
#      @data：数据
#      @low: 列名称
def save_file(filename, data, low, sel = False):
    window = tk.Tk()
    window.withdraw()  # 隐藏主窗口
    # 将查询结果转换为DataFrame格式
    if sel is False:
        df = pd.DataFrame(data, columns=[i[0] for i in low])
    else:
        df = pd.DataFrame(columns=[i[0] for i in low])

    folder_path = os.path.join(os.getenv('USERPROFILE'), 'Documents')
    # 打开文件对话框，获取用户选择的文件路径
    default_file_name = filename
    file_types = [('Excel files', '*.xlsx'), ('All files', '*.*')]
    save_path = filedialog.asksaveasfilename(initialdir=folder_path, initialfile=default_file_name,
                                             defaultextension='.xlsx', filetypes=file_types)
    # 将DataFrame保存为Excel文件
    if save_path:
        df.to_excel(save_path, index=False)
    else:
        print('取消导出表格！')
    # 关闭窗口
    window.destroy()

# 选择文件函数
def select_file():
    # 创建Tkinter窗口
    window = tk.Tk()
    window.withdraw()  # 隐藏主窗口

    folder_path = os.path.join(os.getenv('USERPROFILE'), 'Documents')
    # 打开文件对话框，获取用户选择的文件路径
    file_path = filedialog.askopenfilename(initialdir=folder_path)
    # 输出选择的文件路径
    # 关闭窗口
    window.destroy()
    # 返回文件路径
    return file_path
