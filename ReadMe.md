# Environment Setup

## Install Poetry
Ensure you have Poetry installed by running the following command:

```bash
curl -sSL https://install.python-poetry.org | python3.11 -
```

## Create Virtual Environment
If a `pyproject.lock` file exists, remove it with the following command:

```bash
rm pyproject.lock
```

Enter the coding environment using Poetry:

```bash
poetry shell
```

To check the environment details, run:

```bash
poetry env info
```

Confirm that you are running the correct Python version in the project environment:

```bash
which python
```

## Install Langchain Libraries
Add Langchain libraries via pip:

```bash
pip install -U llama-cpp-python --no-cache-dir
```

# Download Language Models

Download the following language models from huggingface.co and save them to your computer:

- [codeninja-1.0-openchat-7b.Q4_K_M.gguf](model_link_1)
- [llama-2-7b-32k-instruct.Q4_K_M.gguf](model_link_2)
- [mistral-7b-instruct-v0.1.Q3_K_M.gguf](model_link_3)
- [zephyr-7b-beta.Q4_K_M.gguf](model_link_4)
- [mixtral-fusion-4x7b-instruct-v0.1.Q4_K_M.gguf](model_link_5) (optional)

Replace `model_link_X` with the actual download links.

Feel free to ignore the last model (`mixtral-fusion-4x7b-instruct-v0.1.Q4_K_M.gguf`) for now if not needed.