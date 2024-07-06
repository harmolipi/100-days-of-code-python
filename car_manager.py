import random

from car import Car

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []
        self.move_distance = STARTING_MOVE_DISTANCE

    def update(self):
        self.maybe_create_car()
        self.move_all_cars()

    def maybe_create_car(self):
        if random.randint(1, 10) == 3:
            self.cars.append(Car(random.choice(COLORS)))

    def move_all_cars(self):
        for car in self.cars:
            car.move(self.move_distance)

    def speed_up(self):
        self.move_distance += MOVE_INCREMENT

    def is_in_contact_with_car(self, player):
        for car in self.cars:
            if player.ycor() >= car.ycor() - 10 and player.ycor() <= car.ycor() + 10:
                if (
                    player.xcor() >= car.xcor() - 20
                    and player.xcor() <= car.xcor() + 20
                ):
                    return True

        return False
