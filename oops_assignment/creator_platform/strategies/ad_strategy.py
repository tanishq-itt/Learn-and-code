from strategies.earning_strategy import EarningStrategy


class AdStrategy(EarningStrategy):
    def calculate(self, creator):
        return creator.views * 0.05