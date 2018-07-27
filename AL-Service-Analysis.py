import re
from openpyxl import Workbook

with open(r"E:\Career\Project\2017年山东QoS\青岛剩余SR\端口调研log\124.129.29.191 操作开始时间20170831102032 service调研输出.log", 'rt',
          encoding='utf-8') as default_file:
    all_config = default_file.read()

v_or_i_config_mid = list(re.split(r'(vprn\s+\d+\s+customer\s+\d+\s+create|ies\s+\d+\s+customer\s+\d+\s+create)', all_config))
v_or_i_count = 1
portresult = []
while v_or_i_count < len(v_or_i_config_mid):
    v_or_i_config_mid2 = v_or_i_config_mid[v_or_i_count]
    if re.match(r'vprn\s+\d+\s+customer\s+\d+\s+create|ies\s+\d+\s+customer\s+\d+\s+create',
                v_or_i_config_mid2) is not None:
        v_or_i_config = v_or_i_config_mid2 + v_or_i_config_mid[v_or_i_count + 1]
        if 'no shutdown' in v_or_i_config:
            v_or_i_name = ' '.join(v_or_i_config.split('\n')[0].split()[0:4])
            v_or_i_descr = ''
            if "description" in v_or_i_config.split('\n')[1]:
                v_or_i_descr = v_or_i_config.split('\n')[1].split(maxsplit=1)[1]
            interface_config_mid = list(re.split(r'(interface\s+\S*\s+create)', v_or_i_config))
            interface_count = 1
            while interface_count < len(interface_config_mid):
                interface_mid2 = interface_config_mid[interface_count]
                if re.match(r'interface\s+\S*\s+create', interface_mid2) is not None:
                    interface_config = interface_mid2 + interface_config_mid[interface_count + 1]
                    interface_name = interface_config.split('\n')[0].split()[1]
                    interface_descr = ''
                    if "description" in interface_config.split('\n')[1]:
                        interface_descr = interface_config.split('\n')[1].split(maxsplit=1)[1]
                    sap_config_mid = list(re.split(r'(sap\s+\S*\s+create)', interface_config))
                    sap_count = 1
                    while sap_count < len(sap_config_mid):
                        sap_config_mid2 = sap_config_mid[sap_count]
                        if re.match(r'sap\s+\S*\s+create', sap_config_mid2) is not None:
                            sap_config = sap_config_mid2 + sap_config_mid[sap_count + 1]
                            sap_name = sap_config.split('\n')[0].split()[1]
                            ingress_qos_policy = ''
                            egress_qos_policy = ''
                            if re.search(r'ingress\s*\n\s*qos\s+\d+', sap_config) is not None and re.search(r'egress\s*\n\s*qos\s+\d+', sap_config) is not None:
                                ingress_qos_policy = re.split(r'(ingress\s*\n\s*qos\s+\d+)', sap_config)[1].split()[2]
                                egress_qos_policy = re.split(r'(egress\s*\n\s*qos\s+\d+)', sap_config)[1].split()[2]

                            elif re.search(r'ingress\s*\n\s*qos\s+\d+', sap_config) is not None:
                                ingress_qos_policy = re.split(r'(ingress\s*\n\s*qos\s+\d+)', sap_config)[1].split()[2]
                            elif re.search(r'egress\s*\n\s*qos\s+\d+', sap_config) is not None:
                                egress_qos_policy = re.split(r'(egress\s*\n\s*qos\s+\d+)', sap_config)[1].split()[2]

                            ALServiceResult = [v_or_i_name, v_or_i_descr, interface_name, interface_descr, sap_name,
                                          ingress_qos_policy,
                                          egress_qos_policy]
                            portresult.append(ALServiceResult)
                            sap_count = sap_count + 2

                        else:
                            sap_count = sap_count + 1


                    interface_count = interface_count + 2

                else:
                    interface_count = interface_count + 1


            v_or_i_count = v_or_i_count + 2

        else:
            v_or_i_count = v_or_i_count + 1

    else:
        v_or_i_count = v_or_i_count + 1

print(portresult)

# 生成输出excel
hwwb = Workbook()

hwportsheet = hwwb.active

hwportsheet.title = "AC 7750 service接口调研结果"

# 编写sheet的列头：
hwportsheet['A1'].value = '服务名'
hwportsheet['B1'].value = '服务描述'
hwportsheet['C1'].value = '端口名'
hwportsheet['D1'].value = '端口描述'
hwportsheet['E1'].value = 'sap名称'
hwportsheet['F1'].value = 'sap ingress'
hwportsheet['G1'].value = 'sap engress'
hwportsheet['H1'].value = '备注'

# 以下为批量转化list型变量内容到xlsx文件对应位置

for row1 in range(2, len(portresult) + 2):  # 写入数据
    for col1 in range(1, len(portresult[row1 - 2]) + 1):
        _ = hwportsheet.cell(row=row1, column=col1, value=str(portresult[row1 - 2][col1 - 1]))

hwwb.save(filename="AC 7750 service接口调研结果.xlsx")
print("保存成功")
