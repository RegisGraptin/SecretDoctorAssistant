
uv venv --python 3.12
source .venv/bin/activate

uvicorn src.secret.secret_chat_server:app --host 0.0.0.0 --port 8000 --reload


