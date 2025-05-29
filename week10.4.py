inFp, outFp = None, None
inStr = ""

sourcefile = input("소스 파일명을 입력하세요: ")
targetfile = input("타깃 파일명을 입력하세요: ")

inFp = open(sourcefile,"r", encoding="UTF8")
outFp = open(targetfile, "w", encoding="UTF8")

inList = inFp.readlines()
for inStr in inList:
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("---파일이 정상적으로 복사되었음---")
