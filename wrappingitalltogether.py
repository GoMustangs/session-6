from question import Question
from student import Student

nme = str(input("what is the student's name? "))
grd = int(input("what is the students grade? "))

stu = Student(nme,grd,'1/1/2000')

stu.test()

que = Question()

correct=0
for x in range(5):
    que.generate()