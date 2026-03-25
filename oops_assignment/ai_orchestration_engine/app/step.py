from abc import ABC, abstractmethod


class Step(ABC):
    def __init__(self, name, retry=0, fallback=None, condition=None):
        self.name = name
        self.retry = retry
        self.fallback = fallback
        self.condition = condition

    def should_run(self, context, input_data):
        if self.condition:
            return self.condition(context, input_data)
        return True

    def execute_with_handling(self, context, input_data):
        if not self.should_run(context, input_data):
            context.log(f"[SKIPPED] {self.name}")
            return input_data

        attempts = 0

        while attempts <= self.retry:
            try:
                context.log(f"[START] {self.name}")
                result = self.execute(context, input_data)
                context.log(f"[SUCCESS] {self.name}")
                return result

            except Exception as e:
                attempts += 1
                context.log(f"[ERROR] {self.name}: {str(e)} (Attempt {attempts})")

                if attempts > self.retry:
                    if self.fallback:
                        context.log(f"[FALLBACK] {self.name}")
                        return self.fallback.execute_with_handling(context, input_data)
                    raise e

    @abstractmethod
    def execute(self, context, input_data):
        pass