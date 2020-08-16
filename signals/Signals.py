import math
import random

import numpy as np

from Signal import Signal
from signals.SignalsParams import SignalsParams
from random import randint


class IndividualSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t1, d, n = self.signals_parameters.get_params_gauss()

        samples = np.linspace(t1, d, n)
        values = [random.uniform(int(-a), int(a)) for x in samples]
        return Signal(samples, values, 'casual')


class GaussSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t1, d, n = self.signals_parameters.get_params_gauss()

        samples = np.linspace(t1, d, n)
        values = [(1 / math.sqrt(2 * math.pi) * math.exp((-x * x) / 2)) for x in samples]

        return Signal(samples, values, 'casual')


class SinusSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t, t1, d, n = self.signals_parameters.get_params()

        samples = np.linspace(t1, d, n)
        values = [(a * math.sin(2 * math.pi * (x - t1) / t)) for x in samples]

        return Signal(samples, values, 'discreet')


class SinusHalfSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t, t1, d, n = self.signals_parameters.get_params()

        samples = np.linspace(t1, d, n)
        values = [1 / 2 * a * (math.sin(2 * math.pi * (x - t1) / t) +
                               math.fabs(math.sin(2 * math.pi * (x - t1) / t))) for x in samples]

        return Signal(samples, values, 'discreet')


class SinusTwoHalfSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t, t1, d, n = self.signals_parameters.get_params()

        samples = np.linspace(t1, d, n)
        values = [a * math.fabs(math.sin(2 * math.pi * (x - t1) / t)) for x in samples]

        return Signal(samples, values, 'discreet')


class RectSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t, t1, d, kw, n = self.signals_parameters.get_params_react()

        samples = np.linspace(t1, d, n)
        values = [a if x < kw * t + t * int(x / t) else 0 for x in samples]

        return Signal(samples, values, 'discreet')


class RectSimetricSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t, t1, d, kw, n = self.signals_parameters.get_params_react()

        samples = np.linspace(t1, d, n)
        values = [a if x < kw * t + t * int(x / t) else -a for x in samples]

        return Signal(samples, values, 'casual')


class TriangleSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t, t1, d, kw, n = self.signals_parameters.get_params_triangle()

        samples = np.linspace(t1, d, n)
        values = [a * (x - int(x / t) * t - t1) / (kw * t) if x < kw * t + t * int(x / t)
                  else -a * (x - int(x / t) * t - t1) / (t - kw * t) + a / (1 - kw) for x in samples]

        return Signal(samples, values, 'discreet')


class JumpSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t1, d, ts, n = self.signals_parameters.get_params_jump()

        samples = np.linspace(t1, d, n)
        values = [a if x > ts else 1 / 2 * a if x == ts else 0 for x in samples]

        return Signal(samples, values, 'casual')


class IndividualSignalDiscreet:
    signals_parameters = SignalsParams()

    def signal(self):
        a, n1, ns, f = self.signals_parameters.get_params_discreet_1()

        samples = np.linspace(n1, ns * 2, int(f) * ns * 2)
        values = [a if x == ns else 0 for x in samples]
        return Signal(samples, values, 'discreet')


class ImpulsSignalDiscreet:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t1, d, f, p = self.signals_parameters.get_params_discreet_2()

        samples = []
        i = t1
        while i <= d:
            samples.append(i)
            i += 1 / f

        values = [a if randint(1, 100) / 100 < p else 0 for x in samples]
        return Signal(samples, values, 'discreet')


class StFourierSinusSignal:

    def signal(self):
        t1, d, n, t = 0, 10, 512, 1/16
        samples = np.linspace(t1, d, n)

        values1 = [(2 * math.sin(math.pi/2 + math.pi * (x - t1))) for x in samples]
        values2 = [(5 * math.sin(math.pi / 2 + 4 * math.pi * (x - t1))) for x in samples]

        values = [values1[i] + values2[i] for i in range(len(values2))]

        return Signal(samples, values, 'casual')


class ScFourierSinusSignal:

    def signal(self):
        t1, d, n, t = 0, 10, 512, 1/16
        samples = np.linspace(t1, d, n)

        values1 = [(2 * math.sin(math.pi * (x - t1))) for x in samples]
        values2 = [(math.sin(2 * math.pi * (x - t1))) for x in samples]
        values3 = [(5 * math.sin(4 * math.pi * (x - t1))) for x in samples]

        values = [values1[i] + values2[i] + values3[i] for i in range(len(values2))]

        return Signal(samples, values, 'casual')