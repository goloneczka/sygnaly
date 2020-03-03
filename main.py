import matplotlib.pyplot as plt
from signals.GaussSignal import GaussSignal
from signals.SignalContext import SignalContext
from signals.SinusSignal import SinusSignal

if __name__ == "__main__":
    gaussSignal = GaussSignal()
    sinusSignal = SinusSignal()
    signalContext = SignalContext(sinusSignal)
    samples, values = signalContext.context_sygnal()

    plt.plot(samples, values)
    plt.show()
