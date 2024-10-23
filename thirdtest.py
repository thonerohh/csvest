import os
import sys

import time

TIME = []
LOAD = ["test1.csv","test2.csv"
# ,"test3.csv", "test4.csv", "test40.csv","test41.csv","test42.csv","test43.csv","test44.csv","test4.csv","test5_content__product.csv","test5_content__service.csv","test5_content__user.csv","test5_content__user_extended.csv","test5_data__ids.csv","test5_data_categories.csv","test5_product.csv","test5_service.csv","test5_service__extended.csv","test5_user__data.csv","test5_user__data_extended.csv","test5_user__extended_locker.csv","test5_user__locker.csv"
]

def OPENS(FILE):
    datum = open(FILE, "r", encoding="utf-8").read()
    return datum

def SPLITS(ROW):
    IS = False
    WAS = False
    TEMP = ""
    VALUESTEMP = []

    for i in range(0, len(ROW)):
        if ROW[i] != "," and ROW[i] != '"' or i == (len(ROW) - 1):
            if i == (len(ROW) - 1):
                TEMP += ROW[i]
                VALUESTEMP.append(TEMP)
            else:
                TEMP += ROW[i]
        elif ROW[i] == "," and IS == False:
            VALUESTEMP.append(TEMP)
            TEMP = ""
        elif ROW[i] == '"':
            if WAS is False:
                WAS = True
            if IS is False:
                IS = True
            else:
                IS = False
        elif ROW[i] == "," and IS == True:
            TEMP += ","
        
    return WAS, VALUESTEMP

# Retrieving parameters from a table with data
def PARAM(HEAD,DATA):
    TIME.append(time.time())

    TYPES = []
    MAX = []
    MIN = []

    print("Keys amount: ",len(HEAD))
    print(HEAD)
    print("Length of joined keys: ",len("".join(HEAD)))
    print("Somewhat bits in keys: ",len("".join(HEAD)) * 8)

    for i in range(0, len(HEAD)):
        MAXLENGTH=0
        MINLENGTH=0
        WAS=False

        for j in range(0, len(DATA)):
            IS,DATUM = SPLITS(DATA[j])
        
            if MAXLENGTH < len(DATUM[i]):
                MAXLENGTH = len(DATUM[i])
            if MINLENGTH > len(DATUM[i]):
                MINLENGTH = len(DATUM[i])

            if IS is True:
                WAS = IS

        MAX.append(MAXLENGTH)
        MIN.append(MINLENGTH)
        TYPES.append(WAS)

    TIME.append(time.time())

    return [TYPES, MAX, MIN]

# Test to find and print column by key
def COL(DATA, COLUMN):
    TIME.append(time.time())

    WAS = False
    TEMP = ""
    TEMPS = []

    for j in range(0, len(DATA)):
        IS, DATUM = SPLITS(DATA[j])

        if COLUMN > len(DATUM):
            TEMPS.append(DATUM[len(DATUM)])
        else:
            TEMPS.append(DATUM[COLUMN])

        if IS is True:
            WAS = IS

    TIME.append(time.time())

    return TEMPS

# Test to find and print two columns by key
def COLS(DATA, COLUMNS):
    TIME.append(time.time())

    WAS = False
    TEMP = ""
    TEMPS = []
    THETEMPS = []

    for j in range(0, len(DATA)):
        IS, DATUM = SPLITS(DATA[j])

        for COLUMN in COLUMNS:
            if COLUMN > len(DATUM):
                TEMPS.append(DATUM[len(DATUM)])
            else:
                TEMPS.append(DATUM[COLUMN])

        THETEMPS.append(TEMPS)
        TEMPS = []

    TIME.append(time.time())

    return THETEMPS

# Test to find and print specific row by column's key
def FINDS(THEDATA,KEY,ID):
    TIME.append(time.time())

    WAS = False
    TEMP = ""

    DATA = THEDATA.split("\n")

    LINESWITHCOMMA = []
    NEWDATA = []
    for j in range(0, len(DATA)):
        HAVECOMMA = False

        for jj in range(0, len(DATA[j])):
            if DATA[j][jj] == ",":
                HAVECOMMA = True

        if HAVECOMMA is True:
            LINESWITHCOMMA.append(j)
        else:
            DATA[LINESWITHCOMMA[-1]] += DATA[j]
            DATA[j] = ""
    for j in range(0, len(DATA)):
        if DATA[j] != "" and DATA[j] != []:
            NEWDATA.append(DATA[j])

    IS, HEAD = SPLITS(NEWDATA[0])
    IS = False
    POS = 0

    while (IS is False):
        POS = POS + 1
        if len(HEAD) < (POS + 2):
            IS = True
        elif HEAD[POS] == KEY:
            IS = True


    A, DATUM = SPLITS(NEWDATA[int(ID) + 1])
    TEMP = DATUM[POS]

    TIME.append(time.time())

    return TEMP

# Test to find and print rows between start and the end with specific column start and the column end #useful for image csv
def SHOW(DATA, HORIZONTALS, VERTICALS):
    TIME.append(time.time())

    WAS = False
    TEMPS = []

    S, E = HORIZONTALS[0], HORIZONTALS[1]

    if E > len(DATA):
        E = len(DATA)

    DATA = DATA[S:E]

    for j in range(0, len(DATA)):
        IS, DATUM = SPLITS(DATA[j])

        S2, E2 = VERTICALS[0], VERTICALS[1]

        if E2 > len(DATUM):
            E2 = len(DATUM)

        TEMPS.append(DATUM[S2:E2])

    TIME.append(time.time())

    return TEMPS

