import matplotlib.pyplot as plt


class SignalParams:
    n = 200  # czestosc probkowania

    def get_params(self):
        a = input("podaj amplitude (A):")
        t = input("podaj okres (T): ")
        t1 = input("podaj czas poczatkowy (t1): ")
        d = input("podaj czas trwania (d): ")
        return float(a), float(t), float(t1), float(d) + float(t1), self.n

    def get_params_gauss(self):
        a = input("podaj amplitude (A):")
        t1 = input("podaj czas poczatkowy (t1): ")
        d = input("podaj czas trwania (d): ")
        return float(a), float(t1), float(d) + float(t1), self.n

    def get_params_react(self):
        a = input("podaj amplitude (A):")
        t = input("podaj okres (T): ")
        t1 = input("podaj czas poczatkowy (t1): ")
        d = input("podaj czas trwania (d): ")
        k = input("podaj wspolczynnik wypelnienia (k): ")
        return float(a), float(t), float(t1), float(d) + float(t1), float(k), self.n

    def get_params_jump(self):
        a = input("podaj amplitude (A):")
        t1 = input("podaj czas poczatkowy (t1): ")
        d = input("podaj czas trwania (d): ")
        t = input("podaj wspolczynnik wypelnienia (t): ")
        return float(a), float(t1), float(d) + float(t1), float(t), self.n

    def get_params_discreet_1(self):
        a = input("podaj amplitude (A):")
        n1 = input("podaj numer pierwszej probki (n1): ")
        ns = input("podaj probowke ze skokiem (n): ")
        f = input("podaj czestotliwosc probkowania (f): ")
        return float(a), int(n1), int(ns), float(f)

    def get_params_discreet_2(self):
        a = input("podaj amplitude (A):")
        t1 = input("podaj czas poczatkowy (t1): ")
        d = input("podaj czas trwania (d): ")
        f = input("podaj czestotliwosc probkowania (f): ")
        p = input("podaj prawdopodobienstwo skoku (p): ")
        return float(a), float(t1), float(d) + float(t1), float(f), float(p)

    def show_plot(self, samples, values, str1=''):
        plt.plot(samples, values, str1)
        plt.show()
