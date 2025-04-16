from langchain.tools import Tool
import requests

def file_tool_func(folder_query: str) -> str:
    response = requests.post("http://localhost:8002/retrieve", json={"input": folder_query})
    return response.json()["documents"][0]["page_content"]

file_tool = Tool.from_function(
    name="list_files_in_folder",
    func=file_tool_func,
    description="Use this tool to list files in a folder. Input should mention folder name."
)
