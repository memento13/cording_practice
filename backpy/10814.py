N =int(input())
people = list()
num = 0
for i in range(N):
    age, name =input().split()
    age = int(age)
    people.append([age, name, num])
    num = num+1
people = sorted(people,key = lambda x: (x[0],x[2]))
for i in people:
     print(i[0],i[1])