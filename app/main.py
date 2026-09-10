import asyncio
import json
from app.config import anthropic_async_client as async_client
from app.constants import CLASSIFIER_MODEL, CLASSIFIER_OUTPUT_MAX_TOKENS, SYSTEM_CLASSIFIER_PROMPT
from app.enums import ClaudeMessageRoleEnum
from app.schema import ClassifierResult


async def classify(ticket_text: str) -> ClassifierResult | None:

    response = await async_client.messages.parse(
        max_tokens=CLASSIFIER_OUTPUT_MAX_TOKENS,
        system=SYSTEM_CLASSIFIER_PROMPT,
        messages=[
            {
                "role": ClaudeMessageRoleEnum.user,
                "content": ticket_text,
            }
        ],
        model=CLASSIFIER_MODEL,
        output_format=ClassifierResult,
    )

    return response.parsed_output


async def main():
    with open("data/synthetic_tickets.json", "r") as file:
        data = json.load(file)
    a = await classify(data["tickets"][0]["text"])
    b = 1


if __name__ == "__main__":
    asyncio.run(main())
