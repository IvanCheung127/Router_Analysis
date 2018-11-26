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

data_split_mid_1 = re.split('Logic_down|\n\-',test1)[2]
print(data_split_mid_1)

port_info=[]