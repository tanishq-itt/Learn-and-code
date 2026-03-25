from app.core.context import WorkflowContext


class Workflow:
    def __init__(self, steps):
        self.steps = steps

    def run(self, input_data):
        context = WorkflowContext()
        result = input_data

        for step in self.steps:
            result = step.execute_with_handling(context, result)

        return result, context.logs