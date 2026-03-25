from app.core.step import Step


class FailingStep(Step):
    def execute(self, context, input_data):
        raise Exception("Simulated failure")