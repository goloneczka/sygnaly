# Import the necessary packages
import tkinter
from consolemenu import *
from consolemenu.items import *
from Operations import *
from signals.SignalContext import *
from signals.Signals import *
from tkinter import filedialog

signal1 = None
signal2 = None


def createStartMenu():
    # Create the menu
    menu = ConsoleMenu("Main menu")

    # A FunctionItem runs a Python function when selected
    draw_signal = FunctionItem("Draw one signal", loadDataMenu)
    add_signals = FunctionItem("Add two signals", twoSignals, [1])
    sub_signals = FunctionItem("Sub two signals", twoSignals, [2])
    mult_signals = FunctionItem("Mult two signals", twoSignals, [3])
    div_signals = FunctionItem("Div two signals", twoSignals, [4])

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(draw_signal)
    menu.append_item(add_signals)
    menu.append_item(sub_signals)
    menu.append_item(mult_signals)
    menu.append_item(div_signals)
    menu.show()


def chooseSignalMenu(which_signal=1):
    # Create the menu
    menu = ConsoleMenu("Choose signal")

    # A FunctionItem runs a Python function when selected
    individualSignal = FunctionItem("IndividualSignal", drawSignal,
                                    [IndividualSignal(), which_signal], should_exit=True)
    gaussSignal = FunctionItem("GaussSignal", drawSignal,
                               [GaussSignal(), which_signal], should_exit=True)
    sinusSignal = FunctionItem("SinusSignal", drawSignal,
                               [SinusSignal(), which_signal], should_exit=True)
    sinusHalfSignal = FunctionItem("SinusHalfSignal", drawSignal,
                                   [SinusHalfSignal(), which_signal], should_exit=True)
    sinusTwoHalfSignal = FunctionItem("SinusTwoHalfSignal", drawSignal,
                                      [SinusTwoHalfSignal(), which_signal], should_exit=True)
    reactSignal = FunctionItem("RectSignal", drawSignal,
                               [RectSignal(), which_signal], should_exit=True)
    triangleSignal = FunctionItem("TriangleSignal", drawSignal,
                                  [TriangleSignal(), which_signal], should_exit=True)
    rectSimetricSignal = FunctionItem("RectSimetricSignal", drawSignal,
                                      [RectSimetricSignal(), which_signal], should_exit=True)
    jumpSignal = FunctionItem("JumpSignal", drawSignal,
                              [JumpSignal(), which_signal], should_exit=True)
    individualSignalDiscreet = FunctionItem("IndividualSignalDiscreet", drawSignal,
                                            [IndividualSignalDiscreet(), which_signal], should_exit=True)
    impulsSignalDiscreet = FunctionItem("ImpulsSignalDiscreet", drawSignal,
                                        [ImpulsSignalDiscreet(), which_signal], should_exit=True)

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
    menu.show()


def showAllResultsForSignal(signal):
    signal.show_hist()
    signal.show_plot()
    printAllAdditionalInfo(signal)


def which_signal_save(signal, which):
    if which == 1:
        global signal1
        signal1 = signal
    else:
        global signal2
        signal2 = signal


def drawSignal(signal, which_signal=1):
    signalContext = SignalContext(signal)
    signal_1 = signalContext.context_sygnal()
    signal_1.save_to_file()
    showAllResultsForSignal(signal_1)
    which_signal_save(signal_1, which_signal)


def drawLoadedSignal(signal, which_signal=1):
    showAllResultsForSignal(signal)
    which_signal_save(signal, which_signal)


def twoSignals(what_should_i_do):
    # what_should_i_do -->
    # 1.Addition, 2.Subtraction, 3.Multiplication, 4.Division
    loadDataMenu(1)
    loadDataMenu(2)
    operations = Operations()
    global signal1, signal2
    if signal1 is not None and signal2 is not None:
        if what_should_i_do == 1:
            signal_result = operations.add(signal1, signal2)
            signal_result.show_plot()
            signal_result.show_hist()
            signal_result.save_to_file()
            printAllAdditionalInfo(signal_result)
        elif what_should_i_do == 2:
            signal_result = operations.sub(signal1, signal2)
            signal_result.show_plot()
            signal_result.show_hist()
            signal_result.save_to_file()
            printAllAdditionalInfo(signal_result)
        elif what_should_i_do == 3:
            signal_result = operations.mult(signal1, signal2)
            signal_result.show_plot()
            signal_result.show_hist()
            signal_result.save_to_file()
            printAllAdditionalInfo(signal_result)
        elif what_should_i_do == 4:
            signal_result = operations.div(signal1, signal2)
            signal_result.show_plot()
            signal_result.show_hist()
            signal_result.save_to_file()
            printAllAdditionalInfo(signal_result)
        else:
            print("Coś poszło nie tak. Podana opcja jest błędna.")
    else:
        print("Coś poszło nie tak . . . ")


def printAllAdditionalInfo(signal):
    print("Wartość średnia = " + str(signal.calculate_average_value()))
    print("Wartość średnia bezwzględna = " + str(signal.calculate_absolute_average_value()))
    print("Moc średnia = " + str(signal.calculate_avg_pow()))
    print("Wariacja = " + str(signal.calculate_variance()))
    print("Wartość skuteczna = " + str(signal.calculate_effective_value()))


def loadDataMenu(which_signal=1):
    # Create the menu
    menu = ConsoleMenu("Load data or create new signal")

    # A FunctionItem runs a Python function when selected
    load_data = FunctionItem("Load Data", loadDataAndDraw, [which_signal], should_exit=True)
    create_new = FunctionItem("Create new signal", chooseSignalMenu, [which_signal], should_exit=True)

    # Once we're done creating them, we just add the items to the menu
    menu.append_item(load_data)
    menu.append_item(create_new)
    menu.show()


def loadDataAndDraw(which_signal=1):
    root = tkinter.Tk()
    root.filename = tkinter.filedialog.askopenfilename()
    print(root.filename)
    root.destroy()
    counter = 0
    howManyXY = 0
    arrayX = []
    arrayY = []
    with open(root.filename, "r") as work_data:
        for line in work_data:
            if counter == 0:
                howManyXY = int(line)
            elif 0 < counter < (1 + howManyXY):
                arrayX.append(float(line))
            else:
                arrayY.append(float(line))
            counter += 1
    signal = Signal(arrayX, arrayY, 'casual')
    drawLoadedSignal(signal, which_signal)
