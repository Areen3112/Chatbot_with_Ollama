# 🤖 Chatbot with Ollama

An AI-powered chatbot built using **Ollama**, **LangChain**, and **Streamlit** that allows users to interact with Large Language Models (LLMs) running locally on their machine. This project provides a simple and intuitive web interface for private, fast, and API-free conversational AI experiences.

## 🚀 Features

* 💬 Interactive chatbot interface built with Streamlit
* 🏠 Run open-source LLMs locally using Ollama
* 🔒 Complete privacy with no external API dependency
* ⚡ Fast response generation
* 🔄 Easily switch between different Ollama-supported models
* 🎯 Simple and beginner-friendly implementation

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **LangChain**
* **Ollama**
* **Gemma 2B** (or any Ollama-supported model)



## 📂 Project Structure

```text
Chatbot_with_Ollama/
│
├── app.py                 # Main Streamlit application
├── requirements.txt       # Project dependencies
├── README.md              # Project documentation
└── .gitignore             # Ignored files and folders
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/Areen3112/Chatbot_with_Ollama.git
cd Chatbot_with_Ollama
```

### 2. Create and activate a virtual environment

**macOS/Linux**

```bash
python -m venv venv
source venv/bin/activate
```

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Install Ollama

Download and install Ollama from:

https://ollama.com/download

### 5. Pull the required model

```bash
ollama pull gemma:2b
```

You can replace `gemma:2b` with any Ollama-supported model such as:

* `llama3`
* `mistral`
* `phi3`
* `gemma`

### 6. Run the Streamlit application

```bash
streamlit run app.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

## 🎯 How It Works

1. Users enter their queries through the Streamlit interface.
2. LangChain manages the interaction with the LLM.
3. Ollama processes the request using a locally hosted model.
4. The generated response is displayed back to the user.

## 📈 Future Improvements

* [ ] Conversation memory support
* [ ] Multiple model selection
* [ ] Chat history persistence
* [ ] Document Question Answering using RAG
* [ ] Voice input and output
* [ ] Docker containerization
* [ ] Deployment support

## 🤝 Contributing

Contributions are welcome. Feel free to fork this repository and submit pull requests for improvements.

## 📄 License

This project is licensed under the MIT License.

## 👨‍💻 Author

**Areen Joshi**

* GitHub: https://github.com/Areen3112

If you found this project helpful, consider giving it a ⭐ on GitHub!
