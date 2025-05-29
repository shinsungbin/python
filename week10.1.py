inFp = None
inStr = ""

inFp = open("C:\\Users\\kxsrl\\OneDrive\\바탕 화면\\파이썬\\과제\\filetest\\data1.txt", "r", encoding='UTF8')

lineNum = 1

while True:
    inStr = inFp.readline()
    if inStr == "":
        break;
    print("%d: %s" % (lineNum, inStr), end = "")
    lineNum += 1

inFp.close()