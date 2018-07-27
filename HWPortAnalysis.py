from openpyxl import Workbook
import os

filepath = r"E:\Career\Project\2017年江苏电信QoS\调研资料\南京\221.224.178.101_20170824.log"


with open(os.path.abspath(filepath), 'rt',
          encoding='utf-8') as default_file:
    all_config = default_file.read()

ports_list = list(all_config.split('\n#\n'))
pcount = 1
portresult = []

while pcount < len(ports_list):
    port_name = ports_list[pcount].split()[1]
    if "Eth-Trunk" in port_name:
        # 下行接口带有相关域配置的话，摘出相应的端口名，描述和域名
        if "bas" in ports_list[pcount]:
            domain = ((ports_list[pcount].split('#')[1]).split('\n')[1]).split()[-1]
            line_countd = len(ports_list[pcount].split('\n'))
            line_currentd = 0
            while line_currentd < line_countd:
                if "description" in ports_list[pcount].split('\n')[line_currentd]:
                    descr = ports_list[pcount].split('\n')[line_currentd].split(maxsplit=1)[1]
                line_currentd = line_currentd + 1
            domain_port = [port_name, descr, "", "所在域为:%s" % domain]
            portresult.append(domain_port)

        # 下行端口配置了组播业务的话，摘取端口号，描述并记录业务类型为组播业务
        elif "igmp" in ports_list[pcount] or "pim" in ports_list[pcount]:
            line_countd = len(ports_list[pcount].split('\n'))
            line_currentd = 0
            while line_currentd < line_countd:
                if "description" in ports_list[pcount].split('\n')[line_currentd]:
                    descr = ports_list[pcount].split('\n')[line_currentd].split(maxsplit=1)[1]
                line_currentd = line_currentd + 1
            multicast_port = [port_name, descr, "组播业务", ""]
            portresult.append(multicast_port)

        # 下行口配置vpn的话，摘取端口号，描述和配置的VPN
        elif "vpn-instance" in ports_list[pcount]:
            line_count = len(ports_list[pcount].split('\n'))
            line_current = 0
            while line_current < line_count:
                if "vpn-instance" in ports_list[pcount].split('\n')[line_current]:
                    vpn_name = ports_list[pcount].split('\n')[line_current].split()[-1]
                    line_countd = len(ports_list[pcount].split('\n'))
                    line_currentd = 0
                    while line_currentd < line_countd:
                        if "description" in ports_list[pcount].split('\n')[line_currentd]:
                            descr = ports_list[pcount].split('\n')[line_currentd].split(maxsplit=1)[1]
                        line_currentd = line_currentd + 1
                    vpn_port = [port_name, descr, "", "调用的vpn为:%s" % vpn_name]
                    portresult.append(vpn_port)
                line_current = line_current + 1

        # 上下行其他端口，只截取端口号和描述
        else:
            line_count = len(ports_list[pcount].split('\n'))
            line_current = 0
            while line_current < line_count:
                if "description" in ports_list[pcount].split('\n')[line_current]:
                    descr = ports_list[pcount].split('\n')[line_current].split(maxsplit=1)[1]
                    other_eth = [port_name, descr, "", ""]
                    portresult.append(other_eth)
                line_current = line_current + 1


    else:
        if "undo shutdown" in ports_list[pcount]:
            line_count = len(ports_list[pcount].split('\n'))
            line_current = 0
            while line_current < line_count:
                if "description" in ports_list[pcount].split('\n')[line_current]:
                    descr = ports_list[pcount].split('\n')[line_current].split(maxsplit=1)[1]
                    other_port = [port_name, descr, "", ""]
                    portresult.append(other_port)
                line_current = line_current + 1
    pcount = pcount + 1

print(portresult)
print(len(portresult))

hwwb = Workbook()

hwportsheet = hwwb.active

hwportsheet.title = "华为端口使用现状"

# 编写sheet的列头：

hwportsheet['A1'].value = '端口名'
hwportsheet['B1'].value = '端口描述'
hwportsheet['C1'].value = '业务类型'
hwportsheet['D1'].value = '备注'

# 以下为批量转化list型变量内容到xlsx文件对应位置
row1 = 1
col1 = 0

for row1 in range(2, len(portresult) + 2):  # 写入数据
    for col1 in range(1, len(portresult[row1 - 2]) + 1):
        _ = hwportsheet.cell(row=row1, column=col1, value=str(portresult[row1 - 2][col1 - 1]))

hwwb.save(filename="华为端口分析结果.xlsx")
print("保存成功")
