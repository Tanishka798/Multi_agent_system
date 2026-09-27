# we used to use create_react_agent but now it old so we use create_agent that uses langgraph inside it

'''
output of craete agent
"messages": [
    HumanMessage(content="Find recent and reliable information on the topic: climate change. Provide titles, URLs and snippets."),
    AIMessage(content="Title: Climate Change: What You Need to Know\nURL: http....]
    ToolMessage(content="web_search: {'query': 'climate change', 'max_results': 5}")
    AIMessage(content="Title: Climate Change: What You Need to Know\nURL: http....]
    (we need last ai message so we will use [-1] while printing the output)
'''
import os

from langchain.agents import create_agent
from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_search, scrape_url
from dotenv import load_dotenv

load_dotenv()

ollama_base_url = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")

llm = ChatOllama(
    model=os.getenv("OLLAMA_MODEL", "qwen2.5-coder:3b"),
    base_url=ollama_base_url,
    temperature=0,
)

tool_llm = ChatOllama(
    model=os.getenv("OLLAMA_TOOL_MODEL", "qwen2.5:3b"),
    base_url=ollama_base_url,
    temperature=0,
)

#1st agent

def build_search_agent():
    return create_agent(model=tool_llm, tools=[web_search])

#2nd agent
def build_reader_agent():
    return create_agent(model=tool_llm, tools=[scrape_url])

#writer chain

writer_prompt = ChatPromptTemplate.from_messages([
("system", "You are an expert research writer. Write clear, structured and insightful reports."),
("human", """Write a detailed research report on the topic below.

Topic: {topic}

Research Gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list all URLs found in the research)

Be detailed, factual and professional."""),

])

writer_chain = writer_prompt | llm | StrOutputParser()

#critic chain

critic_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a sharp and constructive research critic. Be honest and specific."),
    ("human", """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this exact format:

Score: X/10

Strengths:
- ...
- ...

Areas to Improve:
- ...
- ...

One line verdict:
..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()