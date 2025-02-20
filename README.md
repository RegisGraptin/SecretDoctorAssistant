
uv venv --python 3.12
source .venv/bin/activate


uv pip install 'secret-sdk>=1.8.1' --prerelease=allow
uv pip install secret-ai-sdk
uv pip install python-dotenv
uv pip install streamlit

streamlit run src/main.py
