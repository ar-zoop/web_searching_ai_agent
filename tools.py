from langchain_community.tools import DuckDuckGoSearchRun
from langchain.tools import tool

@tool("search_web", description="Search the web for information")
def search_web(query: str) -> str:
    ddg = DuckDuckGoSearchRun()
    return ddg.run(query)