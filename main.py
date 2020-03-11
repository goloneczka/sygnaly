from Menu import createStartMenu
from Operations import Operations
from signals.SignalContext import SignalContext
from signals.Signals import SinusHalfSignal, SinusTwoHalfSignal, GaussSignal, SinusSignal, RectSignal, TriangleSignal, \
    RectSimetricSignal, JumpSignal, IndividualSignalDiscreet, ImpulsSignalDiscreet, IndividualSignal


if __name__ == "__main__":
    # sygnaly
    individualSignal = IndividualSignal()
    gaussSignal = GaussSignal()  # ten sygnal jest cos nie halo
    sinusSignal = SinusSignal()
    sinusHalfSignal = SinusHalfSignal()
    sinusTwoHalfSignal = SinusTwoHalfSignal()
    reactSignal = RectSignal()
    triangleSignal = TriangleSignal()
    rectSimetricSignal = RectSimetricSignal()
    jumpSignal = JumpSignal()
    individualSignalDiscreet = IndividualSignalDiscreet()
    impulsSignalDiscreet = ImpulsSignalDiscreet()

    createStartMenu()
    # signalContext = SignalContext(sinusSignal)
    # signal_1 = signalContext.context_sygnal()
    # signal_1.show_hist()
    # signal_1.show_plot()
    #
    # signalContext = SignalContext(sinusSignal)
    # signal_2 = signalContext.context_sygnal()
    # signal_2.show_plot()
    #
    # print(signal_1.calculate_absolute_average_value())
    #
    # operations = Operations()
    # signal_3 = operations.mult(signal_1, signal_2)
    # signal_3.show_plot()
