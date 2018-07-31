import re
Test_String = '''<SC-NJ-LCDQ-BAS-1.MAN.ME60>display ospf interface  all 

         OSPF Process 1 with Router ID 182.135.124.14
                 Interfaces 

 Area: 0.0.0.0          (MPLS TE not enabled)

 Interface: 182.135.124.14 (LoopBack0)
 Cost: 0       State: P-2-P     Type: P2P       MTU: 1500  
 Timers: Hello 10 , Dead 40 , Poll  120 , Retransmit 5 , Transmit Delay 1 
 Silent interface, No hellos

 Interface: 182.135.124.15 (LoopBack1)
 Cost: 0       State: P-2-P     Type: P2P       MTU: 1500  
 Timers: Hello 10 , Dead 40 , Poll  120 , Retransmit 5 , Transmit Delay 1 
 Silent interface, No hellos

 Interface: 182.135.124.126 (GigabitEthernet3/0/0)
 Cost: 10      State: BDR       Type: Broadcast    MTU: 1586  
 Priority: 1
 Designated Router: 182.135.124.125
 Backup Designated Router: 182.135.124.126
 Timers: Hello 10 , Dead 40 , Poll  120 , Retransmit 5 , Transmit Delay 1 

 Interface: 125.65.250.194 (GigabitEthernet8/1/1)
 Cost: 10      State: BDR       Type: Broadcast    MTU: 1586  
 Priority: 1
 Designated Router: 125.65.250.193
 Backup Designated Router: 125.65.250.194
 Timers: Hello 10 , Dead 40 , Poll  120 , Retransmit 5 , Transmit Delay 1 

 Interface: 182.135.124.142 (GigabitEthernet4/0/0)
 Cost: 10      State: BDR       Type: Broadcast    MTU: 1586  
 Priority: 1
 Designated Router: 182.135.124.141
 Backup Designated Router: 182.135.124.142
 Timers: Hello 10 , Dead 40 , Poll  120 , Retransmit 5 , Transmit Delay 1 

 Interface: 222.214.142.198 (GigabitEthernet6/0/0)
 Cost: 10      State: BDR       Type: Broadcast    MTU: 1586  
 Priority: 1
 Designated Router: 222.214.142.197
 Backup Designated Router: 222.214.142.198
 Timers: Hello 10 , Dead 40 , Poll  120 , Retransmit 5 , Transmit Delay 1 

 Interface: 222.214.142.134 (GigabitEthernet7/0/0)
 Cost: 10      State: BDR       Type: Broadcast    MTU: 1586  
 Priority: 1
 Designated Router: 222.214.142.133
 Backup Designated Router: 222.214.142.134
 Timers: Hello 10 , Dead 40 , Poll  120 , Retransmit 5 , Transmit Delay 1 

 Interface: 125.65.250.190 (GigabitEthernet8/1/0)
 Cost: 10      State: BDR       Type: Broadcast    MTU: 1586  
 Priority: 1
 Designated Router: 125.65.250.189
 Backup Designated Router: 125.65.250.190
 Timers: Hello 10 , Dead 40 , Poll  120 , Retransmit 5 , Transmit Delay 1 
 
<SC-NJ-LCDQ-BAS-1.MAN.ME60>'''


class Port_Info:
    def __init__(self, Dev_Name):
        self.Dev_Name = Dev_Name
        self.Dev_Ports = ''
        self.Port_Flag = ''
        self.Dev_V4_IP = ''
        self.Dev_V6_IP = ''
        self.OSPF_Type = ''
        self.Port_MTU = ''


Data_Init = re.split('OSPF Process | with Router ID |Area\:|Interface\:',Test_String)
Dev_Name = re.split('<|>',Data_Init[0])[1]
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

print(HW_BAS_Result)



