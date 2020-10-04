import sys
# 12*60*60 = 43200 
class clock:
    def __init__(self, second):
        self.second = second # 초침이동거리
        self.h = 0
        self.m = 0
        self.s = 0
        self.twelveHoursOver = 0 #12시 지난 횟수
    
    def TimeAlgin(self):
        if self.s <0:
            self.m -= (abs(self.s)//60)+1
            self.s = 60 - (abs(self.s)%60)
        if self.s>=60:
            self.m += self.s//60
            self.s = self.s%60 
        
        if self.m<0:
            self.h -= (abs(self.m)//60)+1
            self.m = 60 - (abs(self.m)%60)
        if self.m>=60:
            self.h += self.m//60
            self.m = self.m%60

        if self.h <0:
            self.h = 12-(abs(self.h)%12)
        if self.h>=12:
            self.twelveHoursOver +=self.h//12
            self.h = self.h%12
            

    def SecondMove(self): #초침 움직이는 함수
        self.s +=self.second
        self.TimeAlgin()

    def getTime(self):
        return "{}시{}분{}초".format(self.h,self.m,self.s)
    
    def TwelveHoursCK(self):# 24시간 초과유뮤 체크
        if self.twelveHoursOver>=2 and self.s>0:  #12시간을 두번 수행했고 초침이 0 초과일때 반복문 중단
            return False
        return True


a,b = map(int,sys.stdin.readline().split())
if a==0:
    clockTest = clock(0.0)
else:
    clockTest = clock(a/b)
clockNomal = clock(1.0)

result = 0
while(clockNomal.TwelveHoursCK()):
    if clockNomal.getTime() == clockTest.getTime():
        result +=1
    clockTest.SecondMove()
    clockNomal.SecondMove()

print(result-1)
