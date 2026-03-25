class Creator:
    def __init__(self, name, views=0, subscribers=0, base_amount=0):
        self._name = name
        self._views = views
        self._subscribers = subscribers
        self._base_amount = base_amount
        self._strategies = []

    @property
    def views(self):
        return self._views

    @property
    def subscribers(self):
        return self._subscribers

    @property
    def base_amount(self):
        return self._base_amount

    def add_strategy(self, strategy):
        self._strategies.append(strategy)

    def calculate_earnings(self):
        return sum(strategy.calculate(self) for strategy in self._strategies)

    def display(self):
        print(f"Creator: {self._name}, Earnings: ${self.calculate_earnings()}")