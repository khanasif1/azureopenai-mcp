from langchain_openai import AzureChatOpenAI
from langchain.agents import initialize_agent, AgentType
from tools.weather_tool import weather_tool
from tools.file_tool import file_tool
import chainlit as cl
from dotenv import load_dotenv


load_dotenv()

@cl.on_chat_start
async def on_chat_start():
    llm = AzureChatOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY")
        azure_deployment="gpt-4o",    
        azure_endpoint=os.getenv(AZURE_OPENAI_ENDPOINT) #"https://ai-hub-demo-basemodel.openai.azure.com/",
        api_version="2024-06-01",
        temperature=0
    )

    tools = [weather_tool, file_tool]
    agent = initialize_agent(
        tools=tools,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
        llm=llm,
        verbose=True
    )

    cl.user_session.set("agent", agent)
    await cl.Message("🔍 Ask about weather or folders, and I'll decide the right tool!").send()

@cl.on_message
async def on_message(msg: cl.Message):
    agent = cl.user_session.get("agent")
    print(f"agent {agent}")
    print(f"content {msg.content}")
    response = agent.invoke(msg.content)    
    print(f"response {response}")
    await cl.Message(response).send()
