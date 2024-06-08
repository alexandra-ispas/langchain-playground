from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.memory import ConversationBufferMemory
from langchain.chains import LLMChain

model = ChatOpenAI(
    model="gpt-3.5-turbo-1106",
    temperature=0.7,
)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a friendly assistant called Max."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
])

memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# chain = prompt | model
chain = LLMChain(
    llm=model,
    prompt=prompt,
    memory=memory,
    verbose=True,
)

msg = {
    "input": "Hello"
}
response = chain.invoke(msg)
print(response)
