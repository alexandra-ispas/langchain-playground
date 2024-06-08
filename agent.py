from dotenv import load_dotenv
load_dotenv()
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import create_openai_functions_agent, AgentExecutor
from langchain_community.tools.tavily_search import TavilySearchResults

model = ChatOpenAI(
    model="gpt-3.5-turbo-1106",
    temperature=0.7,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant called Max."),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad")
])

search = TavilySearchResults()
tools = [search]

agent = create_openai_functions_agent(
    llm=model,
    prompt=prompt,
    tools=tools,
)

agentExectuor = AgentExecutor(
    agent=agent,
    tools=tools,
)

response = agentExectuor.invoke({
    "input": "Hello",
})
