import re

test1 = '''<CQRH-PA-CMNET-BAS09-ME60-X16>display interface description  | exclude [0-9]*\/*[0-9]*\/*[0-9]+\.[0-9]+
PHY: Physical
*down: administratively down
^down: standby
(l): loopback
(s): spoofing
(E): E-Trunk down
(b): BFD down
(B): Bit-error-detection down
(e): ETHOAM down
(d): Dampening Suppressed
Interface                     PHY     Protocol Description            
Aux0/0/1                      down    down     HUAWEI, Aux0/0/1 Interface
Eth-Trunk0                    up      up       to CQXY-PB-CMNET-RT01-NE5000E Eth-Trunk20 40G
Eth-Trunk1                    up      up       to CQRH-PA-CMNET-BAS10-ME60-X16 Eth-Trunk1 40G
Eth-Trunk2                    up      down     to CQRH-MC-CMNET-SW11-7600-X E-Trunk1 40G
Eth-Trunk3                    up      down     TO CQRH-MC-CMNET-SW11-7610 eth-trunk3 40G
Eth-Trunk4                    up      up       TO CQLZW-PB-CMNET-RT01-NE5000E-X16ACluster Eth-Trunk73 40G
Eth-Trunk5                    up      down     TO CQRH-MC-CMNET-SW11-7600-X 40G
Eth-Trunk207                  down    down     HUAWEI, Eth-Trunk207 Interface
GE0/0/0                       down    down     HUAWEI, GigabitEthernet0/0/0 Interface
GE1/0/0(10G)                  up      up       to CQXY-PB-CMNET-RT01-NE5000E G1/14/1/13 10G
GE1/0/1(10G)                  up      up       to CQXY-PB-CMNET-RT01-NE5000E G1/14/1/14 10G
GE1/0/2(10G)                  up      up       to CQXY-PB-CMNET-RT01-NE5000E G2/14/1/13 10G
GE1/0/3(10G)                  up      up       to CQXY-PB-CMNET-RT01-NE5000E G2/14/1/14 10G
GE1/0/4(10G)                  up      up       TO CQXY-S9306-SW-9306-10G-2/0/8
GE1/1/0(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7610 G1/0/9 10G
GE1/1/1(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7610 G1/0/10 10G
GE1/1/2(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7610 G1/0/11 10G
GE1/1/3(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7610 G1/0/12 10G
GE1/1/4(10G)                  up      down     TO_JianCaiShiChang-OLT002-0/19/0-(ID-9902-20180411-00006)
GE4/0/0(10G)                  up      up       HUAWEI, GigabitEthernet4/0/0 Interface
GE4/0/1(10G)                  up      up       HUAWEI, GigabitEthernet4/0/1 Interface
GE4/0/2(10G)                  up      up       HUAWEI, GigabitEthernet4/0/2 Interface
GE4/0/3(10G)                  up      up       HUAWEI, GigabitEthernet4/0/3 Interface
GE4/0/4(10G)                  *down   down     HUAWEI, GigabitEthernet4/0/4 Interface
GE4/1/0(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7600-X G 1/0/1
GE4/1/1(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7600-X G 1/0/2
GE4/1/2(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7600-X G 1/0/3
GE4/1/3(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7600-X G 1/0/4
GE4/1/4(10G)                  up      down     TO_KangZhuangMeiDi-OLT002-0/17/0_(ID-9902-20180418-00016)
GE5/0/0(10G)                  up      up       TO CQLZW-PB-CMNET-RT01-NE5000E-X16ACluster G1/16/1/10 10G
GE5/0/1(10G)                  up      up       TO CQLZW-PB-CMNET-RT01-NE5000E-X16ACluster G1/16/1/11 10G
GE5/0/2(10G)                  up      up       TO CQLZW-PB-CMNET-RT01-NE5000E-X16ACluster G1/16/1/12 10G
GE5/0/3(10G)                  up      up       TO CQLZW-PB-CMNET-RT01-NE5000E-X16ACluster G1/16/1/13 10G
GE5/0/4(10G)                  down    down     HUAWEI, GigabitEthernet5/0/4 Interface
GE5/1/0(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7600-X XG1/0/45 10G
GE5/1/1(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7600-X XG1/0/46 10G
GE5/1/2(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7600-X XG1/0/47 10G
GE5/1/3(10G)                  up      up       TO CQRH-MC-CMNET-SW11-7600-X XG1/0/48 10G
GE5/1/4(10G)                  down    down     HUAWEI, GigabitEthernet5/1/4 Interface
GE12/0/0                      *down   down     HUAWEI, GigabitEthernet12/0/0 Interface
GE12/0/1(10G)                 *down   down     HUAWEI, GigabitEthernet12/0/1 Interface
GE12/0/2(10G)                 *down   down     HUAWEI, GigabitEthernet12/0/2 Interface
GE12/0/3(10G)                 *down   down     HUAWEI, GigabitEthernet12/0/3 Interface
GE12/0/4(10G)                 *down   down     HUAWEI, GigabitEthernet12/0/4 Interface
Loop0                         up      up(s)    HUAWEI, LoopBack0 Interface
NULL0                         up      up(s)    HUAWEI, NULL0 Interface
VT0                           up      up(s)    HUAWEI, Virtual-Template0 Interface'''

data_split_mid_1 = re.split('Description\s*\n', test1)
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
            Port_Description_Sum.append([Slot_Num,Port_BW,Phy_Status,Pro_Status,Port_Desc])
        else:
            Slot_Num = re.sub('[a-zA-Z]+', '', data_split_mid_3[0])
            Port_BW = '1G'
            Phy_Status = data_split_mid_3[1]
            Pro_Status = data_split_mid_3[2]
            Port_Desc = data_split_mid_3[3]
            Port_Description_Sum.append([Slot_Num, Port_BW, Phy_Status, Pro_Status, Port_Desc])

    port_count += 1


print(Port_Description_Sum)
