import random
from typing import List

from car import Car
from player import Player

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self) -> None:
        super().__init__()
        self.cars: List[Car] = []
        self.move_distance: int = STARTING_MOVE_DISTANCE

    def update(self) -> None:
        self.maybe_create_car()
        self.move_all_cars()

    def maybe_create_car(self) -> None:
        if random.randint(1, 10) == 3:
            self.cars.append(Car(random.choice(COLORS)))

    def move_all_cars(self) -> None:
        for car in self.cars:
            car.move(self.move_distance)

    def speed_up(self) -> None:
        self.move_distance += MOVE_INCREMENT

    def is_in_contact_with_car(self, player: Player) -> bool:
        for car in self.cars:
            if (
                player.ycor() >= car.ycor() - 10 and player.ycor() <= car.ycor() + 10
            ) and (
                player.xcor() >= car.xcor() - 20 and player.xcor() <= car.xcor() + 20
            ):
                return True

        return False
