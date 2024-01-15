# Environment setup
We first install poetry
```
curl -sSL https://install.python-poetry.org | python3.11 -
```

# Create the virtual environment
```
rm pyproject.lock
```
if the lock file exists. 

# Enter the coding environment
```
poetry shell
```
Type `poetry env info` to see where it is located. 
Type `which python` to confirm that you are running the python in the 
project environment. 

# Add langchain libraries via pip
```
pip install -U llama-cpp-python --no-cache-dir
```

# Download language models
Download the following models to my computer (found on huggingface.co)
    - codeninja-1.0-openchat-7b.Q4_K_M.gguf		
    - llama-2-7b-32k-instruct.Q4_K_M.gguf		
    - mistral-7b-instruct-v0.1.Q3_K_M.gguf		
    - zephyr-7b-beta.Q4_K_M.gguf
    - mixtral-fusion-4x7b-instruct-v0.1.Q4_K_M.gguf (you can ignore for now)