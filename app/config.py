import os
from anthropic import AsyncAnthropic, DefaultAioHttpClient
from dotenv import load_dotenv

load_dotenv()

anthropic_async_client = AsyncAnthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
    http_client=DefaultAioHttpClient(),
)
