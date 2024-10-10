import os
import sys

import gc
import time
import subprocess

from pyparsing import empty

start_time = []
end_time = []

LOAD = ["test1.csv","test2.csv"
    ,"test3.csv", "test4.csv", "test40.csv","test41.csv","test42.csv","test43.csv","test44.csv","test4.csv","test5_content__product.csv","test5_content__service.csv","test5_content__user.csv","test5_content__user_extended.csv","test5_data__ids.csv","test5_data_categories.csv","test5_product.csv","test5_service.csv","test5_service__extended.csv","test5_user__data.csv","test5_user__data_extended.csv","test5_user__extended_locker.csv","test5_user__locker.csv"
        ]

# Data CSV format show check

start_time.append(time.time())

for T in LOAD:
    datum = open(T,"r",encoding="utf-8").read()
    datum = str(datum)

    header = datum.split("\n")[0]
    data = datum.split('\n')[1::]

    print(header)

    LINESWITHCOMMA =[]
    for j in range(0, len(data)):
        HAVECOMMA = False

        for jj in range(0, len(data[j])):
            if data[j][jj] is ",":
                HAVECOMMA = True

        if HAVECOMMA is True:
            LINESWITHCOMMA.append(j)
        else:
            data[LINESWITHCOMMA[-1]] += data[j]
            data[j] = ""

    print (header)

    for j in range(0,len(data)):
        if data[j] is not "" and data[j] is not []:
            TEMP = ""
            VALUESTEMP = []
            IS = False

            for i in range(0, len(data[j])):
                if data[j][i] is not "," and data[j][i] is not '"' or i == (len(data[j]) - 1):
                    if i == (len(data[j]) - 1):
                        TEMP += data[j][i]
                        VALUESTEMP.append(TEMP)
                    else:
                        TEMP += data[j][i]
                elif data[j][i] is "," and IS is False:
                    VALUESTEMP.append(TEMP)
                    TEMP = ""
                elif data[j][i] is '"':
                    if IS is False:
                        IS = True
                    else:
                        IS = False
                elif data[j][i] is "," and IS is True:
                    TEMP += ","

            print(VALUESTEMP)

end_time.append(time.time())

# Data CSV format specific lines show check

start_time.append(time.time())

for T in LOAD:
    datum = open(T,"r",encoding="utf-8").read()
    datum = str(datum)

    header = datum.split("\n")[0].split(",")
    data = datum.split('\n')[1::]

    newheader = []

    # print(header)

    LINESWITHCOMMA =[]
    for j in range(0, len(data)):
        HAVECOMMA = False

        for jj in range(0, len(data[j])):
            if data[j][jj] is ",":
                HAVECOMMA = True

        if HAVECOMMA is True:
            LINESWITHCOMMA.append(j)
        else:
            data[LINESWITHCOMMA[-1]] += data[j]
            data[j] = ""

    for n in range(0,len(header), 2):
        newheader.append(header[n])

    # print(newheader)
    newheader = []

    for n in range(0, len(header)):
        if n == 1 or n == 4 or n == 5 or n == 7 or n == 8 or n ==9:
            newheader.append(header[n])

    print(newheader)

    for j in range(0,len(data)):
        if data[j] is not "" and data[j] is not []:
            TEMP = ""
            VALUESTEMP = []
            IS = False

            for i in range(0, len(data[j])):
                if data[j][i] is not "," and data[j][i] is not '"' or i == (len(data[j]) - 1):
                    if i == (len(data[j]) - 1):
                        TEMP += data[j][i]
                        VALUESTEMP.append(TEMP)
                    else:
                        TEMP += data[j][i]
                elif data[j][i] is "," and IS is False:
                    VALUESTEMP.append(TEMP)
                    TEMP = ""
                elif data[j][i] is '"':
                    if IS is False:
                        IS = True
                    else:
                        IS = False
                elif data[j][i] is "," and IS is True:
                    TEMP += ","

            NEWVALUESTEMP = []
            NEWVALUESTEMP.append(VALUESTEMP[1])
            if len(VALUESTEMP) > 4:
                NEWVALUESTEMP.append(VALUESTEMP[4])
            if len(VALUESTEMP) > 5:
                NEWVALUESTEMP.append(VALUESTEMP[5])
            if len(VALUESTEMP) > 6:
                NEWVALUESTEMP.append(VALUESTEMP[7])
            if len(VALUESTEMP) > 8:
                NEWVALUESTEMP.append(VALUESTEMP[8])
            if len(VALUESTEMP) > 9:
                NEWVALUESTEMP.append(VALUESTEMP[9])

            print(NEWVALUESTEMP)

end_time.append(time.time())

# Data CSV format specific lines with condition show check

start_time.append(time.time())

