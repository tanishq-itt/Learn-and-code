from strategies.earning_strategy import EarningStrategy


class SubscriptionStrategy(EarningStrategy):
    def calculate(self, creator):
        return creator.subscribers * 2