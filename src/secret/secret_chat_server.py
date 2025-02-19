from fastapi import FastAPI, HTTPException
from secret_ai_sdk.secret import Secret
from secret_ai_sdk.secret_ai import ChatSecret


class SecretChat:
    def __init__(self):
        secret_client = Secret()

        # Get all the models registered with the smart contracts
        models = secret_client.get_models()

        # For the chosen model you may obtain a list of LLM instance URLs to connect to
        urls = secret_client.get_urls(model=models[0])

        self.secret_ai_llm = ChatSecret(
            base_url=urls[0],
            model=models[0],
            temperature=1.0,
        )

    def invoke(self, messages: list[tuple[str, str]]):
        response = self.secret_ai_llm.invoke(messages, stream=False)
        return response.content


app = FastAPI()


@app.post("/chat")
async def chat(request):
    try:
        secret_chat = SecretChat()
        print(request)
        response = secret_chat.invoke(request.message)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
