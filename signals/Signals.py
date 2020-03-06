import math
import numpy as np

from Signal import Signal
from signals.SignalsParams import SignalsParams
from random import randint


class IndividualSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t1, d, n = self.signals_parameters.get_params_gauss()

        samples = np.linspace(t1, d, n)
        values = [randint(int(-a), int(a)) for x in samples]

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

        return Signal(samples, values, 'casual')


class SinusHalfSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t, t1, d, n = self.signals_parameters.get_params()

        samples = np.linspace(t1, d, n)
        values = [1 / 2 * a * (math.sin(2 * math.pi * (x - t1) / t) +
                               math.fabs(math.sin(2 * math.pi * (x - t1) / t))) for x in samples]

        return Signal(samples, values, 'casual')


class SinusTwoHalfSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t, t1, d, n = self.signals_parameters.get_params()

        samples = np.linspace(t1, d, n)
        values = [a * math.fabs(math.sin(2 * math.pi * (x - t1) / t)) for x in samples]

        return Signal(samples, values, 'casual')


class RectSignal:
    signals_parameters = SignalsParams()

    def signal(self):
        a, t, t1, d, kw, n = self.signals_parameters.get_params_react()

        samples = np.linspace(t1, d, n)
        values = [a if x < kw * t + t * int(x / t) else 0 for x in samples]

        return Signal(samples, values, 'casual')


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
        a, t, t1, d, kw, n = self.signals_parameters.get_params_react()

        samples = np.linspace(t1, d, n)
        values = [a * (x - int(x / t) * t - t1) / (kw * t) if x < kw * t + t * int(x / t)
                  else -a * (x - int(x / t) * t - t1) / (t - kw * t) + a / (1 - kw) for x in samples]

        return Signal(samples, values, 'casual')


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
        print(samples)
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
