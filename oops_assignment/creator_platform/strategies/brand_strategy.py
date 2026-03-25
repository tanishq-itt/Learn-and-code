from strategies.earning_strategy import EarningStrategy


class BrandStrategy(EarningStrategy):
    def calculate(self, creator):
        return creator.base_amount