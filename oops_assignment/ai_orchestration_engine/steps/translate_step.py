from app.core.step import Step


class TranslateStep(Step):
    def execute(self, context, input_data):
        return f"Translated: {input_data}"