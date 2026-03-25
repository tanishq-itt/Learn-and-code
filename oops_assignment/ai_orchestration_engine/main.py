from app.workflow.workflow import Workflow
from app.steps.generate_step import GenerateStep
from app.steps.summarize_step import SummarizeStep
from app.steps.translate_step import TranslateStep
from app.steps.failing_step import FailingStep


def main():
    fallback = SummarizeStep("Fallback Summarize")

    workflow = Workflow([
        GenerateStep("Generate Content"),

        FailingStep(
            "Failing Step",
            retry=1,
            fallback=fallback
        ),

        TranslateStep(
            "Translate Step",
            condition=lambda ctx, data: "Generated" in data
        )
    ])

    output, logs = workflow.run("Product description")

    print("\nFinal Output:")
    print(output)


if __name__ == "__main__":
    main()