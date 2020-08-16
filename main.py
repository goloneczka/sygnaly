# from Menu import createStartMenu
import numpy as np

from Conversions import Conversions, ConversionsMeasurement
from Operations import Operations
from signals.SignalContext import SignalContext
from signals.Signals import IndividualSignal, GaussSignal, SinusSignal, SinusHalfSignal, TriangleSignal, \
    SinusTwoHalfSignal, RectSignal, RectSimetricSignal, JumpSignal, IndividualSignalDiscreet, ImpulsSignalDiscreet, \
    StFourierSinusSignal, ScFourierSinusSignal
from task3.Antene import Antene
from task3.DiscreetOperations import DiscreetOperations
from task4.Fourier import DiscreetFourier, WaveletTransform, KolosFF

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
    stFourier = StFourierSinusSignal()
    scFourier = ScFourierSinusSignal()

    signalContext = SignalContext(scFourier)
    signal_1 = signalContext.context_sygnal()
    signal_1.show_plot()

    # ZAD 2
    # connversions = Conversions()
    # signal_2 = connversions.even_quantization_with_load(signal_1, 15, 6)
    # signal_2.show_plot()
    # signal_3 = connversions.sinc_recon(signal_1, 50, 50)
    # signal_3.show_plot()
    #

    # ZAD 3
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
    #
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
    #
    # signal6 = discreet_operations.correlation_with_twine(signal_2, signal_2A)
    # signal6.show_plot()

    # antene = Antene(20, 400, 10, 4, 10)
    # values = antene.antene_diffrence(4000)
    # print("odleglosc obliczona: ", values)

    # ZAD4

    # fourier = DiscreetFourier()
    # wavelet = WaveletTransform()
    # signal_2 = fourier.transform(signal_1)
    # signal_3 = fourier.reverse_transform(signal_2)
    # signal_3.show_plot()

    # signal_2 = fourier.fast_transform(signal_1)
    # signal_3 = fourier.reverse_transform(signal_2)
    # signal_3.show_plot()

    #
    # signal_2 = wavelet.transformation(signal_1)
    # signal_3 = wavelet.reverse_transform(signal_2)
    # signal_3.show_plot()


