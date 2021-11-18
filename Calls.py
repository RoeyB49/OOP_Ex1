import csv


class Calls:
    def __init__(self):
        self.elevCalls = []

    def from_csv(self, file_name):
        try:
            my_list = []
            with open(file_name, 'r') as f:
                reader = csv.reader(f)
                for row in reader:
                    my_list.append(float(row[1]))
                    my_list.append(int(row[2]))
                    my_list.append(int(row[3]))
                    self.elevCalls.append(my_list)
                    my_list = []
        except IOError as e:
            print(e)

    def __str__(self) -> str:
        return f"{self.elevCalls}"

    def __repr__(self) -> str:
        return f"{self.elevCalls}"

if __name__ == '__main__':
    c = Calls()
    c.from_csv("Calls_d.csv")
    print(c)
