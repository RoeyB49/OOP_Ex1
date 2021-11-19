import json
from Elevator import Elevator


class Building:
    def __init__(self) -> None:
        self.minFloor = 0
        self.maxFloor = 0
        self.elevators = {}
        self.lastFloor = []

    def from_json(self, file_name):
        try:
            with open(file_name, "r") as fp:
                new_p = {}
                di = json.load(fp)
                self.minFloor = di["_minFloor"]
                self.maxFloor = di["_maxFloor"]
                for i in di["_elevators"]:
                    # for key, value in i.items():
                    p = Elevator(**i)
                    self.lastFloor.append(0)
                    new_p[p._id] = p
                self.elevators = new_p
                # print(new_p)
                # print(self.lastFloor)
        except IOError as e:
            print(e)

    def __str__(self) -> str:
        # return (self._minFloor, self._maxFloor, self._elevators)
        return f"{self.minFloor} , {self.maxFloor} , {self.elevators}"

    def __repr__(self) -> str:
        return f"{self.minFloor} , {self.maxFloor} , {self.elevators}"


