from anthropic.types import RefusalStopDetails


class MaxTokenReachException(Exception):
    def __init__(self, max_token: int) -> None:
        super().__init__(f"Max Token Exception. Value is {max_token}")


class AIRefusalException(Exception):
    def __init__(self, stop_details: RefusalStopDetails | None) -> None:
        category = stop_details and stop_details.category
        explanation = stop_details and stop_details.explanation
        message = "Refusal Response Exception."

        if category and explanation:
            message += f" {category}: {explanation}"

        super().__init__(message)
