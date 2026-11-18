# Building with the Claude API – Generative AI Engineering

A hands-on collection of Python projects and Jupyter notebooks exploring **Anthropic's Claude API, Large Language Models (LLMs), Prompt Engineering, Tool Calling, Retrieval-Augmented Generation (RAG), Multimodal AI, and Model Context Protocol (MCP).**

This repository documents my practical learning journey in Generative AI Engineering, focusing on building LLM-powered applications, integrating external tools, implementing retrieval pipelines, and evaluating AI-generated responses.

## 🚀 Project Overview

The goal of this repository is to understand how modern LLM-powered applications are designed and implemented using Python and different AI model providers.

The repository covers the following areas:

- Building conversational AI applications using Claude API.
- Implementing streaming responses for interactive chatbots.
- Designing and improving prompts through prompt engineering.
- Connecting LLMs with external Python functions using tool calling.
- Working with multimodal inputs such as images and PDFs.
- Implementing AI-powered text editing workflows.
- Building Retrieval-Augmented Generation (RAG) pipelines.
- Exploring embeddings, vector databases, and semantic retrieval.
- Evaluating prompt outputs and improving response quality.
- Exploring Model Context Protocol (MCP).

## ✨ Project Modules

### 1. Claude API – Chatbot Development

Learn how to integrate Anthropic's Claude API with Python to build conversational AI applications.

**Topics covered:**

- Claude API initialization.
- Sending messages using the Messages API.
- Managing conversation history.
- System prompts and model parameters.
- Tracking input and output token usage.
- Storing conversation history and response details.

**Notebook:** `Claude_ai_Chat_Bot.ipynb`

### 2. Streaming AI Responses

Explore how to stream LLM-generated responses instead of waiting for the entire response.

**Topics covered:**

- Streaming model responses.
- Handling incremental text generation.
- Improving interactive chatbot experiences.
- Understanding streaming API responses.

**Notebook:** `Claude_ai_Bot_stream_response.ipynb`

### 3. Prompt Engineering

Explore how to design effective prompts to improve LLM response quality.

**Topics covered:**

- System prompts.
- User instructions.
- Prompt structure and clarity.
- Prompt refinement.
- Controlling model behavior.
- Improving response consistency.

**Notebook:** `Prompt_engineering.ipynb`

### 4. Tool Calling

Learn how to connect LLMs with external Python functions and allow models to request tool execution.

**Topics covered:**

- Defining tool schemas.
- Function calling.
- Tool selection by LLMs.
- Executing Python functions.
- Returning tool results to the model.
- Integrating external APIs with LLM applications.

**Notebook:** `Claude_With_Tool_Calling.ipynb`

### 5. Multimodal AI – Image and PDF Support

Explore multimodal capabilities by passing images and PDF documents to AI models.

**Topics covered:**

- Image inputs.
- PDF document processing.
- Multimodal message structures.
- Extracting information from visual and document inputs.
- Building document-understanding applications.

**Notebook:** `Claude_Image_&_PDF_Support_Feature.ipynb`

### 6. AI-Powered Text Editing Tool

Explore how to build a text-editing workflow using LLMs.

**Topics covered:**

- Tool-based text editing.
- Processing user-provided text.
- Connecting model responses with editing operations.
- Building AI-assisted text workflows.

**Notebook:** `Claude_Text_Editing_Tool.ipynb`

### 7. Retrieval-Augmented Generation (RAG)

Explore how to build retrieval-based LLM applications that use external knowledge sources to generate context-aware responses.

**Topics covered:**

- Document retrieval.
- Embedding generation.
- Vector indexing.
- Semantic search.
- Similarity search.
- Custom Retriever implementation.
- Custom VectorIndex implementation.
- Pinecone vector database integration.
- Retrieval and ranking techniques.

**Notebook:** `RAG.ipynb`

### 8. Prompt Evaluation

Understand how to evaluate prompt performance and analyze LLM-generated outputs.

**Topics covered:**

- Prompt evaluation.
- Evaluating model responses.
- Comparing prompt outputs.
- Identifying response quality issues.
- Practicing prompt evaluation through exercises.

**Notebooks:**

- `prompt_eval.ipynb`
- `exercise_prompt_eval.ipynb`

### 9. Model Context Protocol (MCP)

Explore the Model Context Protocol and its role in connecting AI applications with external tools and services.

**Topics covered:**

- MCP fundamentals.
- MCP-related implementation examples.
- Tool integration and communication.

**Directory:** `MCP/`

Explore the MCP directory for individual implementation details.

## 🛠️ Technology Stack