for T in LOAD:
    datum = open(T,"r",encoding="utf-8").read()
    datum = str(datum)

    header = datum.split("\n")[0]
    data = datum.split('\n')[1::]

    header = header.split(",")

    newheader = []
    newheaders = []

    # print(header)

    LINESWITHCOMMA =[]
    for j in range(0, len(data)):
        HAVECOMMA = False

        for jj in range(0, len(data[j])):
            if data[j][jj] is ",":
                HAVECOMMA = True

        if HAVECOMMA is True:
            LINESWITHCOMMA.append(j)
        else:
            data[LINESWITHCOMMA[-1]] += data[j]
            data[j] = ""

    for n in range(0, len(header)):
        if (header[n] == "id") or (header[n] == "title"):
            newheader.append(header[n])
            newheaders.append(n)

    allheaders = [newheader, newheaders]

    for j in range(0,len(data)):
        if data[j] is not "" and data[j] is not []:
            TEMP = ""
            VALUESTEMP = []
            NEWVALUESTEMP = []
            IS = False

            for i in range(0, len(data[j])):
                if data[j][i] is not "," and data[j][i] is not '"' or i == (len(data[j]) - 1):
                    if i == (len(data[j]) - 1):
                        TEMP += data[j][i]
                        VALUESTEMP.append(TEMP)
                    else:
                        TEMP += data[j][i]
                elif data[j][i] is "," and IS is False:
                    VALUESTEMP.append(TEMP)
                    TEMP = ""
                elif data[j][i] is '"':
                    if IS is False:
                        IS = True
                    else:
                        IS = False
                elif data[j][i] is "," and IS is True:
                    TEMP += ","

            for v in range(0,len(newheaders)):
                NEWVALUESTEMP.append(VALUESTEMP[v])

            if len(NEWVALUESTEMP) > 0:
                print(NEWVALUESTEMP)

end_time.append(time.time())

# Data CSV format specific lines characteristic show

start_time.append(time.time())

for T in LOAD:
    datum = open(T,"r",encoding="utf-8").read()
    datum = str(datum)

    header = datum.split("\n")[0]
    data = datum.split('\n')[1::]

    header = header.split(",")

    newheader = []
    newheaders = []

    # print(header)

    LINESWITHCOMMA =[]
    for j in range(0, len(data)):
        HAVECOMMA = False

        for jj in range(0, len(data[j])):
            if data[j][jj] == ",":
                HAVECOMMA = True

        if HAVECOMMA is True:
            LINESWITHCOMMA.append(j)
        else:
            data[LINESWITHCOMMA[-1]] += data[j]
            data[j] = ""

    for n in range(0, len(header)):
        if (header[n] == "id") or (header[n] == "uid") or (header[n] == "price"):
            newheader.append(header[n])
            newheaders.append(n)

    allheaders = [newheader, newheaders]
    # print(newheader, newheaders)

    for j in range(0,len(data)):
        if data[j] != "" and data[j] != []:
            TEMP = ""
            VALUESTEMP = []
            NEWVALUESTEMP = []
            IS = False

            for i in range(0, len(data[j])):
                if data[j][i] != "," and data[j][i] != '"' or i == (len(data[j]) - 1):
                    if i == (len(data[j]) - 1):
                        TEMP += data[j][i]
                        VALUESTEMP.append(TEMP)
                    else:
                        TEMP += data[j][i]
                elif data[j][i] == "," and IS == False:
                    VALUESTEMP.append(TEMP)
                    TEMP = ""
                elif data[j][i] == '"':
                    if IS is False:
                        IS = True
                    else:
                        IS = False
                elif data[j][i] == "," and IS == True:
                    TEMP += ","

            for v in range(0,len(newheaders)):
                if (newheader[v] == 'id' and (VALUESTEMP[newheaders[v]] == '24' or VALUESTEMP[newheaders[v]] == '2')) or (newheader[v] == 'uid' and (VALUESTEMP[newheaders[v]] == '24' or VALUESTEMP[newheaders[v]] == '2')):
                    for i in range(0, len(newheader)):
                        if newheader[i] == 'price':
                            NEWVALUESTEMP.append(VALUESTEMP)


            if len(NEWVALUESTEMP) > 0:
                print(NEWVALUESTEMP)

end_time.append(time.time())

# print(open("./test1.csv","r",encoding="utf-8").read())
print(start_time, end_time)
for i in range(0, len(start_time)):
    if end_time[i] is not None:
        print(end_time[i] - start_time[i])

print(end_time[-1] - start_time[0])

# 4 ghz amd processor, asus vivobook m6500x
# first test heaten-up pycharm
# [1728520453.3372204, 1728520459.7822263, 1728520465.8628404, 1728520471.993359] [1728520459.7822256, 1728520465.8628397, 1728520471.9933584, 1728520478.4058323]
# 6.445005178451538
# 6.080613374710083
# 6.130517959594727
# 6.412473201751709
# 25.06861186027527
# second test heaten-up pycharm
# [1728520628.1863153, 1728520634.6522646, 1728520641.1045873, 1728520647.4266248] [1728520634.6522636, 1728520641.104585, 1728520647.426624, 1728520654.1688511]
# 6.4659483432769775
# 6.452320337295532
# 6.3220367431640625
# 6.7422263622283936
# 25.98253583908081
# third test heaten-up pycharm
# [1728520676.3162363, 1728520682.8584282, 1728520689.0261102, 1728520695.311439] [1728520682.8584278, 1728520689.02611, 1728520695.3114386, 1728520701.903049]
# 6.542191505432129
# 6.167681694030762
# 6.285328388214111
# 6.591609954833984
# 25.586812734603882

