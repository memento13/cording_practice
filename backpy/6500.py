import sys
from collections import deque

numbers = [] #난수 저장

def func(number):
    number = number**2 
    number = deque(map(int,str(number)))
    temp = 8-len(number) #모자란 자릿수 확인
    for _ in range(temp): #모자란 자릿수 만큼 0 채워줌
        number.appendleft(0)
    #앞 뒤 숫자 2개씩 제거
    number.popleft()
    number.popleft()
    number.pop()
    number.pop()
    #리스트 -> 문자열 -> 숫자
    temp =''
    for i in number:
        temp+=str(i)   
    number = int(temp)
    
    if number in numbers: #난수가 이미 생성된 경우 함수 종료
        return
    else: #없는 난수인경우 등록후 다시 난수생성기 시작
        numbers.append(number)
        func(number)

if __name__ == '__main__':
    while True:
        numbers.clear()
        num = int(sys.stdin.readline())
        if num==0:
            exit(0)
        numbers.append(num)
        func(num)
        print(len(numbers))
