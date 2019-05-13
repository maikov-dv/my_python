class Human:
    def __init__(self, name):
        self.name = name
        self._years = 0
        print('Родился человек с именем ' + self.name)

    def eating(self):
        print(self.name + ' ест')   

    def sleeping(self):
        print(self.name + ' спит')

    def working(self):
        if self._years < 18:
            print(self.name + ' еще не работает')
        if 18 <= self._years < 65:
            print(self.name + ' работает')
        elif self._years >= 65:
            print(self.name + ' на пенсии')
        
    def relaxing(self):
        print(self.name + ' отдыхает')

    def growing(self):
        print(self.name + ' отмечает день рождения!')
        self._years += 1

class Life:
    def life(self, human, years=70):
        while years:            
            human.growing()
            human.eating()
            human.sleeping()
            human.working()
            human.relaxing()
            years -= 1
        
petr = Human('Петр')
life_petr = Life()
life_petr.life(petr)
