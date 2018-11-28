import re

test1 = '''<SC-PZH-MD-BAS-1.MAN.ME60>display device pic-status 
Pic-status information in Chassis 1:
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
SLOT PIC Status     Type                   Port_count Init_result   Logic_down  
1    0   Registered ETH_10XGE_CARD         10         SUCCESS       SUCCESS     
2    0   Registered LAN_WAN_10G_TM_CARD    1          SUCCESS       SUCCESS     
2    1   Registered LAN_WAN_10G_TM_CARD    1          SUCCESS       SUCCESS     
3    0   Registered LAN_WAN_10G_TM_CARD    1          SUCCESS       SUCCESS     
3    1   Registered ETH_10XGF_TM_CARD      10         SUCCESS       SUCCESS     
4    0   Registered DVSU_SP_CARD           0          SUCCESS       SUCCESS     
5    0   Registered ETH_10XGE_CARD         10         SUCCESS       SUCCESS     
6    0   Registered ETH_10XGF_TM_CARD      10         SUCCESS       SUCCESS     
6    1   Registered LAN_WAN_10G_TM_CARD    1          SUCCESS       SUCCESS     
7    0   Registered LAN_WAN_10G_TM_CARD    1          SUCCESS       SUCCESS     
8    0   Registered LAN_WAN_2x10GX_T_CARD  2          SUCCESS       SUCCESS     
9    0   Registered LAN_WAN_2x10GX_T_CARD  2          SUCCESS       SUCCESS     
9    1   Registered LAN_WAN_2x10GX_T_CARD  2          SUCCESS       SUCCESS     
10   0   Registered LAN_WAN_2x10GX_T_CARD  2          SUCCESS       SUCCESS     
10   1   Registered LAN_WAN_2x10GX_T_CARD  2          SUCCESS       SUCCESS     
11   0   Registered LAN_WAN_2x10GX_T_CARD  2          SUCCESS       SUCCESS     
12   0   Registered LAN_WAN_2x10GX_T_CARD  2          SUCCESS       SUCCESS     
12   1   Registered LAN_WAN_2x10GX_T_CARD  2          SUCCESS       SUCCESS     
13   0   Registered DVSU_SP_CARD           0          SUCCESS       SUCCESS     
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'''

data_split_mid = re.split('Logic_down\s*\n|\n\-', test1)[2].split('\n')
print(data_split_mid)
daughter_card_num = len(data_split_mid)
print(daughter_card_num)
cur_dcard_num = 0
hardware_info = []
while cur_dcard_num < daughter_card_num:
    cur_info_split = data_split_mid[cur_dcard_num].split()
    print(cur_info_split)
    if cur_info_split[3] != 'DVSU_SP_CARD':
        i = 0
        while i <= (int(cur_info_split[4]) - 1):
            slot_num = '{Card_num}/{DCard_num}/{Port_Num}'.format(Card_num=cur_info_split[0],
                                                                  DCard_num=cur_info_split[1], Port_Num=i)
            Card_Type = ''
            DCard_Type = cur_info_split[3]
            Optical_Type = ''
            Phy_Status = ''
            Pro_Status = ''
            Port_Desc = ''
            Port_BW = ''
            hardware_info.append([slot_num,Card_Type,DCard_Type,Optical_Type,Phy_Status,Phy_Status,Port_Desc,Port_BW])
            i += 1
    cur_dcard_num += 1
print(hardware_info)