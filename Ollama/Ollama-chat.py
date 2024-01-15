import requests
import os
import asyncio
import json
import time

OLLAMA_SERVER_URL = "http://localhost:11434/api/chat"
MODEL = "llama2"
CHAT_JSON_FILENAME = "chat.json"


class OLLAMA_CHAT():
    """
    Class representing an Ollama chat client.

    Attributes:
    - chat (dict): Dictionary containing information about the chat.
                   Initialized with default values for the Ollama chat.
    """
    chat = {
        "model": MODEL,
        "messages": [],
        "stream": False
    }

    def __init__(self):
        """
        Initializes the OLLAMA_CHAT instance.

        Attempts to connect to the Ollama server.
        """
        try:
            response = requests.get(OLLAMA_SERVER_URL)
        except:
            print(
                f"Cannot connect to OLLAMA server \nPlease ensure that server is running at: {OLLAMA_SERVER_URL}")
            self.exit()

    def load_chat(self):
        """
        Loads the chat history from a JSON file.

        If a previous chat history exists and was generated with the same model,
        it updates the 'chat' attribute with the loaded chat.
        """
        try:
            with open(CHAT_JSON_FILENAME, 'r') as chat_file:
                previous_chat = json.loads(chat_file.read())
                if (previous_chat["model"] == MODEL):
                    self.chat = previous_chat
                else:
                    print(
                        "Previous chat was generated with different model, continuing without chat history.")
        except:
            print("Error loading chat, continuing without chat history.")
        return self

    async def chat_request(self):
        """
        Handles user input for the Ollama chat.

        Reads user input, processes special commands, sends requests to the Ollama server,
        and prints the server response.
        """
        chat_input = input(">  ").strip()
        if chat_input == "/bye":
            self.exit()
        elif chat_input == "/save":
            with open(CHAT_JSON_FILENAME, 'w') as chat_file:
                json.dump(self.chat, chat_file, indent=2)
            await self.chat_request()
        else:
            self.chat['messages'].append({
                "role": "user",
                "content": chat_input
            })
            # TODO: Fix the printing of loader.
            # loader = asyncio.create_task(self.print_loader())
            res = await self.send_request()
            # loader.close()
            self.chat['messages'].append(res['message'])
            print(f">> {res['message']['content']}")
            await self.chat_request()

    async def send_request(self):
        """
        Sends a chat request to the Ollama server and returns the server response.
        """
        response = requests.post(
            OLLAMA_SERVER_URL, json=self.chat)
        return response.json()

    async def print_loader(self):
        """
        Prints a loading animation while waiting for the Ollama server response.
        """
        print("\nLoading")
        try:
            while True:
                for char in '|/-\\':
                    print('\r', char, end='', flush=True)
                    time.sleep(0.1)
        except KeyboardInterrupt:
            pass

    def exit(self):
        print("Exiting Ollama chat ...")
        os._exit(0)

    def init(self):
        """
        Initializes the Ollama chat.

        Displays available commands and starts the chat interaction loop.
        """
        print("You can use following commands in chat\n /save : to save the chat to json file.\n /bye : to exit Ollama Chat.\n")
        print(f"Write a Message for {MODEL} ")
        asyncio.run(self.chat_request())


if __name__ == '__main__':
    ollama = OLLAMA_CHAT()
    ollama.load_chat().init()
