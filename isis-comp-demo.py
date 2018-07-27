import tkinter.messagebox
import tkinter.filedialog
import os
import base64
from tkinter import *
from ico1 import img


###以下函数循环处理isis初始数据，并按照***排序###
def HW_N5K_isis_data_format(init_data):
    data_split_mid = re.split('\n', init_data)
    isis_final_result = []
    line_count = 0
    while line_count < len(data_split_mid) - 2:
        #        print(data_split_mid[line_count])
        for _ in data_split_mid[line_count]:
            space_counts = 0
            data_split_mid2 = data_split_mid[line_count].strip()
            space_split_list = data_split_mid2.split(' ')
            space_counts += len(space_split_list)
        #        print(space_counts)
        if space_counts < 37:
            data_split_mid3 = re.split('\s+', data_split_mid2)
            if len(data_split_mid3) == 1:
                sysid_end = data_split_mid3[0]
                isis_data_mid = re.split('\s+', data_split_mid[line_count - 1])
                isis_data_final = [isis_data_mid[0] + sysid_end] + isis_data_mid[1:7]
                isis_final_result.append(isis_data_final)
            elif len(data_split_mid3) == 2:
                sysid_end = data_split_mid3[0]
                cirid_end = data_split_mid3[1]
                isis_data_mid = re.split('\s+', data_split_mid[line_count - 1])
                isis_data_final = [isis_data_mid[0] + sysid_end] + [isis_data_mid[1]] + [
                    isis_data_mid[2] + cirid_end] + isis_data_mid[3:7]
                isis_final_result.append(isis_data_final)
        else:
            isis_data_final = re.split('\s+', data_split_mid2)
            isis_final_result.append(isis_data_final)

        line_count += 1

    ###以下代码去除重复统计数据，判断标准isis应无重复接口###
    datacount = 1
    while datacount < len(isis_final_result):
        if isis_final_result[datacount][1] == isis_final_result[datacount - 1][1]:
            if len(isis_final_result[datacount][0]) > len(isis_final_result[datacount - 1][0]):
                del isis_final_result[datacount - 1]
            else:
                del isis_final_result[datacount]

        datacount += 1
    ###按照对端sysid排序###
    isis_final_result.sort(key=lambda x: x[0])
    ###按照端口排序###
    # isis_final_result.sort(key=lambda x: x[1])
    return (isis_final_result)


def save_file(contents):
    file_name = tkinter.filedialog.asksaveasfile()
    try:
        file_name.write(contents)
        file_name.close()
    except Exception as err:
        print(err)
        tkinter.messagebox.showerror("警告", "存储失败！！！")


def isis_result(filepath):
    with open(filepath, 'rt', encoding='utf-8') as default_file:
        isis_info_split = re.split('Peer information|------\n|Total Peer\(s\)\:', default_file.read())
        isis_process_num = re.split('[()]', isis_info_split[1])[1]
        isis_peer_num = isis_info_split[3].split()[0]
        isis_info_init = isis_info_split[2]
        isis_result = HW_N5K_isis_data_format(isis_info_init)
    return isis_process_num, isis_peer_num, isis_result


def isis_compare():
    try:
        isis_log_before_path = tkinter.filedialog.askopenfilename(title="割接前isis采集文件")
        isis_log_before_result = isis_result(isis_log_before_path)
        tkinter.messagebox.showinfo("提示", "统计完成，请选择割接后采集文件！")
        isis_log_after_path = tkinter.filedialog.askopenfilename(title="割接后isis采集文件")
        if isis_log_after_path is not '':
            isis_log_after_result = isis_result(isis_log_after_path)
            isis_before_process_num = isis_log_before_result[0]
            isis_before_peer_num = isis_log_before_result[1]
            isis_after_process_num = isis_log_after_result[0]
            isis_after_peer_num = isis_log_after_result[1]
            isis_before_more = set(tuple(i) for i in isis_log_before_result[2]).difference(
                set(tuple(i) for i in isis_log_after_result[2]))
            if isis_before_more == set():
                isis_before_more = "无"
            isis_after_more = set(tuple(i) for i in isis_log_after_result[2]).difference(
                set(tuple(i) for i in isis_log_before_result[2]))
            if isis_after_more == set():
                isis_after_more = "无"
            isis_summary = tkinter.messagebox.askyesnocancel('ISIS 比较结果',
                                                             'ISIS 割接前进程号为{a};\nISIS割接前peer数为{b};\nISIS 割接后进程号为{c};\nISIS割接后peer数为{d};\nISIS割接后缺少的peer为{e};\nISIS割接后新增的peer为{f};\n是否需要导出结果？'
                                                             .format(
                                                                 a=isis_before_process_num, b=isis_before_peer_num,
                                                                 c=isis_after_process_num, d=isis_after_peer_num,
                                                                 e=isis_before_more,
                                                                 f=isis_after_more))
            if isis_summary is True:
                isis_comp_result = 'ISIS 割接前进程号为{a};\nISIS割接前peer数为{b};\nISIS 割接后进程号为{c};\nISIS割接后peer数为{d};\nISIS割接后缺少的peer为{e};\nISIS割接后新增的peer为{f};\n'.format(
                    a=isis_before_process_num, b=isis_before_peer_num,
                    c=isis_after_process_num, d=isis_after_peer_num, e=isis_before_more,
                    f=isis_after_more)
                save_file(isis_comp_result)

        else:
            tkinter.messagebox.showerror("警告", "文件选择有误，请重新选择！！！")
            return
    except:
        tkinter.messagebox.showerror("警告", "文件选择有误，请重新选择！！！")



def about_message():
    message_content = ("Author：IC\n"
                       "Version：alpha demo\n"
                       "使用方法：\n"
                       "华为NE5KE:摘取disp isis peer做比较,适用宽度80的显示，默认一行内容空格总数37\n")
    tkinter.messagebox.showinfo("关于", message_content,)


class App(object):
    def __init__(self, master):
        self.com1 = Button(master, text='华为NE5KE isis比对', command=isis_compare, width=25)
        self.com1.pack()
        self.com2 = Button(master, text='关于', command=about_message, width=25)
        self.com2.pack()


root = Tk()
root.title('割接助手demo')
root.geometry("300x75")
with open("tmp.ico","wb+") as tmp:
    tmp.write(base64.b64decode(img))

root.iconbitmap("tmp.ico")
os.remove("tmp.ico")


app = App(root)
root.mainloop()