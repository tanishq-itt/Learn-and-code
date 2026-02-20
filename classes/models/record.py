class Record:
    def __init__(self, record_id: str, name: str, value: float, date: str = None):
        self.id = record_id
        self.name = name
        self.value = value
        self.date = date
        self.doubled_value = None
        self.squared_value = None

    def transform(self, date_format: str):
        self.name = self.name.upper()

        if self.date:
            from datetime import datetime
            try:
                parsed_date = datetime.strptime(self.date, "%Y-%m-%d")
                self.date = parsed_date.strftime(date_format)
            except ValueError:
                pass

        self.doubled_value = self.value * 2
        self.squared_value = self.value ** 2

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "value": self.value,
            "date": self.date,
            "doubled_value": self.doubled_value,
            "squared_value": self.squared_value
        }