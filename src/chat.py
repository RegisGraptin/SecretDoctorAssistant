from dotenv import load_dotenv

from secret.secret_chat_server import SecretChat

load_dotenv()

s = SecretChat()

messages = [
    ("system", "You are my therapist. Help me with my issues."),
    ("human", "I miss my cat."),
]

res = s.invoke(messages)

print(res)
