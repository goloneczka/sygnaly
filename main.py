# from Menu import createStartMenu
from Conversions import Conversions, ConversionsMeasurement
from Operations import Operations
from signals.SignalContext import SignalContext
from signals.Signals import IndividualSignal, GaussSignal, SinusSignal, SinusHalfSignal, TriangleSignal, \
    SinusTwoHalfSignal, RectSignal, RectSimetricSignal, JumpSignal, IndividualSignalDiscreet, ImpulsSignalDiscreet
from task3.Antene import Antene
from task3.DiscreetOperations import DiscreetOperations

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

    # signalContext = SignalContext(sinusHalfSignal)
    # signal_1 = signalContext.context_sygnal()


    # ZAD 2
    # connversions = Conversions()
    # signal_2 = connversions.even_quantization_with_load(signal_1, 15, 6)
    # signal_2.show_plot()
    # signal_3 = connversions.sinc_recon(signal_1, 50, 50)
    # signal_3.show_plot()
    #
    connversions_meas = ConversionsMeasurement()
    # print(connversions_meas.MD(signal_3), connversions_meas.MSE(signal_3), connversions_meas.SNE(signal_3))
    # connversions_meas.show_plot(signal_1, signal_3)

    # signalContext = SignalContext(sinusSignal)
    # signal_2A = signalContext.context_sygnal()
    # signal_2A.show_plot()
    #
    # signalContext = SignalContext(reactSignal)
    # signal_2 = signalContext.context_sygnal()
    # signal_2.show_plot()
    #
    # operations = Operations()
    # signal_2C = operations.add(signal_2A, signal_2)
    # signal_2C.show_plot()

    # discreet_operations = DiscreetOperations()
    # signal_3 = discreet_operations.twine(signal_2, signal_2A)
    # signal_3.show_plot()

    # signal_4 = discreet_operations.medium_filter(signal_2C, 63, 10, 80)
    # signal_4.show_plot()
    #
    # signal_4A = discreet_operations.low_filter(signal_2C, 63, 10, 80)
    # signal_4A.show_plot()

    # signal5 = discreet_operations.correlation(signal_2, signal_2A)
    # signal5.show_plot()

    antene = Antene()
    antene.basic_signal()
    antene.feedback_signal(50)





