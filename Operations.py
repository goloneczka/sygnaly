from Signal import Signal


class Operations:

    @staticmethod
    def check_amount_samples(signal_1, signal_2):
        return len(signal_1.samples) == len(signal_2.samples)

    @staticmethod
    def check_samples(signal_1, signal_2):
        return signal_1.samples[0] == signal_2.samples[0] and signal_1.samples[-1] == signal_2.samples[-1]

    @staticmethod
    def return_tag_signal(signal_1, values):
        if signal_1.tag == 'discreet':
            return Signal(signal_1.samples, values, 'discreet')
        else:
            return Signal(signal_1.samples, values, 'casual')

    def add(self, signal_1, signal_2):
        if not self.check_samples(signal_1, signal_2) or not self.check_amount_samples(signal_1, signal_2):
            raise Exception("niezgodnosc zakresow !")

        values = []
        for y1, y2 in zip(signal_1.values, signal_2.values):
            values.append(y1 + y2)

        return self.return_tag_signal(signal_1, values)

    def sub(self, signal_1, signal_2):
        if not self.check_samples(signal_1, signal_2) or not self.check_amount_samples(signal_1, signal_2):
            raise Exception("niezgodnosc zakresow !")

        values = []
        for y1, y2 in zip(signal_1.values, signal_2.values):
            values.append(y1 - y2)

        return self.return_tag_signal(signal_1, values)

    def mult(self, signal_1, signal_2):
        if not self.check_samples(signal_1, signal_2) or not self.check_amount_samples(signal_1, signal_2):
            raise Exception("niezgodnosc zakresow !")

        values = []
        for y1, y2 in zip(signal_1.values, signal_2.values):
            values.append(y1 * y2)

        return self.return_tag_signal(signal_1, values)

    def div(self, signal_1, signal_2):
        if not self.check_samples(signal_1, signal_2) or not self.check_amount_samples(signal_1, signal_2):
            raise Exception("niezgodnosc zakresow !")

        values = []
        for y1, y2 in zip(signal_1.values, signal_2.values):
            if y2 != 0 and y1 != 0:
                values.append(y1 / y2)
            else:
                values.append(0)

        return self.return_tag_signal(signal_1, values)
