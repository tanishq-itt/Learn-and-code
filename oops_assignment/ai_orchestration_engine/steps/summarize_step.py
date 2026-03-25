from app.core.step import Step


class SummarizeStep(Step):
    def execute(self, context, input_data):
        return f"Summary of: {input_data}"