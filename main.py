
from signals.SignalContext import SignalContext
from signals.Signals import SinusHalfSignal, SinusTwoHalfSignal, GaussSignal, SinusSignal, RectSignal, TriangleSignal, \
    RectSimetricSignal, JumpSignal, IndividualSignalDiscreet, ImpulsSignalDiscreet, IndividualSignal

if __name__ == "__main__":
    # sygnaly
    individualSignal = IndividualSignal()
    gaussSignal = GaussSignal()
    sinusSignal = SinusSignal()
    sinusHalfSignal = SinusHalfSignal()
    sinusTwoHalfSignal = SinusTwoHalfSignal()
    reactSignal = RectSignal()
    triangleSignal = TriangleSignal()
    rectSimetricSignal = RectSimetricSignal()
    jumpSignal = JumpSignal()
    individualSignalDiscreet = IndividualSignalDiscreet()
    impulsSignalDiscreet = ImpulsSignalDiscreet()
    signalContext = SignalContext(individualSignal)
    samples, values = signalContext.context_sygnal()
