import csv
from Building import Building
from Calls import Calls

class Ex1:
    def __init__(self, buildingJson, callsCsv) -> None:  ## , output) :
        self.b = Building()
        self.c = Calls()
        self.b.from_json(buildingJson)
        self.e = self.b.elevators
        self.c.from_csv(callsCsv)
        self.assignedElev = []
        for i in self.c.elevCalls:
            self.assignedElev.append(self.assignElev(self.b, i))
        # for i in self.assignedElev:
        #     print(i)
        self.save_csv(self.assignedElev, callsCsv)

    def assignElev(self, b, call):
        min = self.calculateTime(b.lastFloor[0], b.elevators[0], call)
        elev = b.elevators[0]._id  #
        b.lastFloor[elev] = call[2]  #
        elev = 0
        for i in b.elevators:
            temp = self.calculateTime(b.lastFloor[i], b.elevators[i], call)
            if temp < min:
                min = temp
                elev = b.elevators[i]._id
                b.lastFloor[elev] = call[2]
        # print(b.lastFloor)
        return elev

    # CloseTime + StartTime + df/speed + StopTime + OpenTime (df == |floor_a-floor_b|).
    def calculateTime(self, lastFloor, elev, call):
        df = abs(call[2] - call[1])
        return elev._closeTime + elev._startTime + (df / elev._speed) + elev._stopTime + elev._openTime + abs(
            lastFloor - call[1])

    def save_csv(self, assignedElevList, file_name):
        try:
            with open(file_name, "r") as r:
                r = csv.reader(r)
                lines = list(r)
                index = 0
                for i in lines:
                    i[5] = self.assignedElev[index]
                    index += 1
            with open("output.csv", "w", newline='') as w:
                w = csv.writer(w)
                w.writerows(lines)
        except IOError as e:
            print(e)


if __name__ == '__main__':
    #     # b = Building()
    #     # b.from_json("B1.json")
    #     # print(b)
    #     # c = Calls()
    #     # c.from_csv("Calls_a.csv")
    #     # print(c)
    ans = Ex1("B5.json", "Calls_a.csv")
    # print(ans)
