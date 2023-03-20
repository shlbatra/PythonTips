from numbers import Real


#collecting data about experiment
class Metric:
    #class level attributes so convert to dataclass -> for instance variables
    values: list[Real]
    running_total: float
    num_updates: float
    average: float

    def __init__(self):
        #dont need reset method, can do assignment in dataclass
        self.reset()

    def __str__(self):
        #dont need as dataclass already does it for you
        return f"Metric(average={self.average:0.4f})"

    def update(self, value: Real, batch_size: int):
        self.values.append(value)
        self.running_total += value * batch_size
        self.num_updates += batch_size
        self.average = self.running_total / self.num_updates

    def reset(self):
        #instead just create a new object of dataclass
        self.values: list[Real] = []
        self.running_total: float = 0.0
        self.num_updates: float = 0.0
        self.average: float = 0.0
