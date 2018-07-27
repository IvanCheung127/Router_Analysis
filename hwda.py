import tkinter.messagebox
import tkinter.filedialog
import tkinter
import re
import base64
import os
from ico1 import img
from tkinter import Button
from tkinter import Tk
from openpyxl import Workbook


def hwda(filepath):
    with open(filepath, 'rt',
              encoding='utf-8') as default_file:
        all_config = default_file.read()
        domain_all = \
        all_config.split(r'display current-configuration configuration ip-pool | include pool|gateway', maxsplit=1)[0]
        ipp_all = \
        all_config.split(r'display current-configuration configuration ip-pool | include pool|gateway', maxsplit=1)[-1]
        domain_config_mid = re.split(r'(domain\s+\S*\n)', domain_all)
        domain_count = 0
        domain_result = []
        while domain_count < len(domain_config_mid) - 1:
            if "domain" in domain_config_mid[domain_count] and "ip-pool" in domain_config_mid[domain_count + 1]:
                domain_name = domain_config_mid[domain_count].split()[1]
                ipp_count = 0
                ipp_config_mid = domain_config_mid[domain_count + 1].split('\n')
                while ipp_count < len(ipp_config_mid) - 1:
                    ipp_name = ipp_config_mid[ipp_count].split()[1]
                    ipp_network = ''
                    ipp_wildmask = ''
                    if re.search(r'ip\spool\s%s\sbas\s\S+\n' % ipp_name, ipp_all) is not None:
                        ipp_network_mid = re.split(r'ip\spool\s%s\sbas\s\S+\n' % ipp_name, ipp_all)[1].split()[1]
                        ipp_network = ipp_network_mid.split(r'.')[0] + '.' + ipp_network_mid.split(r'.')[1] + '.' + \
                                      ipp_network_mid.split(r'.')[2] + '.' + str(
                            int(ipp_network_mid.split(r'.')[3]) - 1)
                        ipp_wildmask_mid = re.split(r'ip\spool\s%s\sbas\s\S+\n' % ipp_name, ipp_all)[1].split()[2]
                        ipp_wildmask = str(255 - int(ipp_wildmask_mid.split(r'.')[0])) + '.' + str(
                            255 - int(ipp_wildmask_mid.split(r'.')[1])) + '.' + str(
                            255 - int(ipp_wildmask_mid.split(r'.')[2])) + '.' + str(
                            255 - int(ipp_wildmask_mid.split(r'.')[3]))
                        ad_result = [domain_name, ipp_name, ipp_network, ipp_wildmask]
                        domain_result.append(ad_result)
                        ipp_count = ipp_count + 1
                    else:
                        ipp_count = ipp_count + 1

                domain_count = domain_count + 2
            else:
                domain_count = domain_count + 1


 # 生成输出excel
    hwwb = Workbook()

    hwportsheet = hwwb.active

    hwportsheet.title = "华为域使用现状调研"

    # 编写sheet的列头：

    hwportsheet['A1'].value = '域名'
    hwportsheet['B1'].value = '地址池名'
    hwportsheet['C1'].value = '地址池网段'
    hwportsheet['D1'].value = '地址池反掩码'
    hwportsheet['E1'].value = '业务类型'
    hwportsheet['F1'].value = '备注'

    # 以下为批量转化list型变量内容到xlsx文件对应位置

    for row1 in range(2, len(domain_result) + 2):  # 写入数据
        for col1 in range(1, len(domain_result[row1 - 2]) + 1):
            _ = hwportsheet.cell(row=row1, column=col1, value=str(domain_result[row1 - 2][col1 - 1]))
    devname = re.split(r'[\\/]',filepath)[-1].split()[0]
    hwwb.save(filename="%s 域调研结果.xlsx" % devname)

def run_hwda():
    hw_path = tkinter.filedialog.askopenfilename()
    if hw_path is not '':
        hwda(hw_path)
        tkinter.messagebox.showinfo("提示", "华为域分析完毕！")
    else:
        return

def about_message():
    message_content = ("Author：IC\n"
                       "Version：1.0\n"
                       "使用方法：\n"
                       "华为设备：摘取\n"
                       "display current-configuration configuration aaa | include domain|pool\n"
                       "display current-configuration configuration ip-pool | include pool|gateway\n"
                       "根据相应信息，摘取域与地址池的关系，并输出成excel\n")
    tkinter.messagebox.showinfo("关于", message_content,)

class App(object):
    def __init__(self, master):
        self.com1 = Button(master, text='华为设备域调研', command=run_hwda, width=25)
        self.com1.pack()
        self.com2 = Button(master, text='关于', command=about_message, width=25)
        self.com2.pack()


root = Tk()
root.title('端口调研程序')
root.geometry("300x70")
with open("tmp.ico","wb+") as tmp:
    tmp.write(base64.b64decode(img))

root.iconbitmap("tmp.ico")
os.remove("tmp.ico")

app = App(root)
root.mainloop()

