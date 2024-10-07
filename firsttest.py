import os
import sys

import gc
import time
import subprocess

# 4 ghz, asm to python somehow 1.07 * 600

LOAD = ["test1.csv","test2.csv","test3.csv", "test4.csv", "test40.csv","test41.csv","test42.csv","test43.csv","test44.csv","test4.csv","test5_content__product.csv","test5_content__service.csv","test5_content__user.csv","test5_content__user_extended.csv","test5_data__ids.csv","test5_data_categories.csv","test5_product.csv","test5_service.csv","test5_service__extended.csv","test5_user__data.csv","test5_user__data_extended.csv","test5_user__extended_locker.csv","test5_user__locker.csv"]


time_start3 = time.time()

for T in LOAD:
    data = open(T,"r",encoding="utf-8")
    data = str(data)
    temp = ""

    for char in data:
        temp = temp + char

    print (temp)

time_end3 = time.time()

time_start = time.time()

for T in LOAD:
    data = open(T,"r",encoding="utf-8")
    print(data.read())

time_end = time.time()

time_start2 = time.time()

for T in LOAD:
    data = open(T,"r",encoding="utf-8")
    try:
        ans = subprocess.check_output(["cat", T], text=True)
        print(ans)

    except subprocess.CalledProcessError as e:
        print(f"Command failed with return code {e.returncode}")

time_end2 = time.time()

time_start4 = time.time()

for T in LOAD:
    status = True
    index = 0
    temp = ""
    data = open(T,"r",encoding="utf-8")
    data = str(data)

    while status:
        temp = temp + data[index]
        index += 1
        if len(data) == index:
            status = False

    print (temp)

time_end4 = time.time()

time_start5 = time.time()

for T in LOAD:
    status = True
    index = 0
    data = open(T,"r",encoding="ascii")
    data = str(data)
    START = 0
    END = 0
    if len(data) > 1024:
        for i in range(0, len(data) // 10240):
            END = i * 1024
            print(data[START:END])
            START = END
    else:
        print(data)

time_end5 = time.time()

print(time_end - time_start, time_end2 - time_start2, time_end3 - time_start3, time_end4 - time_start4, time_end5 - time_start5)