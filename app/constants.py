import os

with open("prompts/system_classifier_prompt.txt", "r", encoding="utf-8") as prompt_file:
    SYSTEM_CLASSIFIER_PROMPT = prompt_file.read()


CLASSIFIER_MODEL = os.getenv("CLASSIFIER_MODEL", "claude-haiku-4-5-20251001")
CLASSIFIER_OUTPUT_MAX_TOKENS = 1024
