from langchain.tools import Tool
import requests

def weather_tool_func(city_query: str) -> str:
    response = requests.post("http://localhost:8001/retrieve", json={"input": city_query})
    return response.json()["documents"][0]["page_content"]

weather_tool = Tool.from_function(
    name="get_weather_info",
    func=weather_tool_func,
    description="Use this tool to get current weather for a city. Input should mention the city name."
)
