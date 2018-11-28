import subprocess as sp

normal = 0
bad = 0
count = 0
Bad_IP = []
ping_log = open('ping_log.txt', 'w+',encoding='utf-8')
with open('ip.txt', 'rt', encoding='utf-8') as ip_list:
    for cur_ip in ip_list.readlines():
        status, result = sp.getstatusoutput("ping -w 10 "+cur_ip)
        print(result)
        ping_log.write(result+'\n')
        if status == 0:
            normal += 1
        else:
            bad += 1
            Bad_IP.append(cur_ip.strip('\n'))

        count += 1

    ip_list.close()
ping_log.write("\n\n共计ping测{A}个IP，其中可达{B}个，不可达{C}个，不可达设备为:\n{D}".format(A=count,B=normal,C=bad,D=Bad_IP))
ping_log.close()

