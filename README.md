# 🔎 Multi-Agent Research System

An LLM-powered research application that automates web research, content extraction, report generation, and report evaluation through a coordinated multi-stage AI workflow.

## 📌 Overview

Researching a topic manually often requires searching multiple websites, reading relevant sources, organizing information, and evaluating the quality of the final report.

This project automates these steps using multiple AI agents and LLM chains. Given a research topic, the system searches the web, extracts information from a relevant webpage, generates a structured research report, and evaluates the report using a dedicated critic chain.

The application provides an interactive Streamlit interface for running the workflow and reviewing each stage's output.

## ✨ Features

* **Web Search Agent:** Uses Tavily Search to find recent information, source URLs, titles, and snippets.
* **Reader Agent:** Selects a relevant URL from the search results and extracts webpage content using a scraping tool.
* **Research Writer:** Uses an LLM chain to generate a structured report with an introduction, key findings, conclusion, and sources.
* **Critic Chain:** Evaluates the generated report and provides a score, strengths, areas for improvement, and a verdict.
* **Interactive Dashboard:** Displays the final report, critic review, search results, and scraped content in separate tabs.
* **Report Export:** Allows users to download the generated research report as a Markdown file.

## 🏗️ System Architecture

```text
             User enters a topic
                     |
                     v
             Streamlit Interface
                     |
                     v
              Search Agent
                     |
              Tavily Web Search
                     |
                     v
              Reader Agent
                     |
             URL Scraping Tool
                     |
                     v
               Writer Chain
                     |
              Research Report
                     |
                     v
               Critic Chain
                     |
                     v
             Final Evaluation
                     |
                     v
              Streamlit Tabs
```

## ⚙️ Workflow

### 1. Search Agent

The Search Agent uses Tavily to retrieve up to five web search results related to the user's topic. It returns titles, URLs, and content snippets to help identify relevant sources.

### 2. Reader Agent

The Reader Agent receives the search results and is instructed to select a relevant URL. The scraping tool uses `requests` and `BeautifulSoup` to extract readable webpage text while removing elements such as scripts, styles, navigation, and footers.

### 3. Writer Chain

The Writer Chain combines the search results and extracted webpage content. Using the configured language model, it generates a structured research report containing:

* Introduction
* Key Findings
* Conclusion
* Sources

### 4. Critic Chain

The Critic Chain reviews the generated report and returns a score out of 10, strengths, areas for improvement, and a one-line verdict.

### 5. Results and Export

The Streamlit interface presents the report, evaluation, raw search results, and scraped content in separate tabs. Users can also download the report in Markdown format.

## 🛠️ Tech Stack

| Technology        | Purpose                                                   |
| ----------------- | --------------------------------------------------------- |
| Python            | Core application logic                                    |
| Streamlit         | Interactive user interface                                |
| LangChain         | Agent creation and LLM chains                             |
| LangChain Agents  | Tool-enabled search and reader agents                     |
| Mistral AI        | Language model for agents, report writing, and evaluation |
| Tavily Search API | Web search                                                |
| Requests          | Fetch webpage content                                     |
| BeautifulSoup     | HTML parsing and text extraction                          |
| python-dotenv     | Environment variable management                           |

## 📂 Project Structure

```text
Multi_Agent_System/
│
├── app.py             # Streamlit application
├── agents.py          # Search agent, reader agent, writer and critic chains
├── tools.py           # Web search and webpage scraping tools
├── pipeline.py        # Orchestrates the complete research workflow
├── requirements.txt   # Python dependencies
├── .env               # API keys (not committed to GitHub)
├── .gitignore
└── README.md
```

## 🚀 Getting Started

### Prerequisites

* Python 3.10 or a compatible version
* A Mistral AI API key
* A Tavily API key
* Git

### 1. Clone the repository

```bash
git clone https://github.com/Tanishka798/Multi_agent_system.git
cd Multi_agent_system
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it on Windows PowerShell:

```powershell
.\venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key
MISTRAL_API_KEY=your_mistral_api_key
```

Replace the placeholders with your actual API keys. Never commit the `.env` file to GitHub.

### 5. Run the application

```bash
streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## 🔐 Security

* Store API keys in environment variables.
* Keep `.env` excluded from version control.
* Never expose API keys in source code, screenshots, or public repositories.

## 🔮 Future Improvements

* Scrape and synthesize information from multiple relevant sources.
* Add source validation and citation verification.
* Introduce structured workflow state and improved error handling.
* Add retries and timeout handling for external APIs.
* Evaluate report factuality and source relevance.
* Deploy the application for public access.

## 👩‍💻 Author

**Tanishka Gupta**

[GitHub Profile](https://github.com/Tanishka798)

---

*Built to explore LLM-powered agents, tool calling, workflow orchestration, and automated research using Generative AI.*
