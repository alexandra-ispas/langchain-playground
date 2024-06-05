from dotenv import load_dotenv

load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

#instantiate model
llm = ChatOpenAI(
    temperature=0.7,
    model="gpt-3.5-turbo-1106",
)

# Prompt template
# prompt = ChatPromptTemplate.from_template("Tell me a joke about a {subject}")
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are an Ai chief. create a receipe from these main ingredients")
        ("human", "{input}")
    ]
)
# Chains
# output from prompt is input for llm
chain = prompt | llm

# response = chain.invoke({"subject": "corporations"})
response = chain.invoke({"input": "tomatoes"})
print(response)
