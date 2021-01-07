class Car:
    def __init__(self,color,price,speed=0):
        self.color=color
        self.price=price
        self.speed=speed
    def print_info(self):
        print(f"색깔은 {self.color}  가격은 {self.price}")
    
    def move(self):
        self.speed+=1
        print(f"현재 속도는 {self.speed}입니다")

    def stop(self):
        self.speed=0
        print("멈춤")

class Sport(Car):
    def __init__(self,color,price,boost=False):
        Car.__init__(self,color,price)
        self.boost=boost

    def on_boost(self):
        self.boost=True
        print("부스터가 켜졌습니다")
    def off_boost(self):
        self.boost=False
        print("부스터가 꺼졌습니다")

    def stop(self):
        self.off_boost()
        Car.stop(self)

    def move(self):
        if self.boost:
            Car.move(self)
            Car.move(self)
        else:
            Car.move(self)

    def print_info(self):
        Car.print_info(self)
        print("스포츠카입니다")        
car=Sport("노랑",1)
car.print_info()

while True:
    op=input("1.move 2.stop 3.on_boost 4.off_boost 5.exit : ")
    if op=='1':
        car.move()
    elif op=='2':
        car.stop()
    elif op=='3':
        car.on_boost()
    elif op=='4':
        car.off_boost()
    else:
        break

'learn by sunsu2737'