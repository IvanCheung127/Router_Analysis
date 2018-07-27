import http.client
import tkinter.messagebox
import tkinter.filedialog
import base64
import os
from ico1 import img
from tkinter import *
from openpyxl import Workbook
from datetime import datetime


def per_url_check(filepath):
    with open(filepath, 'rt',
              encoding='utf-8') as default_file:
        all_url = default_file.read()
        url_list = all_url.split('\n')
        url_count = 0
        result_summary = []
        while url_count < len(url_list) :
            try:
                conn = http.client.HTTPConnection(url_list[url_count], timeout=5)
                conn.request("GET", "/")
                r1 = conn.getresponse()
                url_result = [url_list[url_count], r1.status, r1.reason]
            except Exception as er1:
                url_result = [url_list[url_count], "访问失败", er1]

            result_summary.append(url_result)
            url_count = url_count + 1


        # 生成输出excel

        hwwb = Workbook()

        hwportsheet = hwwb.active

        hwportsheet.title = "网页访问状态结果"

        # 编写sheet的列头：

        hwportsheet['A1'].value = '网址'
        hwportsheet['B1'].value = '返回状态码'
        hwportsheet['C1'].value = '备注'

        # 以下为批量转化list型变量内容到xlsx文件对应位置

        for row1 in range(2, len(result_summary) + 2):  # 写入数据
            for col1 in range(1, len(result_summary[row1 - 2]) + 1):
                _ = hwportsheet.cell(row=row1, column=col1, value=str(result_summary[row1 - 2][col1 - 1]))
        devname = re.split(r'[\\/]', filepath)[-1].split()[0]
        curtime = datetime.now().strftime('%Y-%m-%d %Hh%Mm%Ss')
        filetitle = devname + str(curtime)
        hwwb.save(filename="%s 网页访问状态结果.xlsx" % filetitle)


def about_message():
    message_content = ('Author：IC\n'
                       'Version：1.0\n'
                       '使用方法：\n'
                       '	将域名每行一个记录到txt之类的文本当中。\n'
                       '	使用程序读取文本中的域名顺序建立http链接，并记录返回的状态码输出到excel中。')
    tkinter.messagebox.showinfo("关于", message_content,)


def run_urlcheck():
    file_path = tkinter.filedialog.askopenfilename()
    if file_path is not '':
        per_url_check(file_path)
        tkinter.messagebox.showinfo("提示", "批量网页状态码返回完毕！")
    else:
        return


class App(object):
    def __init__(self, master):
        self.com1 = Button(master, text='批量网页状态码输出', command=run_urlcheck, width=25)
        self.com1.pack(side=LEFT)
        self.com2 = Button(master, text='关于', command=about_message, width=25)
        self.com2.pack(side=RIGHT)


root = Tk()
root.title('批量网络状态码获取')
root.geometry("400x80")
with open("tmp.ico","wb+") as tmp:
    tmp.write(base64.b64decode(img))

root.iconbitmap("tmp.ico")
os.remove("tmp.ico")


app = App(root)
root.mainloop()
