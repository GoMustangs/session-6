from person import Person

class Student(Person):

    def __init__(self, name='', grade=-1, birthdate='1/1/2000'):
        Person.__init__(self, name, grade, birthdate)

    def study(self):
        print(self.name + ' is studying')

    def do_homework(self, course):
        print(self.name + ' is doing homework for their ' + course + ' course.')

    def ask_question(self):
        print('Wait, what?')
    
    def test(self):
        print(self.name + ' is taking the test.')