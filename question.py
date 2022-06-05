import random

class Question:
    def generate(self):
        ran1 = int(random.randrange(1, 30))
        ran2 = int(random.randrange(1, 30))
        answer = ran1+ran2
        print('what is ', int(ran1), '+', int(ran2), '=')
        uin = int(input("what is your answer? "))
        if uin == answer:
            print("correct")
        else:
            print("incorrect")