"""

    04_attributes.py

"""


class RaceCar:
    MAX_SPEED = 245

    def __init__(self, speed):
        self.current_speed = speed

    def speed_up(self, amt):
        self.current_speed += amt
        if self.current_speed > self.MAX_SPEED:
            self.current_speed = RaceCar.MAX_SPEED


car1 = RaceCar(200)
car2 = RaceCar(230)

car1.speed_up(30)
car2.speed_up(50)
print(car1.current_speed, car2.current_speed, car1.MAX_SPEED, car2.MAX_SPEED)