# rohh@rohh-Vivobook-ASUSLaptop-M6500XU-M6500XU:/home/rohhs/script/python/data_loader/csvest$ ps aux
# USER         PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
# root           1  0.0  0.0  24644 14764 ?        Ss   Oct05   0:20 /sbin/init sp
# root           2  0.0  0.0      0     0 ?        S    Oct05   0:00 [kthreadd]
# root           3  0.0  0.0      0     0 ?        S    Oct05   0:00 [pool_workque
# root           4  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-rc
# root           5  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-rc
# root           6  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-sl
# root           7  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-ne
# root          10  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/0:0H
# root          12  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-mm
# root          13  0.0  0.0      0     0 ?        I    Oct05   0:00 [rcu_tasks_kt
# root          14  0.0  0.0      0     0 ?        I    Oct05   0:00 [rcu_tasks_ru
# root          15  0.0  0.0      0     0 ?        I    Oct05   0:00 [rcu_tasks_tr
# root          16  0.0  0.0      0     0 ?        S    Oct05   0:03 [ksoftirqd/0]
# root          17  0.0  0.0      0     0 ?        I    Oct05   3:31 [rcu_preempt]
# root          18  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/0]
# root          19  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          20  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/0]
# root          21  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/1]
# root          22  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          23  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/1]
# root          24  0.0  0.0      0     0 ?        S    Oct05   0:03 [ksoftirqd/1]
# root          26  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/1:0H
# root          27  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/2]
# root          28  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          29  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/2]
# root          30  0.0  0.0      0     0 ?        S    Oct05   0:02 [ksoftirqd/2]
# root          32  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/2:0H
# root          33  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/3]
# root          34  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          35  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/3]
# root          36  0.0  0.0      0     0 ?        S    Oct05   0:02 [ksoftirqd/3]
# root          38  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/3:0H
# root          39  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/4]
# root          40  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          41  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/4]
# root          42  0.0  0.0      0     0 ?        S    Oct05   0:01 [ksoftirqd/4]
# root          44  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/4:0H
# root          45  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/5]
# root          46  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          47  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/5]
# root          48  0.0  0.0      0     0 ?        S    Oct05   0:01 [ksoftirqd/5]
# root          50  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/5:0H
# root          51  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/6]
# root          52  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          53  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/6]
# root          54  0.0  0.0      0     0 ?        S    Oct05   0:01 [ksoftirqd/6]
# root          56  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/6:0H
# root          57  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/7]
# root          58  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          59  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/7]
# root          60  0.0  0.0      0     0 ?        S    Oct05   0:01 [ksoftirqd/7]
# root          62  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/7:0H
# root          63  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/8]
# root          64  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          65  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/8]
# root          66  0.0  0.0      0     0 ?        S    Oct05   0:01 [ksoftirqd/8]
# root          68  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/8:0H
# root          69  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/9]
# root          70  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          71  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/9]
# root          72  0.0  0.0      0     0 ?        S    Oct05   0:01 [ksoftirqd/9]
# root          74  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/9:0H
# root          75  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/10]
# root          76  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          77  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/10
# root          78  0.0  0.0      0     0 ?        S    Oct05   0:01 [ksoftirqd/10
# root          80  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/10:0
# root          81  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/11]
# root          82  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          83  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/11
# root          84  0.0  0.0      0     0 ?        S    Oct05   0:01 [ksoftirqd/11
# root          86  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/11:0
# root          87  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/12]
# root          88  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          89  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/12
# root          90  0.0  0.0      0     0 ?        S    Oct05   0:01 [ksoftirqd/12
# root          92  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/12:0
# root          93  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/13]
# root          94  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root          95  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/13
# root          96  0.0  0.0      0     0 ?        S    Oct05   0:08 [ksoftirqd/13
# root          98  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/13:0
# root          99  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/14]
# root         100  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root         101  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/14
# root         102  0.0  0.0      0     0 ?        S    Oct05   0:05 [ksoftirqd/14
# root         104  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/14:0
# root         105  0.0  0.0      0     0 ?        S    Oct05   0:00 [cpuhp/15]
# root         106  0.0  0.0      0     0 ?        S    Oct05   0:00 [idle_inject/
# root         107  0.0  0.0      0     0 ?        S    Oct05   0:01 [migration/15
# root         108  0.0  0.0      0     0 ?        S    Oct05   0:00 [ksoftirqd/15
# root         110  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/15:0
# root         111  0.0  0.0      0     0 ?        S    Oct05   0:00 [kdevtmpfs]
# root         112  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-in
# root         114  0.0  0.0      0     0 ?        S    Oct05   0:04 [kauditd]
# root         115  0.0  0.0      0     0 ?        S    Oct05   0:00 [khungtaskd]
# root         116  0.0  0.0      0     0 ?        S    Oct05   0:00 [oom_reaper]
# root         118  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-wr
# root         119  0.0  0.0      0     0 ?        S    Oct05   0:34 [kcompactd0]
# root         120  0.0  0.0      0     0 ?        SN   Oct05   0:00 [ksmd]
# root         122  0.0  0.0      0     0 ?        SN   Oct05   0:00 [khugepaged]
# root         123  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-ki
# root         124  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-kb
# root         125  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-bl
# root         126  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/9-acpi]
# root         129  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-tp
# root         130  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-at
# root         131  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-md
# root         132  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-md
# root         133  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-ed
# root         134  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-de
# root         135  0.0  0.0      0     0 ?        S    Oct05   0:00 [watchdogd]
# root         136  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/6:1H
# root         138  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/28-AMD-V
# root         139  0.0  0.0      0     0 ?        S    Oct05   0:06 [kswapd0]
# root         140  0.0  0.0      0     0 ?        S    Oct05   0:00 [ecryptfs-kth
# root         141  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-kt
# root         142  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/36-pcieh
# root         143  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/39-aerdr
# root         144  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/39-pcieh
# root         156  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-ac
# root         158  0.0  0.0      0     0 ?        S    Oct05   0:01 [hwrng]
# root         159  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-ml
# root         160  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/2:1H
# root         161  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-ip
# root         168  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-ks
# root         183  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-ch
# root         184  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/29-ACPI:
# root         185  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/30-ACPI:
# root         186  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/31-ACPI:
# root         187  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/32-ACPI:
# root         188  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/33-ACPI:
# root         189  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/34-ACPI:
# root         190  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/35-ACPI:
# root         216  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/0:1H
# root         218  0.0  0.0      0     0 ?        I<   Oct05   0:01 [kworker/15:1
# root         232  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/1:1H
# root         233  0.0  0.0      0     0 ?        I<   Oct05   0:01 [kworker/13:1
# root         247  0.0  0.0      0     0 ?        I<   Oct05   0:01 [kworker/9:1H
# root         249  0.0  0.0      0     0 ?        I<   Oct05   0:01 [kworker/12:1
# root         250  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/4:1H
# root         251  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/7:1H
# root         252  0.0  0.0      0     0 ?        I<   Oct05   0:01 [kworker/11:1
# root         253  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/3:1H
# root         254  0.0  0.0      0     0 ?        I<   Oct05   0:01 [kworker/14:1
# root         255  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/5:1H
# root         256  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/8:1H
# root         257  0.0  0.0      0     0 ?        I<   Oct05   0:01 [kworker/10:1
# root         260  0.0  0.0      0     0 ?        S    Oct05   1:37 [irq/43-ASUE1
# root         356  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-nv
# root         357  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-nv
# root         358  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-nv
# root         359  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-nv
# root         419  0.0  0.0      0     0 ?        S    Oct05   0:27 [jbd2/nvme0n1
# root         420  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-ex
# root         469  0.0  0.6 154068 100432 ?       S<s  Oct05   0:16 /usr/lib/syst
# root         549  0.0  0.0  30752  8576 ?        Ss   Oct05   0:07 /usr/lib/syst
# root         615  0.0  0.0      0     0 ?        S    Oct05   0:00 [psimon]
# root         754  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-cf
# root         809  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-cr
# root         861  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-le
# root         876  0.0  0.0      0     0 ?        S    Oct05   0:00 [irq/82-ACP_P
# root         905  0.0  0.0      0     0 ?        S    Oct05   1:33 [napi/phy0-81
# root         906  0.0  0.0      0     0 ?        S    Oct05   0:05 [napi/phy0-81
# root         907  0.0  0.0      0     0 ?        S    Oct05   1:10 [napi/phy0-81
# root         909  0.0  0.0      0     0 ?        S    Oct05   0:00 [nv_queue]
# root         910  0.0  0.0      0     0 ?        S    Oct05   0:00 [nv_queue]
# root         911  0.0  0.0      0     0 ?        S    Oct05   0:00 [nv_open_q]
# root         923  0.0  0.0      0     0 ?        S    Oct05   0:49 [mt76-tx phy0
# root         928  0.0  0.0      0     0 ?        S    Oct05   0:00 [nvidia-modes
# root         929  0.0  0.0      0     0 ?        S    Oct05   0:00 [nvidia-modes
# root         934  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-am
# root         935  0.0  0.0      0     0 ?        S    Oct05   0:10 [irq/88-nvidi
# root         937  0.0  0.0      0     0 ?        S    Oct05   0:05 [nv_queue]
# root        1001  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-tt
# systemd+    1094  0.0  0.0  17556  7552 ?        Ss   Oct05   1:35 /usr/lib/syst
# systemd+    1110  0.0  0.0  23260 14080 ?        Ss   Oct05   0:25 /usr/lib/syst
# systemd+    1112  0.0  0.0  91044  7808 ?        Ssl  Oct05   0:01 /usr/lib/syst
# avahi       1199  0.0  0.0   8664  4352 ?        Ss   Oct05   0:11 avahi-daemon:
# root        1200  0.0  0.0  14328  6528 ?        Ss   Oct05   4:22 /usr/libexec/
# message+    1201  0.0  0.0  12368  7168 ?        Ss   Oct05   0:40 @dbus-daemon
# gnome-r+    1204  0.0  0.1 439064 15956 ?        Ssl  Oct05   0:00 /usr/libexec/
# polkitd     1208  0.0  0.0 399788 12088 ?        Ssl  Oct05   0:02 /usr/lib/polk
# root        1209  0.0  0.0 322296  7424 ?        Ssl  Oct05   0:00 /usr/libexec/
# root        1219  0.0  0.0 321960  7636 ?        Ssl  Oct05   0:07 /usr/libexec/
# root        1222  0.0  0.0  18092  2816 ?        Ss   Oct05   0:00 /usr/sbin/cro
# root        1224  0.0  0.0 318828  6784 ?        Ssl  Oct05   0:00 /usr/libexec/
# root        1229  0.0  0.0  18300  9064 ?        Ss   Oct05   0:06 /usr/lib/syst
# root        1231  0.0  0.0 470496 14300 ?        Ssl  Oct05   0:05 /usr/libexec/
# avahi       1237  0.0  0.0   8476  1292 ?        S    Oct05   0:00 avahi-daemon:
# root        1256  0.0  0.1 345392 19272 ?        Ssl  Oct05   0:42 /usr/sbin/Net
# root        1260  0.0  0.0  18260 11008 ?        Ss   Oct05   0:11 /usr/sbin/wpa
# syslog      1282  0.0  0.0 222564  6144 ?        Ssl  Oct05   0:04 /usr/sbin/rsy
# root        1368  0.0  0.0 392312 12360 ?        Ssl  Oct05   0:01 /usr/sbin/Mod
# root        1371  0.0  0.0 322296  7744 ?        Ssl  Oct05   0:00 /usr/libexec/
# root        1462  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-am
# root        1463  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-am
# root        1464  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-am
# root        1465  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-am
# root        1466  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-am
# root        1467  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-am
# root        1468  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-am
# root        1469  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-dm
# root        1470  0.0  0.0      0     0 ?        I<   Oct05   0:00 [kworker/R-am
# root        1513  0.0  0.0      0     0 ?        S    Oct05   0:00 [card1-crtc0]
# root        1514  0.0  0.0      0     0 ?        S    Oct05   0:00 [card1-crtc1]
# root        1517  0.0  0.0      0     0 ?        S    Oct05   0:00 [card1-crtc2]
# root        1518  0.0  0.0      0     0 ?        S    Oct05   0:00 [card1-crtc3]
# root        1657  0.0  0.0      0     0 ?        S    Oct05   0:00 [UVM global q
# root        1658  0.0  0.0      0     0 ?        S    Oct05   0:00 [UVM deferred
# root        1659  0.0  0.0      0     0 ?        S    Oct05   0:00 [UVM Tools Ev
# nvidia-+    1725  0.0  0.0   5376  1920 ?        Ss   Oct05   0:00 /usr/bin/nvid
# root        2025  0.0  0.1 120900 22912 ?        Ssl  Oct05   0:00 /usr/bin/pyth
# root        2078  0.0  0.0   6820  5208 ?        Ss   Oct05   0:14 /usr/sbin/apa
# root        2249  0.0  0.0 323488  9216 ?        Ssl  Oct05   0:00 /usr/sbin/gdm
# rtkit       2303  0.0  0.0  22940  3584 ?        SNsl Oct05   0:03 /usr/libexec/
# root        2346  0.0  0.0      0     0 ?        S<   Oct05   0:00 [krfcommd]
# kernoops    2381  0.0  0.0  12744  2220 ?        Ss   Oct05   0:00 /usr/sbin/ker
# root        2385  0.0  0.0  11156  1732 ?        Ss   Oct05   0:00 nginx: master
# www-data    2386  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# www-data    2387  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# www-data    2388  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# www-data    2389  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# www-data    2390  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# kernoops    2392  0.0  0.0  12744  2184 ?        Ss   Oct05   0:00 /usr/sbin/ker
# www-data    2393  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# www-data    2394  0.0  0.0  12880  4552 ?        S    Oct05   0:00 nginx: worker
# www-data    2395  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# www-data    2396  0.0  0.0  12880  4552 ?        S    Oct05   0:00 nginx: worker
# www-data    2397  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# www-data    2398  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# www-data    2399  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# www-data    2400  0.0  0.0  12880  4552 ?        S    Oct05   0:00 nginx: worker
# www-data    2401  0.0  0.0  12880  4552 ?        S    Oct05   0:00 nginx: worker
# www-data    2403  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# www-data    2404  0.0  0.0  12880  4424 ?        S    Oct05   0:00 nginx: worker
# colord      2553  0.0  0.0 328968 14816 ?        Ssl  Oct05   0:00 /usr/libexec/
# root        2625  0.0  0.1 329528 15744 ?        Ssl  Oct05   0:46 /usr/libexec/
# root        2963  0.0  0.0 398844 10752 ?        Sl   Oct05   0:00 gdm-session-w
# rohh        2975  0.0  0.0  22444 14464 ?        Ss   Oct05   0:10 /usr/lib/syst
# rohh        2981  0.0  0.0  21456  3608 ?        S    Oct05   0:00 (sd-pam)
# rohh        2990  0.0  0.1 136880 25676 ?        S<sl Oct05   4:45 /usr/bin/pipe
# rohh        2991  0.0  0.0 106404  6144 ?        Ssl  Oct05   0:00 /usr/bin/pipe
# rohh        2994  0.0  0.1 416700 19640 ?        S<sl Oct05   0:06 /usr/bin/wire
# rohh        2996  0.1  0.5 217016 91320 ?        S<sl Oct05   7:34 /usr/bin/pipe
# rohh        2998  0.0  0.0 325176 10112 ?        SLsl Oct05   0:01 /usr/bin/gnom
# rohh        3011  0.0  0.0  11288  6528 ?        Ss   Oct05   0:37 /usr/bin/dbus
# rohh        3033  0.0  0.0 843260  7936 ?        Ssl  Oct05   0:01 /usr/libexec/
# rohh        3047  0.0  0.0 318588  6528 ?        Ssl  Oct05   0:00 /usr/libexec/
# root        3056  0.0  0.0   2704  1920 ?        Ss   Oct05   0:00 fusermount3 -
# rohh        3087  0.0  0.0 244380  6016 tty2     Ssl+ Oct05   0:00 /usr/libexec/
# rohh        3090  1.5  1.6 27267312 263840 tty2  Sl+  Oct05  94:31 /usr/lib/xorg
# rohh        3221  0.0  0.1 306868 16512 tty2     Sl+  Oct05   0:00 /usr/libexec/
# rohh        3314  0.0  0.0 383000  8064 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3327  0.0  0.0   9740  5120 ?        S    Oct05   0:07 /usr/bin/dbus
# rohh        3345  0.0  0.0 162652  6784 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3346  0.0  0.0 100216  5632 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3360  0.0  0.0 322924  7808 ?        Ssl  Oct05   0:01 /usr/libexec/
# rohh        3368  0.0  0.0 468380  7040 ?        Sl   Oct05   0:00 /usr/libexec/
# rohh        3370  0.0  0.1 529320 17920 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3415  1.5  2.5 6163792 390636 ?      Ssl  Oct05  98:16 /usr/bin/gnom
# rohh        3444  0.0  1.0 1897272 161276 ?      Sl   Oct05   1:28 /usr/libexec/
# rohh        3447  0.0  0.0 236052  8192 ?        Sl   Oct05   0:26 /usr/libexec/
# rohh        3486  0.0  0.1 654964 17152 ?        Sl   Oct05   0:00 /usr/libexec/
# rohh        3494  0.0  0.2 1266816 42368 ?       Ssl  Oct05   0:00 /usr/libexec/
# rohh        3501  0.0  0.0 230464  5888 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3511  0.0  0.1 555244 23936 ?        Sl   Oct05   0:00 /usr/libexec/
# rohh        3513  0.0  0.1 2933416 26848 ?       Sl   Oct05   0:00 /usr/bin/gjs
# rohh        3533  0.0  0.1 1374736 23552 ?       Ssl  Oct05   0:00 /usr/libexec/
# rohh        3536  0.0  0.0 397796  9088 ?        Sl   Oct05   0:00 /usr/libexec/
# rohh        3552  0.1  0.2 414352 31756 ?        Ssl  Oct05   6:24 /usr/bin/ibus
# rohh        3553  0.0  0.0 392248  6528 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3554  0.0  0.1 424132 23952 ?        Ssl  Oct05   0:02 /usr/libexec/
# rohh        3555  0.0  0.0 440388 11904 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3556  0.0  0.0 468256  8192 ?        Ssl  Oct05   0:08 /usr/libexec/
# rohh        3558  0.0  0.1 422972 23380 ?        Ssl  Oct05   0:01 /usr/libexec/
# rohh        3559  0.0  0.1 752796 29208 ?        Ssl  Oct05   0:03 /usr/libexec/
# rohh        3565  0.0  0.1 604148 29692 ?        Ssl  Oct05   0:06 /usr/libexec/
# rohh        3567  0.0  0.0 332312 11264 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3569  0.0  0.0 539752  6656 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3571  0.0  0.0 318228  6016 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3580  0.0  0.0 551924 11392 ?        Ssl  Oct05   0:14 /usr/libexec/
# rohh        3588  0.0  0.0 468280  8320 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3592  0.0  0.0 402368  9472 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3597  0.0  0.1 423648 24244 ?        Ssl  Oct05   0:01 /usr/libexec/
# rohh        3599  0.0  0.1 425268 26400 ?        Ssl  Oct05   0:02 /usr/libexec/
# rohh        3606  0.0  0.0 305624  7680 ?        Sl   Oct05   0:00 /usr/libexec/
# rohh        3624  0.0  0.0 398288 10752 ?        Ssl  Oct05   0:18 /usr/libexec/
# rohh        3633  0.0  0.4 963924 63608 ?        Sl   Oct05   0:02 /usr/libexec/
# rohh        3657  0.0  0.0 319148  7168 ?        Sl   Oct05   0:00 /usr/libexec/
# rohh        3658  0.0  0.2 356528 31316 ?        Sl   Oct05   0:32 /usr/libexec/
# rohh        3669  0.0  0.1 275744 24020 ?        Sl   Oct05   0:36 /usr/libexec/
# rohh        3677  0.0  0.0 673040  9984 ?        Sl   Oct05   0:16 /usr/libexec/
# rohh        3751  0.0  0.0 424872 14976 ?        Sl   Oct05   0:00 /usr/libexec/
# rohh        3761  0.0  0.1 834136 29440 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3795  0.0  0.1 343936 25760 ?        Ssl  Oct05   0:01 /usr/libexec/
# rohh        3814  0.0  0.0 398512  8192 ?        Ssl  Oct05   0:11 /usr/libexec/
# rohh        3826  0.0  0.0 318440  6528 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3832  0.0  0.0 318592  6656 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        3858  0.0  0.1 2941608 26800 ?       Sl   Oct05   0:00 /usr/bin/gjs
# rohh        3883  0.0  0.2 892236 34712 ?        SNsl Oct05   0:03 /usr/libexec/
# rohh        3890  0.0  0.0 245568  7168 ?        Sl   Oct05   1:04 /usr/libexec/
# rohh        3926  0.0  0.0 618232  9216 ?        Sl   Oct05   0:00 /usr/libexec/
# rohh        4040  0.0  0.0 245100  6656 ?        Ssl  Oct05   0:00 /usr/libexec/
# rohh        4227  0.0  0.1 424068 25868 ?        Ssl  Oct05   0:02 /usr/libexec/
# rohh        4237  0.0  0.2 575548 33992 ?        Sl   Oct05   0:08 /usr/bin/upda
# rohh        4507  0.0  0.1 1984100 20960 ?       Sl   Oct05   0:05 /usr/bin/snap
# rohh        5612  0.0  0.0 710472 14412 ?        Ssl  Oct05   0:32 /usr/libexec/
# rohh        5617  0.0  1.7 3518764 270580 ?      Ssl  Oct05   1:22 /usr/libexec/
# rohh        7005  0.0  0.0 128948  9192 ?        Ssl  Oct05   0:07 /usr/bin/spee
# rohh        7017  0.0  0.0      0     0 ?        Z    Oct05   0:00 [sd_espeak-ng
# rohh        7021  0.0  0.0 116040 10112 ?        Sl   Oct05   0:02 /usr/lib/spee
# rohh        7025  0.0  0.0 162692  6144 ?        Sl   Oct05   0:36 /usr/lib/spee
# rohh        7028  0.0  0.0   5668  2688 ?        S    Oct05   0:00 /usr/lib/spee
# rohh        7370  0.0  0.0 397996  9332 ?        Sl   Oct05   0:00 /usr/libexec/
# root        9124  0.0  0.2 586200 43244 ?        Ssl  Oct05   0:17 /usr/libexec/
# rohh       23906  0.0  0.0 471176  8320 ?        Sl   Oct05   0:01 /usr/libexec/
# rohh       23926  0.0  0.0 399216  8832 ?        Sl   Oct05   0:00 /usr/libexec/
# rohh       82055  0.0  0.3 853720 56404 ?        Ssl  Oct07   0:06 /usr/libexec/
# rohh       82066  0.0  0.0  19932  5376 pts/0    Ss   Oct07   0:00 bash
# rohh       83088  4.5 16.2 6115556 2525696 ?     Sl   Oct07 193:27 /snap/pycharm
# rohh       83191  0.0  0.0   3780  2048 ?        S    Oct07   0:13 /snap/pycharm
# root      108335  0.0  0.2 2430760 38356 ?       Ssl  Oct07   0:47 /usr/lib/snap
# rohh      109624  0.0  0.0  39128 11904 ?        Ss   Oct07   0:00 /snap/snapd-d
# rohh      109776  0.0  0.7 1069736 114948 ?      Sl   Oct07   0:03 /snap/snapd-d
# www-data  128307  0.0  0.0 1999552 5776 ?        Sl   Oct08   0:00 /usr/sbin/apa
# www-data  128308  0.0  0.0 1999512 5392 ?        Sl   Oct08   0:00 /usr/sbin/apa
# root      128373  0.0  0.0  46912 12160 ?        Ss   Oct08   0:00 /usr/sbin/cup
# cups-br+  128376  0.0  0.1 268396 20224 ?        Ssl  Oct08   0:00 /usr/sbin/cup
# rohh      149373  0.0  1.2 1212284172 195680 ?   Sl   Oct08   1:39 /snap/discord
# rohh      149452  0.0  0.3 33805988 51584 ?      S    Oct08   0:00 /snap/discord
# rohh      149453  0.0  0.3 33805976 51456 ?      S    Oct08   0:00 /snap/discord
# rohh      149490  0.0  0.0 33576880 3328 ?       Sl   Oct08   0:00 /snap/discord
# rohh      149529  0.0  1.4 34285160 219964 ?     Sl   Oct08   0:37 /snap/discord
# rohh      149561  0.0  0.5 33888568 82560 ?      Sl   Oct08   0:17 /snap/discord
# rohh      149635  0.7  2.4 1225871484 381672 ?   Sl   Oct08  21:45 /snap/discord
# rohh      149704  0.0  0.4 33932456 62712 ?      Sl   Oct08   0:03 /snap/discord
# rohh      155741  0.8  4.2 3204928 663748 ?      SLsl Oct08  24:51 /snap/telegra
# root      163238  0.0  0.0      0     0 ?        S    Oct08   0:00 [psimon]
# root      174640  0.0  0.0      0     0 ?        I    Oct09   0:01 [kworker/10:2
# root      186460  0.0  0.0      0     0 ?        I    Oct09   0:00 [kworker/9:2-
# root      188783  0.0  0.0      0     0 ?        I    01:09   0:00 [kworker/8:0-
# root      188786  0.0  0.0      0     0 ?        I    01:09   0:00 [kworker/11:0
# root      192806  0.0  0.0      0     0 ?        I    01:40   0:00 [kworker/12:2
# root      196759  0.1  0.0      0     0 ?        I    02:32   0:05 [kworker/u32:
# root      197054  0.0  0.0      0     0 ?        I    02:44   0:00 [kworker/5:2-
# root      197255  0.0  0.0      0     0 ?        I    02:53   0:00 [kworker/2:1-
# root      197479  0.0  0.0      0     0 ?        I    03:00   0:00 [kworker/6:0-
# root      197671  0.0  0.0      0     0 ?        I    03:00   0:02 [kworker/u32:
# root      197683  0.0  0.0      0     0 ?        I<   03:01   0:00 [kworker/u33:
# root      197832  0.0  0.0      0     0 ?        I    03:08   0:00 [kworker/15:0
# root      197894  0.0  0.0      0     0 ?        I    03:11   0:00 [kworker/4:2-
# root      197905  0.0  0.0      0     0 ?        I    03:12   0:00 [kworker/7:1-
# root      197938  0.0  0.0      0     0 ?        I    03:14   0:00 [kworker/3:2-
# root      197941  0.0  0.0      0     0 ?        I    03:14   0:00 [kworker/13:0
# root      197943  0.0  0.0      0     0 ?        I    03:14   0:00 [kworker/1:0-
# root      197957  0.0  0.0      0     0 ?        I    03:15   0:00 [kworker/5:1-
# root      197962  0.0  0.0      0     0 ?        I    03:15   0:00 [kworker/11:2
# root      198091  0.0  0.0      0     0 ?        I    03:17   0:00 [kworker/3:3-
# root      198127  0.0  0.0      0     0 ?        I    03:25   0:00 [kworker/14:2
# root      198143  0.0  0.0      0     0 ?        I    03:25   0:00 [kworker/u32:
# root      198146  0.1  0.0      0     0 ?        I    03:25   0:00 [kworker/u32:
# root      198156  0.0  0.0      0     0 ?        I    03:25   0:00 [kworker/15:3
# root      198204  0.0  0.0      0     0 ?        I    03:25   0:00 [kworker/6:2-
# root      198224  0.0  0.0      0     0 ?        I    03:25   0:00 [kworker/8:1-
# root      198255  0.0  0.0      0     0 ?        S    03:25   0:00 [nvidia]
# root      198297  0.0  0.0      0     0 ?        I    03:25   0:00 [kworker/0:2-
# root      198362  0.0  0.0      0     0 ?        I<   03:26   0:00 [kworker/u33:
# rohh      198607  0.0  0.3 3149616 59756 ?       Sl   03:26   0:00 gjs /usr/shar
# root      198799  0.0  0.0      0     0 ?        I    03:26   0:00 [kworker/4:0-
# root      199129  0.0  0.0      0     0 ?        I    03:28   0:00 [kworker/1:1-
# root      199196  0.0  0.0      0     0 ?        I    03:29   0:00 [kworker/2:2-
# root      199286  0.0  0.0      0     0 ?        I    03:29   0:00 [kworker/12:0
# root      199311  0.0  0.0      0     0 ?        I    03:30   0:00 [kworker/10:1
# root      199458  0.0  0.0      0     0 ?        I    03:31   0:00 [kworker/0:0-
# root      199573  0.0  0.0      0     0 ?        I    03:31   0:00 [kworker/13:1
# root      199637  0.0  0.0      0     0 ?        I    03:32   0:00 [kworker/3:0-
# root      199697  0.0  0.0      0     0 ?        I    03:32   0:00 [kworker/14:1
# root      199702  0.2  0.0      0     0 ?        I    03:32   0:00 [kworker/u32:
# root      199803  0.0  0.0      0     0 ?        I    03:33   0:00 [kworker/9:0-
# root      199958  0.0  0.0      0     0 ?        I    03:34   0:00 [kworker/7:0-
# root      200047  0.0  0.0      0     0 ?        I    03:34   0:00 [kworker/11:1
# root      200073  0.0  0.0      0     0 ?        I    03:34   0:00 [kworker/1:2-
# root      200090  0.0  0.0      0     0 ?        I    03:34   0:00 [kworker/2:0-
# root      200147  0.0  0.0      0     0 ?        I    03:35   0:00 [kworker/8:2]
# root      200197  0.0  0.0      0     0 ?        I    03:35   0:00 [kworker/5:0-
# root      200471  0.0  0.0      0     0 ?        I    03:37   0:00 [kworker/10:0
# root      200502  0.0  0.0      0     0 ?        I    03:37   0:00 [kworker/4:1-
# root      200519  0.2  0.0      0     0 ?        I    03:37   0:00 [kworker/u32:
# root      200545  0.0  0.0      0     0 ?        I    03:37   0:00 [kworker/12:1
# root      200604  0.0  0.0      0     0 ?        I    03:38   0:00 [kworker/0:1-
# root      200625  0.0  0.0      0     0 ?        I    03:38   0:00 [kworker/13:2
# root      200754  0.0  0.0      0     0 ?        I<   03:38   0:00 [kworker/u33:
# root      200755  0.0  0.0      0     0 ?        I<   03:38   0:00 [kworker/u33:
# root      200756  0.0  0.0      0     0 ?        I<   03:38   0:00 [kworker/u33:
# root      200757  0.0  0.0      0     0 ?        I<   03:38   0:00 [kworker/u33:
# root      200758  0.0  0.0      0     0 ?        I<   03:38   0:00 [kworker/u33:
# root      200759  0.0  0.0      0     0 ?        I<   03:38   0:00 [kworker/u33:
# root      200760  0.0  0.0      0     0 ?        I<   03:38   0:00 [kworker/u33:
# root      200761  0.0  0.0      0     0 ?        I<   03:38   0:00 [kworker/u33:
# root      200762  0.0  0.0      0     0 ?        I<   03:38   0:00 [kworker/u33:
# root      200763  0.0  0.0      0     0 ?        I<   03:38   0:00 [kworker/u33:
# root      200764  0.0  0.0      0     0 ?        I<   03:38   0:00 [kworker/u33:
# root      200797  0.0  0.0      0     0 ?        I<   03:39   0:00 [kworker/u33:
# root      200807  0.0  0.0      0     0 ?        I<   03:39   0:00 [kworker/u33:
# root      200808  0.0  0.0      0     0 ?        I<   03:39   0:00 [kworker/u33:
# root      200932  0.0  0.0      0     0 ?        I    03:39   0:00 [kworker/9:1]
# all apps closed test runned from terminal
# [1728520858.276507, 1728520865.1882114, 1728520872.183515, 1728520879.1621373] [1728520865.1882107, 1728520872.1835146, 1728520879.1621366, 1728520886.231175]
# 6.911703824996948
# 6.995303153991699
# 6.978621482849121
# 7.069037675857544
# 27.954668045043945
# test from vsc ide with closed apps
# [1728521156.3381166, 1728521163.9612179, 1728521170.6286035, 1728521177.3510995] [1728521163.9612164, 1728521170.628601, 1728521177.3510985, 1728521183.9418838]
# 7.6230998039245605
# 6.667383193969727
# 6.722495079040527
# 6.590784311294556
# 27.603767156600952