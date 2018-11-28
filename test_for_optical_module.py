import re

test1 = '''<SC-PZH-MD-BAS-1.MAN.ME60>display elabel optical-module brief 
Port      BoardType          BarCode         VendorName        Description
===============================================================================
Eth1/0/0  MXPD-243S          HA12200220522    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth1/0/1  RTXM191-400        BP1016B60859     WTD               1200Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth1/0/2  HFBR-5710L         AM07287FK6       AVAGO             1200Mb/s-LC-550m
                                                                (0.05mm)-270m(0.
                                                                0625mm)

Eth1/0/3  HFBR-5710L         AM091795ST       AVAGO             1200Mb/s-LC-550m
                                                                (0.05mm)-270m(0.
                                                                0625mm)

Eth1/0/4  MXPD-243S-F        MA10180040559    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth1/0/5  FTLF8519P2BNL-HW   PKG4839          FINISAR CORP.     2100Mb/s-850nm-L
                                                                C-500m(0.05mm)-3
                                                                00m(0.0625mm)

Eth1/0/6  WXTRPGEAS1         WX1107112500     WXZTE             1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth1/0/7  RTXM191-400        100048562352     WTD               1200Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth2/0/0  PT745F-81-1D       A0811674246      NEOPHOTONICS      9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth2/1/0  PT745F-81-1D       A0811656996      NEOPHOTONICS      9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth3/0/0  PT745F-81-1D       A0811674247      NEOPHOTONICS      9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth3/1/0  RTXM191-400        EC141400031000   WTD               1200Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth3/1/1  MXPD-243S          HA12200220541    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth3/1/2  MXPD-243S-F        HA11200260738    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth3/1/3  MXPD-243S          HA12200220544    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth5/0/0  RTXM191-400        BP1016B60861     WTD               1200Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth5/0/2  HFBR-5710L         AM07287E7H       AVAGO             1200Mb/s-LC-550m
                                                                (0.05mm)-270m(0.
                                                                0625mm)

Eth5/0/3  RTXM191-400        BP0932331622     WTD               1200Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth5/0/4  MXPD-243S          HA12200140879    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth5/0/5  FTLF8519P2BNL-HW   PKG483A          FINISAR CORP.     2100Mb/s-850nm-L
                                                                C-500m(0.05mm)-3
                                                                00m(0.0625mm)

Eth5/0/6  WXTRPGEAS1         WX1107121179     WXZTE             1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth5/0/7  MXPD-243S-F        MA12050530683    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth6/0/0  MXPD-243S          HA12200220520    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth6/0/1  MXPD-243S          HA12200220519    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth6/0/2  MXPD-243S          HA12200220550    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth6/0/3  MXPD-243S          HA12200220515    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth6/0/4  MXPD-243S          HA12200220521    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth6/0/5  MXPD-243S          MB12300100896    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth6/0/6  MXPD-243S-F        MA10060370719    HG GENUINE        1300Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth6/1/0  FTLX1413M3BCL-HW   UQ10P9P          FINISAR CORP.     8500Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth7/0/0  FTLX1413M3BCL-HW   UQ10N40          FINISAR CORP.     8500Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth8/0/0  SXP3104NV-H1       41T040214404     SumitomoElectric  10000Mb/s-1310nm
                                                                -LC-10km(0.009mm
                                                                )

Eth8/0/1  SXP3104NV-H1       41T040213428     SumitomoElectric  10000Mb/s-1310nm
                                                                -LC-10km(0.009mm
                                                                )

Eth9/0/0  TRF5016FN-GA420    T14K73080        Oclaro Inc.       10000Mb/s-1310nm
                                                                -LC-10km(0.009mm
                                                                )

Eth9/0/1  FTLX1413M3BCL-HW   UR30VCL          FINISAR CORP.     8500Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth9/1/0  TRF5016FN-GA420    T14H79437        Oclaro Inc.       10000Mb/s-1310nm
                                                                -LC-10km(0.009mm
                                                                )

Eth9/1/1  TRF5016FN-GA420    T14H79496        Oclaro Inc.       10000Mb/s-1310nm
                                                                -LC-10km(0.009mm
                                                                )

Eth10/0/0 LTX1305-BC+        N5659A03870      Hisense           9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth10/0/1 LTX1305-BC+        N5651A03632      Hisense           9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth10/1/0 LTX1305-BC+        N5659A03878      Hisense           9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth10/1/1 LTX1305-BC+        N5658A01155      Hisense           9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth11/0/0 LTX1305-BC+        N5658A01748      Hisense           9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth11/0/1 LTX1305-BC+        N5659A00964      Hisense           9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth12/0/0 LTX1305-BC+        N5671A15288      Hisense           9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth12/0/1 LTX1305-BC+        N5671A15289      Hisense           9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth12/1/0 LTX1305-BC+        N5671A16905      Hisense           9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                
Eth12/1/1 LTX1305-BC+        N5671A18274      Hisense           9900Mb/s-1310nm-
                                                                LC-10km(0.009mm)
                                                                '''

data_split_mid_1 = re.split('=\n',test1)
data_split_mid_2 = data_split_mid_1[1].split()
count = 0
Port_Type_Sum = []
while count <len(data_split_mid_2):
    if re.match(r'[a-zA-Z]+\d+\/\d+\/+\d+',data_split_mid_2[count]) is not None:
        print(data_split_mid_2[count])
        Slot_Num = re.sub('[a-zA-Z]+', '', data_split_mid_2[count])
        Port_Type = data_split_mid_2[count+1]
        Port_Type_Sum.append([Slot_Num,Port_Type])

    count += 1

print(Port_Type_Sum)