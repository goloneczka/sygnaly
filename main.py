# from Menu import createStartMenu
from Conversions import Conversions, ConversionsMeasurement
from signals.SignalContext import SignalContext
from signals.Signals import IndividualSignal, GaussSignal, SinusSignal, SinusHalfSignal, TriangleSignal, \
    SinusTwoHalfSignal, RectSignal, RectSimetricSignal, JumpSignal, IndividualSignalDiscreet, ImpulsSignalDiscreet

if __name__ == "__main__":
    #   createStartMenu()
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

    signalContext = SignalContext(sinusSignal)
    signal_1 = signalContext.context_sygnal()
    signal_1.show_plot()

    connversions = Conversions()
    signal_2 = connversions.even_quantization_with_load(signal_1, 15, 6)
    signal_2.show_plot()
    signal_3 = connversions.first_holder(signal_1, 15, 30)
    signal_3.show_plot()

    connversions_meas = ConversionsMeasurement()
    print( connversions_meas.MD(signal_3), connversions_meas.MSE(signal_3), connversions_meas.SNE(signal_3))

