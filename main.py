from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.agents import create_agent
from langchain_core.messages import SystemMessage
import os
from tools import search_web

load_dotenv()

# Initialize LLM
llm = ChatOpenAI(
    model="deepseek-chat",
    api_key=os.environ.get('OPENAI_API_KEY'),
    base_url="https://api.deepseek.com"
)

# Create system message
system_prompt = SystemMessage(
    content="You are a research assistant that helps users gather information on a given topic using various tools. "
    "You must always provide a summary, sources, and tools used in your response. "
    "Use the following format:\n"
    "Topic: <topic>\n"
    "Summary: <summary>\n"
    "Sources: <list of sources>\n"
    "Tools Used: <list of tools used>\n"
)

tools = [search_web]

# Create agent
agent = create_agent(
    model=llm,
    tools=tools,
    system_prompt=system_prompt
)

# Invoke agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "Tell me about arzoo bapna working at american express."}]}
)

# Extract and parse AI message content
ai_content = result['messages'][-1].content


print(ai_content)
