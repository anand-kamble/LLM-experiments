# Ollama Chat Client

The Ollama Chat Client is a Python-based chat application that interacts with the Ollama server to generate responses based on a specified language model. This README file provides an overview of the chat client, its features, and instructions on how to use it.

## Ollama

### Installation

To install Ollama on Linux (e.g., in WSL), run the following command:

```bash
curl https://ollama.ai/install.sh | sh
```

### Starting the Ollama Server

After installing Ollama, start the Ollama server by executing the following command:

```bash
ollama serve
```

### Running Llama2

To run Llama2, execute the following command in a new terminal:

```bash
ollama run llama2
```

## Requirements

Using a virtual environment, such as Poetry, is recommended for managing dependencies.

### Using Poetry (Recommended)

1. Install Poetry by following the instructions [here](https://python-poetry.org/docs/#installation).

2. Navigate to the root directory of this git repository.

3. Run the following command to install dependencies:

   ```bash
   poetry install
   ```

4. Activate the virtual environment:

   ```bash
   poetry shell
   ```

### Without Poetry

Before using the Ollama Chat Client, ensure that you have the following dependencies installed:

- Python 3
- Requests library (`pip install requests`)

## Usage

1. Open a terminal and navigate to the directory containing the `ollama_chat.py` file.

2. Run the chat client by executing the following command:

   ```bash
   python ollama_chat.py
   ```

3. Follow the on-screen instructions to interact with the Ollama chat.

## Commands

The Ollama Chat Client supports the following commands:

- `/save`: Save the chat history to a JSON file (`chat.json`).
- `/bye`: Exit the Ollama chat.

## Saving Chat History

To save the chat history, use the `/save` command. The chat history will be stored in a JSON file named `chat.json`. This file can be used to load the chat history in future sessions.

## Exiting the Chat

To exit the Ollama chat, use the `/bye` command. This will gracefully terminate the chat client.

**Note**: Ensure that the Ollama server is running at the specified URL (`http://localhost:11434/api/chat`) before starting the chat client.

Feel free to explore and modify the code to suit your needs or integrate it into other projects.