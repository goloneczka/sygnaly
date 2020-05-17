import math

import numpy as np

from Signal import Signal
from task3.DiscreetOperations import DiscreetOperations


class Antene:

    def __init__(self, duration, points, period, buffor):
        self.duration = duration
        self.points = points
        self.period = period
        self.buffor = buffor

    def basic_signal(self, i, t1=0):
        d = self.duration
        n = self.points
        samples = np.linspace(i, d, n)
        values = [(3 * math.sin(2 * math.pi * (x + t1) / 30)) for x in samples]
        values1 = [(2 * math.sin(2 * math.pi * (x + t1) / 70)) for x in samples]
        values2 = [(1 * math.sin(2 * math.pi * (x + t1) / 66)) for x in samples]

        res_list = [values[i] + values1[i] + values2[i] for i in range(len(values1))]

        return Signal(samples, res_list, 'discreet')

    def feedback_signal(self, i, n):
        Antene.basic_signal(i, n)

    def count_distance(self, count_meassurment, reporting_period, real_speed, abstract_speed):
        result_distances = []
        duration = self.buffor / (self.duration / self.points)
        for i in range(0, count_meassurment * reporting_period, reporting_period):
            delay = i * real_speed * 2 / abstract_speed
            correlation_samples = DiscreetOperations.correlation_with_twine(
                self.basic_signal(self.period, i - duration, duration, (self.duration / self.points)),
                self.basic_signal(self.period, i - delay, duration, (self.duration / self.points)))
            result_distances.append(correlation_samples.values)

    def calculate_distance(self, twined_values):
        max_value_second_half = max(twined_values[len(twined_values) / 2:])
        max_sample = twined_values.index(max_value_second_half)
        t_delay = max_sample / (self.duration / self.points)    # duration / point ???


