import numpy as np
from sortedcontainers import SortedSet
from Signal import Signal
from numpy import zeros, array, sign


class Conversions:

    def sampling(self, signal, freq):
        if signal.tag != 'casual':
            raise Exception("niezgodnosc typu sygnalu !")

        samples = np.linspace(signal.samples[0], signal.samples[-1], freq)
        signal_samples_list = [(np.abs(signal.samples - value)).argmin() for value in np.asarray(samples)]
        values = [signal.values[x] for x in signal_samples_list]

        return Signal(samples, values, 'discreet')

    def even_quantization_with_load(self, signal, freq, quantization_level):
        signal = self.sampling(signal, freq)
        max_val = max(signal.values)
        min_val = min(signal.values)

        tree_set = SortedSet()
        for i in range(quantization_level):
            tree_set.add(min_val + (((max_val - min_val) / quantization_level) * i))

        values = [min(tree_set, key=lambda t_v: abs(t_v - v)) for v in signal.values]

        return Signal(signal.samples, values, 'discreet')

    def zero_holder(self, signal, sampl_freq, freq):
        signal = self.sampling(signal, sampl_freq)
        step = 1 / freq
        base_step = signal.samples[1] - signal.samples[0]

        values = []
        samples = []
        for i, (x, y) in enumerate(zip(signal.samples, signal.values)):
            x1 = x + base_step
            while x < x1:
                samples.append(x)
                values.append(y)
                x += step

        return Signal(samples, values, 'casual')

    def sinc(self, t):
        return 1 if t == 0 else np.sin(np.math.pi * t) / (np.math.pi * t)

    def sinc_recon(self, signal, sampl_freq, freq):
        signal = self.sampling(signal, sampl_freq)
        base_step = signal.samples[1] - signal.samples[0]
        samples = []
        values = []
        t = signal.samples[0]

        while t < signal.samples[-1]:
            sum1 = 0.0
            for i in range(len(signal.samples)):
                sum1 += signal.values[i] * self.sinc(t / base_step - i)
            samples.append(t)
            values.append(sum1)
            t += 1/freq

        return Signal(samples, values, 'discreet')


