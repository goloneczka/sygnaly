import math

import numpy as np

from signals.SignalParams import SignalParams


class SinusSignal:

    signals_parameters = SignalParams()

    def sygnal(self):
        a, t, t1, d, n= self.signals_parameters.get_params()

        samples = np.linspace(t1, d, n)
        values = [(a * math.sin(2 * math.pi * (x - t1) / t)) for x in samples]
        return samples, values
