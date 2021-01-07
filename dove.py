class Dove:
    def __init__(self,color,speed=0):
        self.speed=speed
        self.color=color
        self.speed=speed

    def print_info(self):
        print(f'나는 {self.color} 비둘기에요')
        print(f'스피드는 {self.speed}이죠')

    def fly(self):
        self.speed+=1
        print(f'현재 속도는 {self.speed}입니다')
    
    def stop(self):
        self.speed=0
        print('추락')

    def close(self):
        print('꿈뻑!')

    def feed(self):
        print('쪼기')

class Condition(Dove):
    def __init__(self,color,con,bangbang=False):
        Dove.__init__(self,color)
        self.bangbang=bangbang
        self.con=con

    # def start_bang(self):
    #     self.bangbang=True
    #     print('머리돌리기 mode')
    def end_bang(self):
        self.bangbang=False
        print('머리돌리기 그만')
    
    def fly(self):
        if self.con=='crazy':
            self.bangbang=True
            if self.bangbang:
                Dove.fly(self)
                Dove.fly(self)
                Dove.fly(self)
                print(f'{self.speed}의 속도로 날고 있습니다')
        else:

            Dove.fly(self)
            print('정상적으로 날아요')
            print(f'{self.speed}의 속도로 날고 있습니다')

    def stop(self):
        self.end_bang()
        Dove.stop(self)

    def print_info(self):
        Dove.print_info(self)
        print(f'내 상태는 {self.con}이에요')

# pigeon=Condition('흰색','normal')
pigeon=Condition('흰색','crazy')
pigeon.print_info()

while True:
    option=input('1.fly 2.stop 3.end_bang 4.close 5.feed : ')
    if option=='1':
        pigeon.fly()
    elif option=='2':
        pigeon.stop()
    elif option=='3':
        pigeon.end_bang()
    elif option=='4':
        pigeon.close()
    elif option=='5':
        pigeon.feed()
    else:
        break