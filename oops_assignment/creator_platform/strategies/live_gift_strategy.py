from strategies.earning_strategy import EarningStrategy


class LiveGiftStrategy(EarningStrategy):
    def __init__(self, gift_value):
        self._gift_value = gift_value

    def calculate(self, creator):
        return self._gift_value