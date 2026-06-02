class Summator():
    m = 1
    def total(self, n):
        return sum(i ** self.m for i in range(1, n+1))
    
class SquareSummator(Summator):
    m = 2

class QubeSummator(Summator):
    m = 3

class CustomSummator(Summator):
    def __init__(self, m):
        self.m = m


print(issubclass(SquareSummator, Summator))
print(issubclass(QubeSummator, Summator))

summator1 = Summator()
summator2 = SquareSummator()
summator3 = QubeSummator()
print(summator1.total(3))
print(summator2.total(3))
print(summator3.total(3))

summator1 = Summator()
summator2 = CustomSummator(2)
summator3 = CustomSummator(3)

print(summator1.total(3))
print(summator2.total(3))
print(summator3.total(3))