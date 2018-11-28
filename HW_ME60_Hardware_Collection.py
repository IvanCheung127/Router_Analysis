import re
import tkinter.filedialog


# 母卡分析函数
# 依赖命令display elabel brief
# 输出母卡槽位号和母卡类型

def MCard_Collection(data):
    MCard_Collection = []
    data_split_mid1 = re.split('=\n', data)[1].split('\n')
    for card_item in data_split_mid1:
        if 'BSU' in card_item:
            data_split_mid2 = card_item.split()
            MCard_Num = data_split_mid2[1]
            MCard_Type = data_split_mid2[2]
            MCard_Collection.append([MCard_Num, MCard_Type])

    return MCard_Collection


# 子卡分析函数
# 依赖命令display device pic-status
# 输出端口号和子卡类型

def DCard_Collection(data):
    data_split_mid = re.split('Logic_down\s*\n|\n\-', data)[2].split('\n')
    print(data_split_mid)
    daughter_card_num = len(data_split_mid)
    print(daughter_card_num)
    cur_dcard_num = 0
    DCard_Info = []
    while cur_dcard_num < daughter_card_num:
        cur_info_split = data_split_mid[cur_dcard_num].split()
        print(cur_info_split)
        if cur_info_split[3] != 'DVSU_SP_CARD':
            i = 0
            while i <= (int(cur_info_split[4]) - 1):
                Port_num = '{Card_num}/{DCard_num}/{Port_Num}'.format(Card_num=cur_info_split[0],
                                                                      DCard_num=cur_info_split[1], Port_Num=i)
                DCard_Type = cur_info_split[3]
                DCard_Info.append(
                    [Port_num, DCard_Type])
                i += 1
        cur_dcard_num += 1

    return DCard_Info


# 光模块分析函数
# 依赖命令display elabel optical-module brief
# 输出端口号和光模块类型

def OpticalModule_Collection(data):
    data_split_mid_1 = re.split('=\n', data)
    data_split_mid_2 = data_split_mid_1[1].split()
    count = 0
    Port_Type_Sum = []
    while count < len(data_split_mid_2):
        if re.match(r'[a-zA-Z]+\d+\/\d+\/+\d+', data_split_mid_2[count]) is not None:
            print(data_split_mid_2[count])
            Slot_Num = re.sub('[a-zA-Z]+', '', data_split_mid_2[count])
            Port_Type = data_split_mid_2[count + 1]
            Port_Type_Sum.append([Slot_Num, Port_Type])

        count += 1

    return Port_Type_Sum


# 端口分析函数
# 依赖命令display interface description  | exclude [0-9]*\/*[0-9]*\/*[0-9]+\.[0-9]+
# 输出端口号、带宽、物理状态、协议状态及端口描述

def Port_Collection(data):
    data_split_mid_1 = re.split('Description\s*\n', data)
    data_split_mid_2 = data_split_mid_1[1].split('\n')
    port_count = 0
    Port_Description_Sum = []
    while port_count < len(data_split_mid_2):
        data_split_mid_3 = data_split_mid_2[port_count].split(maxsplit=3)
        if 'GE' in data_split_mid_3[0]:
            if '(' in data_split_mid_3[0]:
                data_split_mid_4 = re.split('\(|\)', data_split_mid_3[0])
                print(data_split_mid_4)
                Slot_Num = re.sub('[a-zA-Z]+', '', data_split_mid_4[0])
                Port_BW = data_split_mid_4[1]
                Phy_Status = data_split_mid_3[1]
                Pro_Status = data_split_mid_3[2]
                Port_Desc = data_split_mid_3[3]
                Port_Description_Sum.append([Slot_Num, Port_BW, Phy_Status, Pro_Status, Port_Desc])
            else:
                Slot_Num = re.sub('[a-zA-Z]+', '', data_split_mid_3[0])
                Port_BW = '1G'
                Phy_Status = data_split_mid_3[1]
                Pro_Status = data_split_mid_3[2]
                Port_Desc = data_split_mid_3[3]
                Port_Description_Sum.append([Slot_Num, Port_BW, Phy_Status, Pro_Status, Port_Desc])

        port_count += 1

    return Port_Description_Sum


# 主流程函数
# 包含打开文件->分段配置->解析输出各部分结果->拼接入excel表

def Main_Process():
    file_path = tkinter.filedialog.askopenfilename()
    if file_path is not '':
        with open(file_path, 'rt', encoding='utf-8') as default_file:
            split_config = re.split(r'\<\S+\>', default_file.read())
            for config_content in split_config:
                if "display elabel brief" in config_content:
                    MCard_Info = MCard_Collection(split_config)
                    print(MCard_Info)
                elif "display device pic-status" in split_config:
                    DCard_Info = DCard_Collection(split_config)
                    print(DCard_Info)
                elif "display elabel optical-module brief" in split_config:
                    OpticalModule_Info = OpticalModule_Collection(split_config)
                    print(OpticalModule_Info)
                elif "display interface description" in split_config:
                    Port_Description_Info = Port_Collection(split_config)
                    print(Port_Description_Info)




Main_Process()