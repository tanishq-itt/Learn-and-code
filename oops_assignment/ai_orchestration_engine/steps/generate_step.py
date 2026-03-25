from app.core.step import Step


class GenerateStep(Step):
    def execute(self, context, input_data):
        return f"Generated: {input_data}"