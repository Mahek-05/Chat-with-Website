# Chat with Website

## Overview
The "Chat with Website" project is designed to facilitate interaction with a website through a chat interface. This Python-based project allows users to interact with a website and retrieve information dynamically.

## Features
- **User-Friendly Interface**: Chat with the website using a simple and intuitive chat interface.
- **Website Interaction**: The chatbot uses the latest version of LangChain to interact with and extract information from various websites.
- **Large Language Model Integration**: Compatibility with models like GPT-4, Mistral, Llama2, and ollama. In this code I am using GPT-4, but you can change it to any other model.
- **Streamlit GUI**: A clean and intuitive user interface built with Streamlit, making it accessible for users with varying levels of technical expertise.
- **Python-based**: Entirely coded in Python.

## Explanation of how the website works
The app.py file implements a web-based chat interface using Streamlit, allowing users to interact with a website by entering its URL. The core functionality is powered by Langchain and OpenAI. Here’s a brief explanation of how it works:

- **Document Loading:** The website content is fetched and split into smaller text chunks.
- **Vector Store Creation:** These chunks are embedded into a vector store using OpenAI embeddings.
- **Retrieval-Augmented Generation (RAG):** The user's queries are processed, and relevant information is retrieved and combined with the chat history to generate accurate responses.
- **Interactive Chat:** The conversation is maintained and displayed, enabling a dynamic and contextual interaction with the website.

## Concepts Used
- **Retrieval-Augmented Generation (RAG)**
RAG combines large language models (LLMs) with a retrieval mechanism to generate accurate and context-aware responses by pulling in relevant information from external data sources during the generation process.

- **Large Language Model (LLM)**
LLMs are AI models trained on vast amounts of text data, enabling them to generate and understand human-like text, making them useful in natural language processing tasks.

- **Langchain**
Langchain is a framework designed to simplify the development of applications that use LLMs by providing tools for chaining together different components like prompts, retrievers, and generators.

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/Mahek-05/Chat-with-Website.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Chat-with-Website
    ```
3. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

Create your own .env file with the following variables:

```bash
OPENAI_API_KEY=[your-openai-api-key]
```

## Usage
To run the Streamlit app:

```bash
streamlit run app.py
```

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

This `README.md` provides an overview, installation instructions, and other essential details about this project.

- [@Mahek-05](https://github.com/Mahek-05)