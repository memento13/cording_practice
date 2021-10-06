import pyautogui
import sys
import time
import os
import pytesseract
import jaydebeapi

print("좌상단 x값 ,y값, x의 길이, y의 길이 입력 ex) x y x길이 y길이 : ")
axis = list(map(int,sys.stdin.readline().split()))

# 테서렉트 ocr
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'


# 쿼리작성
sql = "insert into %s (name) values ('%s')"
tableName = ""

# 나중에 db에서 그날 출근 퇴근 리스트 받아와야함
clockonList = list()
clockoffList = list()

# 스크린샷이 저장될 경로
path = "C:\\Users\\hight\\Desktop\\autoscrean\\%s"
while True:

    pyautogui.screenshot(path % "test.png",region=(axis[0],axis[1],axis[2],axis[3]))

    text = pytesseract.image_to_string(path % "test.png",lang='kor',config='--psm 4')
    listForDB = text.strip().split("; ")

    if listForDB[0] == "출근":
        tableName = "clockon"
        if listForDB[1] in clockonList:
            os.remove(path % "test.png")
            time.sleep(10)
            continue
        else:
            clockonList.append(listForDB[1])

    elif listForDB[0] == "퇴근":
        tableName = "clockoff"
        if listForDB[1] in clockoffList:
            os.remove(path % "test.png")
            time.sleep(10)
            continue
        else:
            clockoffList.append(listForDB[1])
    else:
        os.remove(path % "test.png")
        time.sleep(10)
        continue

    # db연결
    conn = jaydebeapi.connect("org.h2.Driver","jdbc:h2:tcp://localhost/~/entry",["sa", ""],"c:\\Users\\hight\\Downloads\\h2\\bin\\h2-1.4.200.jar")
    curs = conn.cursor()

    # 쿼리전송
    curs.execute(sql % (tableName,listForDB[1]))
    conn.commit()

    # 커넥션 종료 (굳이 여기놔둬야하나?)
    conn.close()

    # 파일 삭제
    os.remove(path % "test.png")
    time.sleep(10)


