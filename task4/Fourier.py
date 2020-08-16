import cmath
import time

import numpy as np

from Signal import Signal


def show_complex_signal_w1(signal):
    real_values = [y.real for y in signal.values]
    Signal(signal.samples, real_values, 'casual').show_plot()

    img_values = [y.imag for y in signal.values]
    Signal(signal.samples, img_values, 'casual').show_plot()


def show_complex_signal_w2(signal):
    module_values = [np.sqrt(y.real*y.real + y.imag*y.imag) for y in signal.values]
    Signal(signal.samples, module_values, 'casual').show_plot()
    arg_values = [np.angle(v) for v in signal.values]
    Signal(signal.samples, arg_values, 'casual').show_plot()


class DiscreetFourier:

    def transform(self, signal):

        complex_values = self.real_to_complex(signal.values)
        values = []

        start = time.time()
        for i in range(0, len(signal.values)):
            cmplx = complex(0, 0)
            for j in range(0, len(signal.values)):
                cmplx += complex_values[j] * self.reverse_wcoefficient(i, j, len(signal.values))
            values.append(cmplx / len(signal.values))

        end = time.time()
        print("(algorytm z definicji) czas dyskretnej transformaty fouriera: ", round(end - start, 6))
        signal = Signal(signal.samples, values, 'casual')
        show_complex_signal_w1(signal)
        show_complex_signal_w2(signal)
        return signal

    def reverse_transform(self, signal):
        values = []
        for i in range(0, len(signal.values)):
            val = 0
            for j in range(0, len(signal.values)):
                val += (signal.values[j] * self.wcoefficient(i, j, len(signal.values))).real
            values.append(val)

        signal = Signal(signal.samples, values, 'casual')
        return signal

    def fast_transform(self, signal):
        start = time.time()
        complex_values = self.real_to_complex(signal.values)
        transformed = self.switch_samples(complex_values)
        values = [x / len(signal.values) for x in transformed]
        end = time.time()
        print("(szybka transformata) czas dyskretnej transformaty fouriera: ", round(end - start, 6))
        signal = Signal(signal.samples, values, 'casual')
        show_complex_signal_w1(signal)
        show_complex_signal_w2(signal)
        return signal

    def switch_samples(self, values, reverse=False):

        if len(values) < 2:
            return values
        odd, even = [], []
        for i in range(0, int(len(values) / 2)):
            even.append(values[i*2])
            odd.append(values[i*2 + 1])

        value = self.connection(self.switch_samples(even, reverse),
                                self.switch_samples(odd, reverse), reverse)
        return value

    def connection(self, even, odd, reverse):
        values, right_values = [], []
        for i in range(0, len(odd)):
            if not reverse:
                values.append(even[i] + self.wcoefficient(i, 1, len(odd)*2) * odd[i])
                right_values.append(even[i] - self.wcoefficient(i, 1, len(odd) * 2) * odd[i])
            else:
                values.append(even[i] + self.reverse_wcoefficient(i, 1, len(odd) * 2) * odd[i])
                right_values.append(even[i] - self.reverse_wcoefficient(i, 1, len(odd) * 2) * odd[i])
        values.extend(right_values)
        return values

    @staticmethod
    def wcoefficient(param, param1, n):
        return cmath.exp(complex(0, -2 * np.pi * param1 * param / n))

    @staticmethod
    def reverse_wcoefficient(param, param1, n):
        return cmath.exp(complex(0, 2 * np.pi * param1 * param / n))

    @staticmethod
    def real_to_complex(values):
        return [(complex(x, 0)) for x in values]


class WaveletTransform:

    @staticmethod
    def six_row():
        return [0.47046721, 1.14111692, 0.650365, -0.19093442, -0.12083221, 0.0498175]

    @staticmethod
    def reverse_six_row():
        return [0.0498175, 0.12083221, -0.19093442, -0.650365, 1.14111692, -0.47046721]

    def transformation(self, signal):
        start = time.time()
        h_samples = np.convolve(signal.values, self.six_row())
        g_samples = np.convolve(signal.values, self.reverse_six_row())

        h_half = [x for i, x in enumerate(h_samples) if i % 2 == 0]
        g_half = [x for i, x in enumerate(g_samples) if i % 2 != 0]

        values = []
        for i in range(0, len(g_half)):
            values.append(complex(h_half[i], g_half[i]))
        end = time.time()
        print("dyskretna transformata falkowa: ", round(end - start, 6))

        signal = Signal(np.linspace(0, 10, len(values)), values, 'casual')
        show_complex_signal_w1(signal)
        show_complex_signal_w2(signal)
        return signal

    def reverse_transform(self, signal):

        h_samples, g_samples = [], []
        for i in range(0, len(signal.values)):
            h_samples.append(signal.values[i].real)
            h_samples.append(0)
            g_samples.append(0)
            g_samples.append(signal.values[i].imag)

        h_result = np.convolve(h_samples, list(reversed(self.six_row())))
        g_result = np.convolve(g_samples, list(reversed(self.reverse_six_row())))

        values = [(h_result[i] + g_result[i])/2 for i in range(len(g_result))]
        return Signal(np.linspace(0, 10, len(values)), values, 'casual')


class KolosFF:

    def fast_transform_kol(self, arrayVal):

        complex_values = self.real_to_complex(arrayVal)
        transformed = self.switch_samples(complex_values)
        values = [x / len(arrayVal) for x in transformed]
        return values

    def switch_samples(self, values, reverse=False):

        if len(values) < 2:
            return values
        odd, even = [], []
        for i in range(0, int(len(values) / 2)):
            even.append(values[i*2])
            odd.append(values[i*2 + 1])

        value = self.connection(self.switch_samples(even, reverse),
                                self.switch_samples(odd, reverse), reverse)
        print(value)
        return value

    def connection(self, even, odd, reverse):
        values, right_values = [], []
        for i in range(0, len(odd)):
            if not reverse:
                values.append(even[i] + self.wcoefficient(i, 1, len(odd)*2) * odd[i])
                right_values.append(even[i] - self.wcoefficient(i, 1, len(odd) * 2) * odd[i])
            else:
                values.append(even[i] + self.reverse_wcoefficient(i, 1, len(odd) * 2) * odd[i])
                right_values.append(even[i] - self.reverse_wcoefficient(i, 1, len(odd) * 2) * odd[i])
        values.extend(right_values)
        return values

    @staticmethod
    def wcoefficient(param, param1, n):
        return cmath.exp(complex(0, -2 * np.pi * param1 * param / n))

    @staticmethod
    def reverse_wcoefficient(param, param1, n):
        return cmath.exp(complex(0, 2 * np.pi * param1 * param / n))

    @staticmethod
    def real_to_complex(values):
        return [(complex(x, 0)) for x in values]

    @staticmethod
    def correlation_with_twine(val):
        values = []

        for i in range(len(val) + len(val)):
            sum = 0
            k1min = i - (len(val) - 1) if i >= (len(val) - 1) else 0
            k1max = i if i < (len(val) - 1) else (len(val) - 1)
            k2min = (len(val) - 1 - i) if i <= (len(val) - 1) else 0
            k1, k2 = k1min, k2min
            while k1 <= k1max:
                sum += val[k1] * val[k2]
                k1 += 1
                k2 += 1
            values.append(sum)

        print(values)

