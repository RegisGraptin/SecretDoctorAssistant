import os
import re

from secret_ai_sdk.secret import Secret
from secret_ai_sdk.secret_ai import ChatSecret


def remove_think_content(text: str) -> str:
    """
    Removes the <think> content from the input text and returns the cleaned summary.

    Parameters:
    text (str): The input text containing the <think> section and the summary.

    Returns:
    str: The cleaned text with the <think> section removed.
    """
    # Use regex to remove the <think> content
    cleaned_text = re.sub(r"<think>.*?</think>", "", text, flags=re.DOTALL)

    # Remove any leading/trailing whitespace
    cleaned_text = cleaned_text.strip()

    return cleaned_text


class SecretChat:
    def __init__(self):
        secret_client = Secret(
            chain_id="pulsar-3", node_url=os.environ["SECRET_NODE_URL"]
        )

        # Get all the models registered with the smart contracts
        models = secret_client.get_models()

        # For the chosen model you may obtain a list of LLM instance URLs to connect to
        urls = secret_client.get_urls(model=models[0])

        self.secret_ai_llm = ChatSecret(
            base_url=urls[0],
            model=models[0],
            temperature=1.0,
        )

    def invoke(self, messages: list[tuple[str, str]]) -> str:
        response = self.secret_ai_llm.invoke(messages, stream=False)
        return remove_think_content(response.content)


# app = FastAPI()


# @app.post("/chat")
# async def chat(request):
#     try:
#         secret_chat = SecretChat()
#         print(request)
#         response = secret_chat.invoke(request.message)
#         return {"response": response}
#     except Exception as e:
#         raise HTTPException(status_code=500, detail=str(e))
