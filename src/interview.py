

class Interview(object):

    def __init__(self, data, hour, company):
        self.data = data
        self.hour = hour
        self.company = company

    # def set(self):
    #     self.data = '06/06/2018'
    #     self.company = 'AC DC'
    #     self.hour = '3 pm'

    def print(self):
        print(self.data)
        print(self.hour)
        print(self.company)


# a = Interview(2,1,'ABC')
# a.hour = '3 pm'
# a.data = '06/06/2018'

# a.print()


class Detals(Interview):

    def questions(self, question, answer):
        self.questions = question
        self.answer = answer

andrey = Detals('06/06/2018', '3pm', 'DDD')
andrey.hour = '3-30 pm'
andrey.company = 'AC DC'
andrey.data = '06/06/2018'
print(andrey)
andrey.print()