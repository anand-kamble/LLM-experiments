## Ollama

To install Ollama on Linux (In my case it is `wsl`) you need to run following command

```
curl https://ollama.ai/install.sh | sh
```

After installing Ollama, you can start the Ollama server by 

```
ollama serve
```

To run Llama2, you need to run following command in a new terminal.

```
ollama run llama2
```

Also, you can run the python script in this folder to test the chat functionality with ollama.