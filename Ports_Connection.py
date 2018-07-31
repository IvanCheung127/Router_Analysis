import re


class Port_Info:
    def __init__(self, Dev_Name):
        self.Dev_Name = Dev_Name
        self.Dev_Ports = ''
        self.Port_Flag = ''
        self.Dev_V4_IP = ''
        self.Dev_V6_IP = ''
        self.Port_Pro = ''
        self.Port_MTU = ''


def HW_Bas_OSPF_analysis(HW_OSPF_Config):
    Data_Init = re.split('OSPF Process | with Router ID |Area\:|Interface\:', HW_OSPF_Config)
    Dev_Name = re.split('<|>', Data_Init[0])[1]
    Part_Num = 4
    HW_BAS_Result = []
    while Part_Num < len(Data_Init):
        Data_Mid_1 = re.split('\(|\)|Type:|MTU:|\s+', Data_Init[Part_Num])
        Port_Instance = Port_Info(Dev_Name)
        Port_Instance.Dev_Ports = Data_Mid_1[3]
        Port_Instance.Dev_V4_IP = Data_Mid_1[1]
        if 'LoopBack' in Port_Instance.Dev_Ports:
            Port_Instance.Port_Flag = 0
        else:
            Port_Instance.Port_Flag = 1
        Port_Instance.OSPF_Type = Data_Mid_1[11]
        HW_BAS_Result.append(Port_Instance)
        Part_Num += 1


