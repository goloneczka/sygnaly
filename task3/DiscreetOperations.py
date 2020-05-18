import numpy as np
import matplotlib.pyplot as plt

from Signal import Signal


class DiscreetOperations:

    @staticmethod
    def twine(signal_a, signal_b):

        if len(signal_a.values) > len(signal_b.values):
            signal_a, signal_b = signal_b, signal_a

        twined_signal = []
        for i in range(len(signal_a.values) + len(signal_b.values) - 1):
            sigma = 0.0
            for j in range(len(signal_a.values)-1, 0, -1):
                sigma += signal_a.values[j] * signal_b.values[j]
        twined_signal.append(sigma)

        values = np.convolve(signal_a.values, signal_b.values)
        t1 = signal_a.samples[0] if signal_a.samples[0] < signal_b.samples[0] else signal_b.samples[0]
        samples = np.linspace(t1, signal_b.samples[-1] + signal_a.samples[-1], len(values))

        return Signal(samples, values, 'discreet')

    @staticmethod
    def hamming_window(signal_values, m):
        return [(0.53836 - (0.46164 * np.cos(2 * np.pi * i / m)) * x) for i, x in enumerate(signal_values)]

    @staticmethod
    def count_low_filter(m, fo, fp, k=-1):
        values = []
        if k == -1:
            k = 1.0 * fp/fo
        for i in range(1, m+1):
            if i == (m - 1)/2:
                values.append(2.0 / k)
            else:
                values.append(np.sin(2 * np.pi * ((i - (m - 1) / 2) / k) / (np.pi * (i - (m - 1) / 2))))

        return values

    @staticmethod
    def low_filter(basic_signal, m, fo, fp):
        values = DiscreetOperations.count_low_filter(m, fo, fp)
        samples = np.linspace(0, m, len(values))
        signal = Signal(samples, values, 'discreet')

        return DiscreetOperations.twine(basic_signal, signal)

    @staticmethod
    def medium_filter(basic_signal, m, fo, fp):
        temp_signal = DiscreetOperations.count_low_filter(m, fo, fp, fp / (fp / 4 - fo))
        values_medium_signal = [(x * 2.0 * np.sin(np.pi * i / 2.0)) for i, x in enumerate(temp_signal)]

        samples = np.linspace(0, m, len(values_medium_signal))
        signal = Signal(samples, DiscreetOperations.hamming_window(values_medium_signal, m), 'discreet')
        return DiscreetOperations.twine(basic_signal, signal)

    @staticmethod
    def correlation_with_twine(signal_a, signal_b):
        if len(signal_a.values) > len(signal_b.values):
            signal_a, signal_b = signal_b, signal_a

        signal_a.values.reverse()
        return DiscreetOperations.twine(signal_a, signal_b)

    @staticmethod
    def correlation(signal_a, signal_b):
        values = []

        for i in range(len(signal_a.values) + len(signal_b.values)):
            sum = 0
            k1min = i - (len(signal_b.values) - 1) if i >= (len(signal_b.values) - 1) else 0
            k1max = i if i < (len(signal_b.values) - 1) else (len(signal_b.values) - 1)
            k2min = (len(signal_b.values) - 1 - i) if i <= (len(signal_b.values) - 1) else 0
            k1, k2 = k1min, k2min
            while k1 <= k1max:
                sum += signal_a.values[k1] * signal_b.values[k2]
                k1 += 1
                k2 += 1
            values.append(sum)

        samples = np.linspace(0, signal_a.samples[-1] + signal_b.samples[-1], len(values))

        return Signal(samples, values, 'discreet')



