import pytesseract
import jaydebeapi

# 테서렉트 ocr
pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract'

# 파일명
text = pytesseract.image_to_string('C:\\Users\\hight\\Desktop\\tesserTest.png',lang='kor',config='--psm 4')
print(text)

# ocr 데이터 파싱
listForDB = text.strip().split("; ")

# db연결
conn = jaydebeapi.connect("org.h2.Driver","jdbc:h2:tcp://localhost/~/entry",["sa", ""],"c:\\Users\\hight\\Downloads\\h2\\bin\\h2-1.4.200.jar")
curs = conn.cursor()

# 쿼리작성
sql = "insert into %s (name) values ('%s')"
tableName = ""

if listForDB[0] == "출근":
    tableName = "clockon"
elif listForDB[0] == "퇴근":
    tableName = "clockoff"
else:
    # 추후 파일 삭제
    pass

# 쿼리 전송
curs.execute(sql % (tableName,listForDB[1]))
conn.commit()
conn.close()