# Import the necessary packages
from consolemenu import *
from consolemenu.items import *

from signals.SignalContext import *
from signals.Signals import *


def createStartMenu():
    # Create the menu
    menu = ConsoleMenu("Main menu")

    # Create some items
    # A FunctionItem runs a Python function when selected
    draw_signal = FunctionItem("Draw one signal", chooseSignalMenu)
    add_signals = FunctionItem("Add two signals", twoSignals)
    sub_signals = FunctionItem("Sub two signals", twoSignals)
    mult_signals = FunctionItem("Mult two signals", twoSignals)
    div_signals = FunctionItem("Div two signals", twoSignals)

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(draw_signal)
    menu.append_item(add_signals)
    menu.append_item(sub_signals)
    menu.append_item(mult_signals)
    menu.append_item(div_signals)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()


def chooseSignalMenu():
    # Create the menu
    menu = ConsoleMenu("Choose signal")

    # Create some items
    # A FunctionItem runs a Python function when selected
    individualSignal = FunctionItem("IndividualSignal", drawSignal,
                                    [IndividualSignal()], should_exit=True)
    gaussSignal = FunctionItem("GaussSignal", drawSignal,
                               [GaussSignal()], should_exit=True)
    sinusSignal = FunctionItem("SinusSignal", drawSignal,
                               [SinusSignal()], should_exit=True)
    sinusHalfSignal = FunctionItem("SinusHalfSignal", drawSignal,
                                   [SinusHalfSignal()], should_exit=True)
    sinusTwoHalfSignal = FunctionItem("SinusTwoHalfSignal", drawSignal,
                                      [SinusTwoHalfSignal()], should_exit=True)
    reactSignal = FunctionItem("RectSignal", drawSignal,
                               [RectSignal()], should_exit=True)
    triangleSignal = FunctionItem("TriangleSignal", drawSignal,
                                  [TriangleSignal()], should_exit=True)
    rectSimetricSignal = FunctionItem("RectSimetricSignal", drawSignal,
                                      [RectSimetricSignal()], should_exit=True)
    jumpSignal = FunctionItem("JumpSignal", drawSignal,
                              [JumpSignal()], should_exit=True)
    individualSignalDiscreet = FunctionItem("IndividualSignalDiscreet", drawSignal,
                                            [IndividualSignalDiscreet()], should_exit=True)
    impulsSignalDiscreet = FunctionItem("ImpulsSignalDiscreet", drawSignal,
                                        [ImpulsSignalDiscreet()], should_exit=True)

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(individualSignal)
    menu.append_item(gaussSignal)
    menu.append_item(sinusSignal)
    menu.append_item(sinusHalfSignal)
    menu.append_item(sinusTwoHalfSignal)
    menu.append_item(reactSignal)
    menu.append_item(triangleSignal)
    menu.append_item(rectSimetricSignal)
    menu.append_item(jumpSignal)
    menu.append_item(individualSignalDiscreet)
    menu.append_item(impulsSignalDiscreet)

    # Finally, we call show to show the menu and allow the user to interact
    menu.show()


def drawSignal(signal):
    signalContext = SignalContext(signal)
    signal_1 = signalContext.context_sygnal()
    signal_1.show_hist()
    signal_1.show_plot()
    print("Wartość średnia = " + str(signal_1.calculate_average_value()))
    print("Wartość średnia bezwzględna = " + str(signal_1.calculate_absolute_average_value()))
    print("Moc średnia = " + str(signal_1.calculate_avg_pow()))
    print("Wariacja = " + str(signal_1.calculate_variance()))
    print("Wartość skuteczna = " + str(signal_1.calculate_effective_value()))


def twoSignals():
    print("2 Signals")
