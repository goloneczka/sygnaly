import math

import numpy as np

from Signal import Signal
from task3.DiscreetOperations import DiscreetOperations


class Antene:

    def __init__(self, sample_freq, buffor, count_meassurment, reporting_period, real_speed):
        self.sample_freq = sample_freq
        self.buffor = buffor
        self.count_meassurment = count_meassurment
        self.reporting_period = reporting_period
        self.real_speed = real_speed

    def create_signal(self, start_time, duration):
        values, values1, values2, res, x = [], [], [], [], []
        j = start_time
        while j < start_time + duration:
            values.append(3 * math.sin(2 * math.pi * j / 4))
            values1.append(2 * math.sin(2 * math.pi * j / 2))
            values2.append(1 * math.sin(2 * math.pi * j / 1))
            res.append(values[-1] + values1[-1] + values2[-1])
            x.append(j)
            j += 1 / self.sample_freq

        return Signal(x, res, 'discreet')

    def count_distance(self, abstract_speed):
        result_distances = []
        duration = self.buffor / self.sample_freq
        for i in range(0, self.count_meassurment * self.reporting_period, self.reporting_period):
            delay = i * self.real_speed * 2 / abstract_speed
            correlation_samples = DiscreetOperations.correlation_with_twine(
                self.create_signal(i - duration, duration),
                self.create_signal(i - delay, duration))
            result_distances.append(self.calculate_distance(correlation_samples.values, abstract_speed))
        return result_distances

    def calculate_distance(self, twined_values, abstract_speed):
        second_half = twined_values[int(len(twined_values) / 2):]
        max_sample = np.argmax(second_half)
        t_delay = max_sample / self.sample_freq
        return round(t_delay * abstract_speed / (max_sample + len(second_half)) / 2, 2)

    def original_distance(self):
        values = []
        for i in range(0, self.count_meassurment * self.reporting_period, self.reporting_period):
            values.append(i * self.real_speed)
        return values

    def antene_diffrence(self, speed_abs):
        values1 = self.original_distance()
        print("odleglosc rzeczywista: ", values1)
        values2 = self.count_distance(speed_abs)
        res_list = [math.fabs(values1[i] - values2[i]) for i in range(len(values1))]
        return res_list
