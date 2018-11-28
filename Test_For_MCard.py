import re


test1 = '''<SC-PZH-DDK-BAS-1.MAN.ME60>display elabel brief 
Slot      BoardType            BarCode                         Description
================================================================================
BSU 1      ME03BSUF21          210305327110D7000151            BSUF-21                          
  PIC 0    ME03EAGFE0          030LLF10C5000853                BP20-E-10*GEBase-SFP             
BSU 2      ME03BSUF21          210305327110C6002087            BSUF-21                          
  PIC 0    ME03E1XXE0          030HEE10D6001419                BP20-E-1*10GBase LAN/WAN-XFP     
  PIC 1    ME03E1XXE0          030HEE10B8000971                BP20-E-1*10GBase LAN/WAN-XFP     
BSU 3      ME03BSUF21          210305327110B8000977            BSUF-21                          
  PIC 0    ME03E1XXE0          030HEE10B8000989                BP20-E-1*10GBase LAN/WAN-XFP     
  PIC 1    
BSU 4      ME03BSUF21          210305327110B8000972            BSUF-21                          
  PIC 0    ME03E1XXE0          030HEE10B8000988                BP20-E-1*10GBase LAN/WAN-XFP     
  PIC 1    ME03EAGFE0          030LLF10D6000317                BP20-E-10*GEBase-SFP             
BSU 5      ME03LPUF50CA0       210305462910H4000164            BSUF-51                          
  PIC 0    ME03EFGFE0          030PYN10H4000015                BP51-E-24xGE-SFP                 
BSU 6      ME03BSUF21          210305327110C6002084            BSUF-21                          
  PIC 0    ME03EAGFE0          030LLF10C6000350                BP20-E-10*GEBase-SFP             
  PIC 1    ME03E1XXE0          030HEE10D6001434                BP20-E-1*10GBase LAN/WAN-XFP     
BSU 7      ME03BSUF21          210305327110D7000158            BSUF-21                          
  PIC 0    ME03E1XXE0          030HEE10D6001433                BP20-E-1*10GBase LAN/WAN-XFP     
BSU 8      ME03BSUF21          210305327110D7000156            BSUF-21                          
  PIC 0    ME03E1XXE0          030HEE10D6001431                BP20-E-1*10GBase LAN/WAN-XFP     
  PIC 1    ME03EAGFE0          030LLF10D6000327                BP20-E-10*GEBase-SFP             
BSU 9      ME03BSUF40          210305313010E4000202            BSUF-40                          
  PIC 0    ME03L2XXB0          030NFR10EB000141                BP40-E-2*10GBase LAN/WAN-XFP     
  PIC 1    ME03L2XXB0          030NFR10E4000083                BP40-E-2*10GBase LAN/WAN-XFP     
BSU 10     ME03BSUF40          210305313010H3000057            BSUF-40                          
  PIC 0    ME03L2XXB0          030NFR10H3000013                BP40-E-2*10GBase LAN/WAN-XFP     
  PIC 1    ME03L2XXB0          030NFR10H3000040                BP40-E-2*10GBase LAN/WAN-XFP     
VSU 11     ME03VSUF8000        210305449610EC000393            VSUF80                           
BSU 12     ME03BSUF40          210305313010EC000619            BSUF-40                          
  PIC 0    ME03L2XXB0          030NFR10EB000085                BP40-E-2*10GBase LAN/WAN-XFP     
BSU 13     ME03BSUF40          210305313010H3000056            BSUF-40                          
  PIC 0    ME03L2XXB0          030NFR10H3000018                BP40-E-2*10GBase LAN/WAN-XFP     
  PIC 1    ME03L2XXB0          030NFR10H3000025                BP40-E-2*10GBase LAN/WAN-XFP     
BSU 14     ME03BSUF40          210305313010H3000062            BSUF-40                          
  PIC 0    ME03L2XXB0          030NFR10H3000031                BP40-E-2*10GBase LAN/WAN-XFP     
  PIC 1    ME03L2XXB0          030NFR10H3000006                BP40-E-2*10GBase LAN/WAN-XFP     
VSU 15     ME03VSUF8011        210305763410J7000166            VSUF80-J                         
VSU 16     ME03VSUF8000        210305449610EC000368            VSUF80                           
MPU 17     ME03MPUB4           210305313110EC000008            MPUB                             
MPU 18     ME03MPUB4           210305313110EC000007            MPUB                             
SFU 19     ME03SFU200B0        210305392510GC000079            SFUI-200-B                       
SFU 20     ME03SFU200B0        210305392510GC000099            SFUI-200-B                       
SFU 21     ME03SFU200B0        210305392510GC000076            SFUI-200-B                       
SFU 22     ME03SFU200B0        210305392510GC000080            SFUI-200-B                       
PWR 25     
  PEM 0    CR52PEMB            2102120560P0EB003456                                             
  PEM 1    CR52PEMB            2102120560P0EB003452                                             
  PEM 2    CR52PEMB            2102120560P0EB003462                                             
  PEM 3    CR52PEMB            2102120560P0EB003447                                             
PWR 26     
  PEM 0    CR52PEMB            2102120560P0EB003459                                             
  PEM 1    CR52PEMB            2102120560P0EB003453                                             
  PEM 2    CR52PEMB            2102120560P0EB003443                                             
  PEM 3    CR52PEMB            2102120560P0EB003444                                             
FAN 27     CR52FCBH            2102120562P0EB001699                                             
FAN 28     CR52FCBH            2102120562P0EB001691                                             
FAN 29     CR52FCBH            2102120562P0EB001666                                             
FAN 30     CR52FCBH            2102120562P0EB001655                                             '''

MCard_Collection = []
data_split_mid1 = re.split('=\n',test1)[1].split('\n')
for card_item in data_split_mid1:
    if 'BSU' in card_item:
        data_split_mid2 = card_item.split()
        MCard_Num = data_split_mid2[1]
        MCard_Type = data_split_mid2[2]
        MCard_Collection.append([MCard_Num,MCard_Type])


print(MCard_Collection)