| Technology           | Purpose                           |
| -------------------- | --------------------------------- |
| Python               | Core programming language         |
| Anthropic Claude API | LLM integration                   |
| Anthropic Python SDK | Claude API communication          |
| OpenAI Python SDK    | API-compatible model integrations |
| NVIDIA AI Endpoints  | Model and embedding integration   |
| Pinecone             | Vector database                   |
| Jupyter Notebook     | Interactive development           |
| Google Colab         | Cloud-based experimentation       |
| Python-dotenv        | Environment variable management   |
| Requests             | HTTP API communication            |

Some notebooks use additional provider-specific libraries. Refer to their individual setup cells.

## 📁 Repository Structure

```text
Building-with-the-Claude-API/
│
├── MCP/
│
├── Claude_ai_Chat_Bot.ipynb
│
├── Claude_ai_Bot_stream_response.ipynb
│
├── Claude_With_Tool_Calling.ipynb
│
├── Claude_Image_&_PDF_Support_Feature.ipynb
│
├── Claude_Text_Editing_Tool.ipynb
│
├── Prompt_engineering.ipynb
│
├── prompt_eval.ipynb
│
├── exercise_prompt_eval.ipynb
│
├── RAG.ipynb
│
└── README.md
```

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10+
- pip
- Jupyter Notebook or JupyterLab
- Google Colab (optional)
- API credentials for the services used in individual notebooks.

### 1. Clone the Repository

```bash
git clone https://github.com/chandupradeep18/Building-with-the-Claude-API.git

cd Building-with-the-Claude-API
```

### 2. Create a Virtual Environment

**Windows:**

```bash
python -m venv .venv

.venv\Scripts\activate
```

**Linux / macOS:**

```bash
python3 -m venv .venv

source .venv/bin/activate
```

### 3. Install Dependencies

Install the core dependencies:

```bash
python -m pip install --upgrade pip

pip install anthropic openai pinecone jupyter python-dotenv requests
```

Some notebooks require additional packages. Check the installation cells inside each notebook before execution.

### 4. Configure API Keys

Create a `.env` file in the project root.

```env
ANTHROPIC_API_KEY=your_anthropic_api_key
OPENAI_API_KEY=your_openai_api_key
NVIDIA_API_KEY=your_nvidia_api_key
NEBIUS_API_KEY=your_nebius_api_key
PINECONE_API_KEY=your_pinecone_api_key
```

**Important:**

- Configure only the API keys required by the notebook you are running.
- Some notebooks use Google Colab Secrets instead of environment variables.
- Follow the corresponding notebook's authentication implementation.
- Never upload API keys or `.env` files to GitHub.

Add the following to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
.ipynb_checkpoints/
```

### 5. Start Jupyter Notebook

```bash
jupyter notebook
```

Alternatively:

```bash
jupyter lab
```

Open the required notebook and execute its cells in sequence.

## 📚 Suggested Learning Path

For someone starting with LLM application development, the following sequence is recommended:

| Order | Module              | Learning Objective                    |
| ----- | ------------------- | ------------------------------------- |
| 1     | Prompt Engineering  | Understand effective prompting        |
| 2     | Claude AI Chatbot   | Build a conversational AI application |
| 3     | Streaming Responses | Implement streaming generation        |
| 4     | Tool Calling        | Connect LLMs with external functions  |
| 5     | Image & PDF Support | Explore multimodal capabilities       |
| 6     | Text Editing Tool   | Build tool-assisted AI workflows      |
| 7     | RAG                 | Understand retrieval and embeddings   |
| 8     | Prompt Evaluation   | Evaluate LLM response quality         |
| 9     | MCP                 | Explore standardized tool integration |

## 🎯 Learning Objectives

Through these implementations, I am developing practical knowledge in:

- Integrating LLM APIs with Python.
- Building conversational AI applications.
- Managing conversation context and history.
- Prompt Engineering and optimization.
- Function and Tool Calling.
- Multimodal AI applications.
- Retrieval-Augmented Generation.
- Embeddings and vector search.
- Vector database integration.
- Prompt evaluation and testing.
- Model Context Protocol.

## 🔮 Future Improvements

- Develop end-to-end RAG applications.
- Implement advanced retrieval strategies.
- Explore hybrid search and reranking.
- Integrate LangChain and LangGraph.
- Build multi-agent applications.
- Implement MCP-based AI agents.
- Add automated evaluation pipelines.
- Explore Guardrails and responsible AI.
- Build production-ready LLM applications.

## 📖 References

- [Anthropic Documentation](https://docs.anthropic.com/)
- [Anthropic API Documentation](https://docs.anthropic.com/en/api/overview)
- [Anthropic Courses – Skilljar](https://anthropic.skilljar.com/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Pinecone Documentation](https://docs.pinecone.io/)
- [Model Context Protocol](https://modelcontextprotocol.io/)
- [Jupyter Documentation](https://docs.jupyter.org/)

## 🤝 Contributions

Suggestions, improvements, and contributions are welcome.

Feel free to fork this repository, explore the implementations, and submit pull requests.

---



