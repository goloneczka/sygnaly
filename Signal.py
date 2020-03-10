import math
import matplotlib.pyplot as plt


class Signal:

    def __init__(self, samples, values, tag):
        self.samples = samples
        self.values = values
        self.tag = tag

    def calculate_average_value(self):
        sigma = 0.0
        for x in self.values:
            sigma += x

        return 1 / (self.samples[-1] - self.samples[0] + 1) * sigma

    def calculate_absolute_average_value(self):
        sigma = 0.0
        for x in self.values:
            sigma += math.fabs(x)

        return 1 / (self.samples[-1] - self.samples[0] + 1) * sigma

    def calculate_avg_pow(self):
        sigma = 0.0
        for x in self.values:
            sigma += x * x

        return 1 / (self.samples[-1] - self.samples[0] + 1) * sigma

    def calculate_variance(self):
        sigma = 0.0
        avg = self.calculate_average_value()
        for x in self.values:
            sigma += (x - avg) * (x - avg)

        return 1 / (self.samples[-1] - self.samples[0] + 1) * sigma

    def calculate_effective_value(self):
        return math.sqrt(self.calculate_avg_pow())

    def show_plot(self):
        if self.tag == 'discreet':
            plt.plot(self.samples, self.values, 'ro')
        else:
            plt.plot(self.samples, self.values)

        plt.show()

    def show_hist(self):
        n = input("podaj ilosc przedzialow: ")
        if self.tag != 'discreet':
            plt.hist(self.values, bins=int(n), rwidth=0.95)

        plt.show()