# Prebuilt function to split rows of data by comma or programmatically stringified double quotes
def CONVERT(DATA):
    NEWDATA=[]
    LINESWITHCOMMA = []
    for j in range(0, len(DATA)):
        HAVECOMMA = False

        for jj in range(0, len(DATA[j])):
            if DATA[j][jj] == ",":
                HAVECOMMA = True

        if HAVECOMMA == True:
            LINESWITHCOMMA.append(j)
        else:
            DATA[LINESWITHCOMMA[-1]]+=DATA[j]
            DATA[j] = ""

    for j in range(0, len(DATA)):
        if DATA[j] != "" and DATA[j] != []:
            TEMP = ""
            VALUESTEMP = []
            IS = False

            for i in range(0, len(DATA[j])):
                if DATA[j][i] != "," and DATA[j][i] != '"' or i == (len(DATA[j]) - 1):
                    if i == (len(DATA[j]) - 1):
                        TEMP += DATA[j][i]
                        VALUESTEMP.append(TEMP)
                    else:
                        TEMP += DATA[j][i]
                elif DATA[j][i] == "," and IS == False:
                    VALUESTEMP.append(TEMP)
                    TEMP = ""
                elif DATA[j][i] == '"':
                    if IS is False:
                        IS = True
                    else:
                        IS = False
                elif DATA[j][i] == "," and IS == True:
                    TEMP += ","

            NEWDATA.append(VALUESTEMP)

    return NEWDATA

# Test to print combined csv with id or uid
def UNIONS(THEDATA, SUBDATA):
    TIME.append(time.time())

    RESULT = ""
    RESULTS = []

    SUBDATA = OPENS(SUBDATA)
    GROUPDATA = [
        CONVERT(THEDATA.split("\n")),
        CONVERT(SUBDATA.split("\n"))
    ]
    # print(GROUPDATA)

    HEAD=[]
    # Union groupdata
    for i in range(0,len(GROUPDATA)):
        HEADIN=GROUPDATA[i][0]
        for i2 in range(0,len(HEADIN)):
            HEAD.append(HEADIN[i2])
    print(HEAD)
    print(len(HEAD))

    # In combined 2 files heads I am finding similar key-values
    POSES=[]
    NOTPOSES=[]
    for i in range(0,len(HEAD)):
        if i not in NOTPOSES:
            TEMPS = [i]
            for j in range((i+1),len(HEAD)):
                if j not in NOTPOSES:
                    if HEAD[i] == HEAD[j]:
                        TEMPS.append(j)
                        NOTPOSES.append(j)
            if TEMPS[-1] != i:
                POSES.append(TEMPS)
    # print(POSES)

    # In the initial (head) list of values replacing last to first and removing each key not first from POSES
    NEWDATA=[]
    for i in range(0, len(GROUPDATA)): #file
        ROW=[]
        WIDE=len(HEAD)
        for i2 in range(1, len(GROUPDATA[i][0::])): #row
            for i3 in range(0, len(GROUPDATA[i][i2])): #value
                if i2!=0 and i!=0:
                    if len(NEWDATA[i2]) < WIDE:
                        NEWDATA[i2 - 1].append(GROUPDATA[i][i2][i3])
                        # if i2+1 == len(GROUPDATA[i][0::]):
                            # To obtain data without another cycle, it should trigger the current [i] file length with exclusion of NEWDATA length
                else:
                    ROW.append(GROUPDATA[i][i2][i3])
            NEWDATA.append(ROW)
            # print(NEWDATA[i2])
            ROW=[]
        # print(GROUPDATA[i])

    NEWERDATA=[]
    for LINE in NEWDATA:
        if LINE != []:
            DIFF=len(HEAD)-len(LINE)
            if DIFF > 0:
                for i7 in range(0,DIFF):
                    LINE.append("")
            NEWERDATA.append(LINE)
    # print("NEWERDATA", len(NEWERDATA))

    NEWESTDATA=[]
    NEWESTDATA.append(HEAD)
    for LINE in NEWERDATA:
        NEWESTDATA.append(LINE)

    TIME.append(time.time())

    RESULT=NEWESTDATA
    return RESULT

if __name__ == "__main__":

    print("Start time : ", time.time())

    PARAMS = []
    COLED = []
    COLSED = []
    FOUND = []
    SHOWN = []
    UNITED = []
    for T in LOAD:
        THEDATA = OPENS(T)
        DATA = THEDATA.split("\n")

        LINESWITHCOMMA = []
        NEWDATA = []
        for j in range(0, len(DATA)):
            HAVECOMMA = False

            for jj in range(0, len(DATA[j])):
                if DATA[j][jj] == ",":
                    HAVECOMMA = True

            if HAVECOMMA is True:
                LINESWITHCOMMA.append(j)
            else:
                DATA[LINESWITHCOMMA[-1]] += DATA[j]
                DATA[j] = ""
        for j in range(0, len(DATA)):
            if DATA[j] != "" and DATA[j] != []:
                NEWDATA.append(DATA[j])

        IS,HEAD = SPLITS(NEWDATA[0])
        DATA = NEWDATA[1::]
        NEWDATA = []

        PARAMS.append(PARAM(HEAD,DATA))
        COLED.append(COL(DATA,1))
        COLSED.append(COLS(DATA, [3,4]))
        FOUND.append(FINDS(THEDATA, "price", "4"))
        SHOWN.append(SHOW(DATA, [1,3],[1,3]))
        UNITED.append(UNIONS(THEDATA, "test40.csv"))

    TEST = [
        PARAMS,
        COLED,
        COLSED,
        FOUND,
        SHOWN,
        UNITED
    ]
    # print(TEST)
    print(TIME)

    print(len(TIME))
    for i in range(0,len(TIME),2):
        print(TIME[i+1]-TIME[i])


    print("End time : ", time.time())