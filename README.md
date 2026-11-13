[# Building-with-the-Claude-API
Leaning Building With Claude Api From Anthropic SkillJar
](https://github.com/chandupradeep18/Building-with-the-Claude-API
Building-with-the-Claude-API — Repository analysis

Repository: chandupradeep18/Building-with-the-Claude-API
10 Jupyter notebooks + MCP folder

This repository is a practical learning portfolio based on Anthropic's Claude API and Skilljar learning materials.

Unlike your Pandas repository, this one focuses on LLM application development and Generative AI engineering.
Topics identified

Area
	

Topics

Claude API
	

Chatbot development and streaming responses

Prompt Engineering
	

Prompt design and evaluation

Tool Calling
	

Connecting Claude with external functions

RAG
	

Retrieval-Augmented Generation

Multimodal AI
	

Image and PDF support

AI Tools
	

Text editing tools

MCP
	

Model Context Protocol

The repository contains notebooks for these topics, plus an MCP folder. 
GitHub
New README file

README_Claude_API.md
GitHub-ready Markdown documentation
Ready

Download the new README.md
My recommendations

A few improvements I recommend for this repository:

    Add a requirements.txt with verified dependencies.

    Separate MCP examples into individual folders.

    Add practical projects demonstrating Claude API integrations.

    Include prompt evaluation examples and test cases.

    Add screenshots or sample outputs for chatbot and RAG applications.

Important: I inspected the repository file listing and selected notebook source, but did not execute all notebooks. The README describes the available material without claiming that every example has been tested.

You can replace the existing GitHub README with this file. I haven't made changes to the remote repository.
README_Claude_API.mdDocument
Building with the Claude API

A hands-on collection of Python notebooks exploring how to build
applications with Anthropic's Claude API and related LLM
application-development concepts.

This repository covers prompt engineering, chatbot development,
streaming responses, tool calling, Retrieval-Augmented Generation (RAG),
multimodal inputs, text-editing tools, prompt evaluation, and Model
Context Protocol (MCP).

The notebooks are intended for learning and experimentation. Some
examples also demonstrate OpenAI-compatible clients and other model
providers alongside Claude.
Repository Contents
1. Claude API Fundamentals and Applications

Notebook / Folder Description

Claude AI Chatbot Build a conversational chatbot
using an LLM API.

Claude AI Bot --- Streaming Explore streaming model responses Response for an interactive chat experience.

Claude with Tool Define tools, provide tool schemas, Calling and connect model responses to
Python functions. The notebook also
demonstrates working with multiple
API-compatible providers.

Claude Image & PDF Experiment with image and PDF Support inputs in a model-powered
application.
Claude Text Editing Explore a text-editing tool Tool workflow.
2. Prompt Engineering and Evaluation

Notebook Description

Prompt Practice writing and improving Engineering prompts for LLM applications.

Prompt Evaluation Explore evaluating prompt outputs.
Prompt Evaluation Practice prompt evaluation through Exercises exercises.
3. Retrieval-Augmented Generation (RAG)

Notebook Description

RAG Explore a retrieval pipeline,
embeddings, vector search, and
retrieval techniques. The notebook
includes custom retrieval/index
abstractions and a Pinecone
integration.
4. Model Context Protocol (MCP)

Folder Description

MCP MCP-related learning materials and
examples. Browse the folder for its
available files.
Concepts and Skills Practiced

    Calling LLM APIs from Python
    Building conversational applications
    Streaming model responses
    Prompt engineering and prompt evaluation
    Tool/function calling and tool schemas
    Connecting model outputs to Python functions
    Working with image and PDF inputs
    Building text-editing workflows
    RAG fundamentals and retrieval pipelines
    Embeddings and vector search
    Vector database integration with Pinecone
    Exploring MCP concepts

Technology Stack

    Python --- application development
    Anthropic Python SDK --- Claude API integration
    OpenAI Python SDK --- OpenAI-compatible API clients used in some
    examples
    Pinecone --- vector database integration in the RAG notebook
    Jupyter Notebook / Google Colab --- interactive development
    HTTP clients and Python standard library --- supporting API and
    utility code

Individual notebooks may use additional packages. Check the installation
cells at the beginning of each notebook before running it.
Getting Started
Prerequisites

    Python 3.10 or later is recommended.
    pip
    Jupyter Notebook or JupyterLab, or a Google Colab account
    API credentials for the provider used by the notebook

1. Clone the repository
git clone https://github.com/chandupradeep18/Building-with-the-Claude-API.git
cd Building-with-the-Claude-API
2. Create a virtual environment (recommended)

Windows PowerShell:
python -m venv .venv
.\.venv\Scripts\Activate.ps1

Windows Command Prompt:
python -m venv .venv
.venv\Scripts\activate.bat

Linux / macOS:
python3 -m venv .venv
source .venv/bin/activate
3. Install the core packages
python -m pip install --upgrade pip
pip install anthropic openai pinecone jupyter python-dotenv requests

Some notebooks may require extra libraries. Install those as indicated
in the notebook's own setup cells.
4. Configure API credentials

The examples use API credentials for services such as Anthropic, NVIDIA,
Nebius, Ollama, and Pinecone. You only need credentials for the
providers and services used by the notebook you are running.

For local development, create a .env file in the project directory:
ANTHROPIC_API_KEY=your_anthropic_api_key
OPENAI_API_KEY=your_openai_api_key
NVIDIA_API_KEY=your_nvidia_api_key
NEBIUS_API_KEY=your_nebius_api_key
PINECONE_API_KEY=your_pinecone_api_key

Load only the variables you need in your Python code. Adapt the variable
names to the notebook's implementation.

For Google Colab notebooks, configure secrets through Colab's Secrets
panel when the notebook uses google.colab.userdata.

Security: Never commit API keys, .env files, access tokens, or
other credentials to GitHub. Add .env to .gitignore.
5. Run the notebooks

Start Jupyter:
jupyter notebook

Or use JupyterLab:
jupyter lab

You can also open the notebooks in Google Colab using the links below.
Suggested Learning Path

If you are new to building LLM applications, follow this sequence:

    Prompt Engineering --- understand how prompts influence model
    outputs.
    Claude AI Chatbot --- make your first conversational
    application.
    Streaming Response --- learn how to stream generated output.
    Tool Calling --- connect an LLM to Python functions and external
    tools.
    Image & PDF Support --- experiment with multimodal inputs.
    Text Editing Tool --- explore tool-assisted text workflows.
    RAG --- learn retrieval, embeddings, and vector search.
    Prompt Evaluation --- evaluate and improve prompt quality.
    MCP --- explore the MCP examples in the repository.

Open Notebooks in Google Colab

Notebook Open

Claude AI Chatbot Open in Colab

Streaming Response Open in Colab

Tool Calling Open in Colab

Image & PDF Support Open in
Colab

Text Editing Tool Open in Colab

Prompt Engineering Open in Colab

Prompt Evaluation Open in Colab

Prompt Evaluation Exercises Open in Colab
RAG Open in Colab
Important Notes

    API access may require a paid account, credits, or provider-specific
    setup.
    Model names and API endpoints can change. Check the relevant
    provider's documentation if an example stops working.
    The notebooks include provider-specific configuration. Do not assume
    every notebook requires every API key listed above.
    The repository is a learning collection; review each notebook's code
    and dependencies before running it.
    No license information was visible in the repository at the time
    this README was prepared. Add a license file if you intend to
    specify reuse and distribution terms.

Contributing

Suggestions, fixes, and learning improvements are welcome. Fork the
repository, create a branch for your changes, and submit a pull request.

If this repository helps you learn about Claude API and LLM application
development, consider giving it a ⭐.


)
