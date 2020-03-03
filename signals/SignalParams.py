
class SignalParams:
    n = 100     # czestosc probkowania

    def get_params(self):
        a = input("podaj amplitude (A):")
        t = input("podaj okres (T): ")
        t1 = input("podaj czas poczatkowy (t1): ")
        d = input("podaj czas trwania (d): ")
        return float(a), float(t), float(t1), float(d), self.n
