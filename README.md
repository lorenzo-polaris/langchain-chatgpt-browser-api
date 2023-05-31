# Langchain LLM

[![PyPI version](https://badge.fury.io/py/langchain-llm.svg)](https://badge.fury.io/py/langchain-llm)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description

Langchain ChatGPT Browser API is a Langchain implementation of [ChatGPT-Web-API](https://github.com/lorenzo-polaris/ChatGPT-Web-API). It allows you to use the ChatGPT instance in your browser in a Langchain project.

With a Plus subscription, you can take advantage of GPT4 without the need for an API key.

## Installation

You can install ChatGPT Browser API via pip. Run the following command to install it:

```
pip install langchain-chatgpt-browser-api
```

Ensure that you have Python 3.6 or a higher version installed on your system.

## Usage

Once installed, you can import ChatGPT Browser API. Here's a basic example to get you started:

```python
from ChatGPTBrowserAPI import BrowserChatGPT

# Create an instance of LangchainLLM
llm = BrowserChatGPT(chatgpt_web_api_url="http://localhost:3001")

answer = chatgpt("Write your prompt here")

print(answer)
```

To start the web server located at chatgpt_web_api_url, see [ChatGPT-Web-API](https://github.com/lorenzo-polaris/ChatGPT-Web-API)

## Contributing

Contributions are welcome! If you have any ideas, bug reports, or feature requests, please open an issue or submit a pull request on GitHub.

## License

This library is licensed under the MIT License. See the LICENSE file for more information.
